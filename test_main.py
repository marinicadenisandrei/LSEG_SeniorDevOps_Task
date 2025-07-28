import unittest
from datetime import datetime, timedelta
from utils import get_job_analysis

class TestAnalyzeJobs(unittest.TestCase):

    def setUp(self):
        now = datetime.strptime("12:00:00", "%H:%M:%S")
        self.jobs = {
            "short-job-123": {
                "start": now,
                "end": now + timedelta(minutes=4),
            },
            "warning-job-456": {
                "start": now,
                "end": now + timedelta(minutes=7),
            },
            "error-job-789": {
                "start": now,
                "end": now + timedelta(minutes=12),
            },
            "incomplete-job-999": {
                "start": now,
                # no 'end'
            },
        }

    def test_ok_job(self):
        result = get_job_analysis(self.jobs)
        job = next(row for row in result if row[0].startswith("short-job"))
        self.assertEqual(job[3], "[OK]")

    def test_warning_job(self):
        result = get_job_analysis(self.jobs)
        job = next(row for row in result if row[0].startswith("warning-job"))
        self.assertEqual(job[3], "[WARNING]")

    def test_error_job(self):
        result = get_job_analysis(self.jobs)
        job = next(row for row in result if row[0].startswith("error-job"))
        self.assertEqual(job[3], "[ERROR]")

    def test_incomplete_job(self):
        result = get_job_analysis(self.jobs)
        job = next(row for row in result if row[0].startswith("incomplete-job"))
        self.assertIn("Incomplete log", job[3])

if __name__ == "__main__":
    unittest.main()
