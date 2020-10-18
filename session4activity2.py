# activity 2
name = input('Enter your last name: ')
score_one = float(input('Enter the score for 1: '))
score_two = float(input('Enter the score for 2: '))


def cal_average_one():
    cal_one = score_one * (40 / 100)
    return cal_one


def cal_average_two():
    cal_two = score_two * (60 / 100)
    return cal_two


def total_score():
    total = cal_average_one() + cal_average_two()
    return total


print(name)
print('Test score 1: ', score_one)
print('Test score 2: ', score_two)


def display_results(total):
    print('Total score: ', total)


def main():
    total = total_score()
    display_results(total)


main()
