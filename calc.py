while True:
    date = input('Введи свою дату рождения в формате (DD MM YYYY)')
    import datetime
    now = datetime.datetime.now()
    yyear = int(now.year) - int(str(date[6:]))
    ymonth = int(now.month) - int(str(date[3:-5]))
    yday = int(now.day) - int(str(date[:-8]))
    if ymonth == 12:
        yyear = yyear + 1
        ymonth = ymonth - 12
    if int(now.month) - int(str(date[3:-5])) <= 0:
        yyear = yyear - 1
        ymonth = ymonth + 12
    if int(now.day) - int(str(date[:-8])) <= 0:
        ymonth = ymonth - 1
        yday = yday + 31
    print('Тебе сейчас: ' + str(yyear) + ' лет, ' + str(ymonth) + ' месяцев, ' + str(yday) + ' дней')
