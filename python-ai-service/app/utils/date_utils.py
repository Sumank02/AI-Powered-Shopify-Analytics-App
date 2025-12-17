from datetime import datetime, timedelta


def last_n_days(n: int) -> dict:
    end = datetime.utcnow()
    start = end - timedelta(days=n)

    return {
        "start_date": start.date().isoformat(),
        "end_date": end.date().isoformat()
    }
