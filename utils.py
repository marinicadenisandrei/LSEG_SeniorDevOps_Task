from datetime import datetime
from collections import defaultdict
from termcolor import colored
from tabulate import tabulate

TIME_FORMAT = "%H:%M:%S"

def parse_log_file(log_path):
    """
    Parses the log file and returns a dictionary of job start and end events.
    """
    jobs = defaultdict(dict)

    with open(log_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) != 4:
                continue  # skip malformed lines

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

def get_job_analysis(jobs):
    """
    Returns a list of [key, duration_str, minutes_str, status_str] without coloring or printing.
    Useful for testing.
    """
    results = []

    for key, job in jobs.items():
        start = job.get("start")
        end = job.get("end")

        if not start or not end:
            results.append([key, "Incomplete", "-", "[INFO] Incomplete log"])
            continue

        duration = end - start
        minutes = duration.total_seconds() / 60

        if minutes > 10:
            status = "[ERROR]"
        elif minutes > 5:
            status = "[WARNING]"
        else:
            status = "[OK]"

        results.append([key, f"{duration}", f"{minutes:.2f}", status])

    return results

def analyze_jobs(jobs):
    """
    Calculates durations and prints warnings/errors in a color-coded table.
    """
    raw_results = get_job_analysis(jobs)

    colored_results = []
    for job, duration, minutes, status in raw_results:
        if status.startswith("[ERROR]"):
            status = colored(status, "red")
        elif status.startswith("[WARNING]"):
            status = colored(status, "yellow")
        elif status.startswith("[OK]"):
            status = colored(status, "green")
        elif status.startswith("[INFO]"):
            status = colored(status, "cyan")

        colored_results.append([job, duration, minutes, status])

    headers = ["Job", "Duration", "Minutes", "Status"]
    print(tabulate(colored_results, headers=headers, tablefmt="grid"))
