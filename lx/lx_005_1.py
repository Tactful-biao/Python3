#!/usr/bin/env python
month=[
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]
ending= ['st','nd','rd']+7*['th']\
        +['st','nd','rd']+7*['th']\
        +['st','nd','rd']+7*['th']\
        +['st']

year = input ('Year :')
months=input ('Month (1-12):')
day=input('Day (1-31):')

month_number=int(months)
day_number=int(day)

month_name=month[month_number-1]
day_name=ending[day_number-1]

print (month_name + ' ' + day + day_name + '. ' + year)
