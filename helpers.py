from datetime import date, timedelta

def tomorrow_date():
    tomorrow = date.today() + timedelta(days=1)
    return tomorrow.strftime('%Y.%m.%d')