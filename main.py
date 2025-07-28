from utils import parse_log_file
import os

if __name__ == "__main__":
    log_path = "logs.log"

    if not os.path.exists(log_path):
        print(f"Log file '{log_path}' not found!")
        exit()

    jobs = parse_log_file(log_path)
