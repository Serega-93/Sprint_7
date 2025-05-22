from datetime import date, timedelta

TOMORROW_DATE = (date.today() + timedelta(days=1)).strftime('%Y.%m.%d')
