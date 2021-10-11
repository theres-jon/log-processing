from MetricCollecting.app.MetricProcessor import MetricProcessor
from MetricCollecting.app.FileStream import FileStream
import sys


def main(args):
    metric_reader = FileStream.read_file(args)

    # No point in our processor being a generator also
    # as we need to store all the values in memory so
    # we can print a sorted list
    metric_collection = [MetricProcessor.process_log_entry(line) for line in metric_reader]

    # Remove None values that could come from exception handling
    metric_collection = [v for v in metric_collection if v]

    metric_collection = sorted(
        metric_collection,
        key=lambda x: x.avg_sample,
        reverse=True
    )

    # Future enhancement - We may want to aggregate multiple
    # files from the same host. This is assuming each host
    # only has one file.
    for host_metrics in metric_collection:
        print(f"{host_metrics.host}: Average: {host_metrics.avg_sample} Max: {host_metrics.max_sample} Min: {host_metrics.min_sample}")


if __name__ == "__main__":
    # Future enhancement - add named parameters
    # for parsing as this is obviouly pretty
    # brittle.
    #
    # Future enhnacement - add a flag for type of
    # processing - local log, stream, s3, etc
    #
    # Adding this for local dev experience.
    # Would need refactored or removed prior
    # to prod.
    args = sys.argv[1] if len(sys.argv) > 1 else "fake_msgs.log"
    main(args)
