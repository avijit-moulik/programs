import math

x = int(input("Enter the initial investment amount: "))
annual_interest_rate = float(input("Enter the annual interest rate in percentage: ")) / 100
invest = float(x)
monthly_interest_rate = annual_interest_rate / 12

# Calculate monthly interest and return value
monthly_interest = invest * monthly_interest_rate
monthly_return_value = invest + monthly_interest

print("Monthly interest : ")
print(monthly_interest)

print("Monthly return value : ")
print(monthly_return_value)

# Calculate yearly interest and return value
yearly_interest = monthly_interest * 12
print("Yearly interest : ")
print(yearly_interest)

print("Yearly return value : ")
print(yearly_interest + invest)

# Calculate interest and return value after 10 years
total_interest_10_years = 0
for i in range(10):
    total_interest_10_years += yearly_interest

print("After 10 years : ")
print("Interest :")
print(total_interest_10_years)
print("10-year return value : ")
print(total_interest_10_years + invest)
