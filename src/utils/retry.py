import time

def retry(func, retries=1, delay=1):
    for attempt in range(retries + 1):
        try:
            return func()
        except Exception:
            if attempt == retries:
                raise
            time.sleep(delay)
