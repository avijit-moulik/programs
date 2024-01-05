import math

initial_investment = float(input("Enter the initial investment amount: "))
annual_interest_rate = float(input("Enter the annual interest rate in percentage: ")) / 100
monthly_deposit = float(input("Enter the monthly deposit amount: "))

invest = initial_investment
monthly_interest_rate = annual_interest_rate / 12

# Calculate monthly interest and return value
for month in range(12):
    monthly_interest = invest * monthly_interest_rate
    invest += monthly_deposit  # Add monthly deposit
    invest += monthly_interest  # Add monthly interest
    print(f"Month {month + 1}:")
    print("Monthly interest:", monthly_interest)
    print("Monthly return value:", invest)

# Calculate yearly interest and return value
yearly_interest = monthly_interest * 12
print("Yearly interest : ")
print(yearly_interest)

print("Yearly return value : ")
print(yearly_interest + initial_investment)

# Calculate interest and return value after 10 years
total_interest_10_years = 0
for i in range(10):
    total_interest_10_years += yearly_interest

print("After 10 years : ")
print("Interest :")
print(total_interest_10_years)
print("10-year return value : ")
print(total_interest_10_years + initial_investment)
