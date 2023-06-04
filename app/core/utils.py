from datetime import datetime, timedelta


def default_date():
    return datetime.now() + timedelta(days=365)
