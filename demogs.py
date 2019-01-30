from datetime import date, datetime

def calculate_age(born):
    today = date.today()
    birthdate = lambda b: datetime.strptime(b, '%Y-%m-%d')
    born = birthdate(born)
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


