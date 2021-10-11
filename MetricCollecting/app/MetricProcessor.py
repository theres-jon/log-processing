import logging
from typing import List
from MetricCollecting.app.MetricSample import MetricSampling


class MetricProcessor():

    @staticmethod
    def process_log_entry(data: str) -> MetricSampling:
        # Future enhancement: Allow for regex pattern at class level
        # for matching rather than splitting. Would be nice to keep
        # this as flexible as possible.
        entry: List[str] = data.split('|')

        if len(entry) == 2:
            metadata: List[str] = entry[0].split(',')
            readings: List[float] = entry[1].split(',')

            # Edge case that came out of testing where
            # we have to handle spaces between metric readings
            readings = [x.strip() for x in readings]

            # Sometimes the type hints are useless and we need to
            # hit Python with a hammer. We need the readings as floats
            # so we can run calculations on them.
            #
            # Additionally we're dropping None values here
            # as to not dilute the averave aggregation.
            readings = [float(reading) for reading in readings if reading != 'None']

            try:
                metric_sample: MetricSampling = MetricSampling(
                    *metadata,
                    metrics=readings
                )
                return metric_sample

            except Exception as ex:
                logging.error(ex)
                return
