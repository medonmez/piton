# Input for the price of the dream home
home = float(input("Enter the price of your dream home: "))

# Input for the salary
salary = float(input("Enter your salary: "))

# Input for the percentage of salary saved monthly
saving_percentage = float(input("Enter the percentage of your salary you save monthly (25 for 25%): "))

# Calculate the amount of money saved monthly
saving_money = salary * (saving_percentage / 100)

# Calculate the number of months needed to save enough money for the dream home by dividing the home price by the monthly saving amount
months = home / saving_money

# Round up the number of months to the upper integer, using the round() function. For example: 40.1 months rounds up to 41
# Adding 0.49999999 helps to correct upper rounding. If we use +0.5, 51 months(for example) rounds to 52 because it is a odd number.
months_upper_rounded = round(months + 0.49999999)

# Print the result with a formatted string, displaying the calculated number of months.
print(f"It will take {months_upper_rounded} months to save enough money for your dream home.")