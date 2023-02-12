# replace ??? with Python code
quarters = int(input('Counts of quarters: '))

dimes = int(input('Counts of dimes: '))

nickels = int(input('Counts of nickels: '))

pennies = int(input('Counts of pennies: '))

dollars = quarters/4 + dimes/10 + nickels/20 + pennies/100

print(f'Amount: ${dollars:.2f}')