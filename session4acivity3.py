# Activity 3
num_tickets = float(input('Enter the number of airline tickets: '))
price_per_seat = float(input('Enter the price per seats:$'))


def cost_per_seats():
    cost = price_per_seat * num_tickets
    return cost


def tax_tickets():
    tax = cost_per_seats() * .07
    return tax


def total_tickets():
    total = cost_per_seats() + tax_tickets()
    return total


print('Number of plane tickets:', num_tickets)
print('Price per seat:$ ', price_per_seat)


def display_result(cost):
    print('The cost of the plane tickets:$', cost)


def display(tax):
    print('The tax of the plane tickets:$', tax)


def display_total(total):
    print('The total cost of the plane tickets:$ ', total)


def main():
    cost = cost_per_seats()
    display_result(cost)
    tax = tax_tickets()
    display(tax)
    total = total_tickets()
    display_total(total)


main()
