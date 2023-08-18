import pytest

def retry(max_retries=3):
    def decorator(func):
        def wrapper(*args, ** kwargs):
            for attempt in range(max_retries + 1):
                try: 
                    func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries:
                        raise e
                    print(f"Attemp {attempt + 1}/{max_retries} failed. Retrying...")
                else:
                    break
        return wrapper
    return decorator

@pytest.mark.skip
def test_divide_by_zero():
    result = 5 / 0
    assert result == 1

@retry()
def test_subtraction():
    assert (5-5) == 0


if __name__ == "__main__":
    pytest.main()
    