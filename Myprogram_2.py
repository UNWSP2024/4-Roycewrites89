#Royce Daniel. 2/13/2026 "Rainthinker"
years = int(input("Enter the number of years in this period: "))
total_rainfall = 0.0
total_months = 0

for year in range(1, years + 1):
    print("Year", year)

    for month in range(1, 13):
        rainfall = float(input(f"Enter rainfall for month {month} (in inches): "))
        total_rainfall += rainfall
        total_months += 1

average_rainfall = total_rainfall / total_months
print("RESULTS")
print("Total months:", total_months)
print("Total rainfall (inches):", total_rainfall)
print("Average rainfall per month:", average_rainfall)
