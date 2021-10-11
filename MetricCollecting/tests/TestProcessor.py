import unittest
from MetricCollecting.app.MetricProcessor import MetricProcessor as processor
import random
import datetime
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))


# We're going to create test cases for everything
# except the FileStream as that's primarily a
# built-in method pass-thru

class TestProcessor(unittest.TestCase):
    def setUp(self):
        log_entries = []
        log_entries.append("n10,1366829460,1366831260,60|37.0,65.0,87.1,41.0,76.0,83.0,82.0,50.0,54.0,46.0")
        log_entries.append("n27,1366829460,1366831260,60|63.0,100.0,94.0,78.0,66.0,89.0,79.0,97.0,92.0,76.0,76.0,21.5")

        self.metric_collection = [processor.process_log_entry(line) for line in log_entries]

    # Creating this for future use - testing performance or streaming data
    def create_mock_data(self):

        host = random.randrange(0, 10000)
        time_stamp = datetime.datetime.now().timestamp()
        interval = random.randrange(0, 100)

        # This could be improved
        metric_list = [random.uniform(0, 100.0) for i in range(100)]
        metric_list = [str(x) for x in metric_list]
        metric_formatted_list = str(metric_list).replace('[', '').replace(']', '').strip()
        return f"n{host},{time_stamp},{time_stamp},{interval}|{metric_formatted_list}"

    def test_list_size(self):
        self.assertEqual(2, len(self.metric_collection))

    def test_aggregate_min(self):
        self.assertEqual(37.0, self.metric_collection[0].min_sample)
        self.assertEqual(21.5, self.metric_collection[1].min_sample)

    def test_aggregate_max(self):
        self.assertEqual(87.1, self.metric_collection[0].max_sample)
        self.assertEqual(100.0, self.metric_collection[1].max_sample)

    def test_aggregate_average(self):
        self.assertEqual(62.11, self.metric_collection[0].avg_sample)
        self.assertEqual(77.62, self.metric_collection[1].avg_sample)

    def test_aggregate_running_aggregates(self):
        local_metric_collection = self.metric_collection[1]

        # Double check average
        self.assertEqual(77.62, local_metric_collection.avg_sample)

        # Add a new metric and ensure the aggregate
        # property is setting the new metric
        local_metric_collection.metrics.append(1.1)
        self.assertEqual(71.74, local_metric_collection.avg_sample)
        self.assertEqual(1.1, local_metric_collection.min_sample)

    def test_generate_mock_data(self):
        mock = self.create_mock_data()
        log_entry = processor.process_log_entry(mock)
        self.assertTrue(log_entry.min_sample > 0)
