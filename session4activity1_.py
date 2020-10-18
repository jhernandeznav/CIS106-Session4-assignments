# Activity one
year_age = int(input('How old are you? '))


def years():
    year = year_age * 1
    return year


def months():
    month = years() * 12
    return month


def days():
    day = months() * 365
    return day


def display_years(year):
    print(year, 'Years')


def display_months(month):
    print(month, 'Months')


def display_days(day):
    print(day, 'Days')


def main():
    year = years()
    display_years(year)
    month = months()
    display_months(month)
    day = days()
    display_days(day)


main()
