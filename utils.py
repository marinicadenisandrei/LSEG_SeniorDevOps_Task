from datetime import datetime
from collections import defaultdict

TIME_FORMAT = "%H:%M:%S"

def parse_log_file(log_path):
    """
    Parses the log file and returns a dictionary of job start and end events.
    """
     
    jobs = defaultdict(dict)

    with open(log_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            time_str, job_desc, status, pid = [p.strip() for p in parts]
            timestamp = datetime.strptime(time_str, TIME_FORMAT)
            key = f"{job_desc}-{pid}"
            status = status.upper()

            if status == "START":
                jobs[key]["start"] = timestamp
                jobs[key]["desc"] = job_desc
            elif status == "END":
                jobs[key]["end"] = timestamp

    return jobs
