#Напечатайте в консоль даты: вчера, сегодня, 30 дней назад

def dates():
    from datetime import datetime, date, timedelta

    date_today = datetime.now().date()
    delta1 = timedelta(days=1)
    delta2 = timedelta(days=30)

    yesterday = date_today - delta1
    yesterday = yesterday.strftime('%d.%m.%Y')
    month_ago = date_today - delta2
    month_ago = month_ago.strftime('%d.%m.%Y')
    date_today = date_today.strftime('%d.%m.%Y')

    print(f'Сегодня {date_today}')
    print(f'Вчера было {yesterday}')
    print(f'30 дней назад было {month_ago}')

dates()


#Превратите строку "01/01/25 12:10:03.234567" в объект datetime

from datetime import datetime
print(datetime.strptime('01/01/25 12:10:03.234567', '%d/%m/%y %H:%M:%S.%f'))