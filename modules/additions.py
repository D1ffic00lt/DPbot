from datetime import datetime


def get_time() -> str:
    return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
