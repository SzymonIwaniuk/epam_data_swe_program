from contextlib import ContextDecorator
from datetime import datetime
import time


class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.start_time = datetime.now()
        self.start_perf = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_perf = time.perf_counter()
        run_time = end_perf - self.start_perf
        run_time_str = str(datetime.utcfromtimestamp(run_time).time())

        error_msg = None if exc_val is None else str(exc_val)
        log_line = f"Start: {self.start_time} | Run: {run_time_str} | An error occurred: {error_msg}\n"

        with open(self.filename, "a") as f:
            f.write(log_line)

        return False

