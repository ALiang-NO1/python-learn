import time
from retrying import retry

@retry
def test_retry():
    """"""
    try:
        1/0
    except Exception as e:
        print(e)
        raise e

@retry(stop_max_attempt_number=4)
def stop_times():
    print("Stopping after 4 attempts.")
    raise
# stop_4()

@retry(stop_max_delay=2000)
def stop_ms():
    print("Stopping after 2 seconds.")
# stop_ms()

@retry(wait_fixed=2000, stop_max_delay=1000)
def fix_time():
    print("Wait 2 seconds between retriex.")
# fix_time()

@retry(wait_random_min=1000, wait_random_max=2000)
def wait_between():
    print("Randomly wait 1 to 3 seconds between retries.")
    raise
# wait_between()

@retry(wait_exponential_multiplier=1000, wait_exponential_max=3000)
def wait_exponential():
    print("Wait 2^x 1000 milliseconds between each retry, up to 3 seconds.")
    print(int(time.time()))
    raise
# wait_exponential()

def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, IOError)

@retry(retry_on_exception=retry_if_io_error)
def might_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any other errors")
    raise Exception('a')

@retry(retry_on_exception=retry_if_io_error, wrap_exception=True)
def only_raise_retry_error_when_not_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any other errors wrapped in RetryError")
    raise Exception('a')

def retry_if_result_none(result):
    return result is None

@retry(retry_on_result=retry_if_result_none)
def get_result():
    print('Retry forever ignoring Exceptions with no wait if return value is None')
    return None