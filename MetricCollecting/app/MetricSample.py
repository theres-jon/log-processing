import attr
from typing import List
from datetime import datetime
import statistics


@attr.s
class MetricSampling():
    host: str = attr.ib()
    start_time: datetime = attr.ib()
    end_time: datetime = attr.ib()

    # TODO: Confirm what this value
    # actually represents
    interval: int = attr.ib()

    metrics: List[float] = attr.ib()

    @property
    def min_sample(self):
        return min(self.metrics)

    @property
    def max_sample(self):
        return max(self.metrics)

    @property
    def avg_sample(self):
        return round(statistics.mean(self.metrics), 2)
