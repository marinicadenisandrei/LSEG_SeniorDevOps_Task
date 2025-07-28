from datetime import datetime
from collections import defaultdict
from termcolor import colored

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

def analyze_jobs(jobs):
    """
    Calculates durations and prints warnings/errors based on thresholds.
    """
    for key, job in jobs.items():
        start = job.get("start")
        end = job.get("end")

        if not start or not end:
            print(f"[INFO] Incomplete log for {key}")
            continue

        duration = end - start
        minutes = duration.total_seconds() / 60

        log_line = f"{key}: Duration = {duration}"

        if minutes > 10:
            print(f"[ERROR] {log_line}")
        elif minutes > 5:
            print(f"[WARNING] {log_line}")
        else:
            print(f"[OK] {log_line}")
