import csv

lowest_expectancy = float('inf')
highest_expectancy = float('-inf')
largest_drop = 0
largest_drop_country = ""
largest_drop_year = 0

# Initialize a dictionary to store life expectancy data by entity (country)
entity_data = {}

# Read the data from the CSV file
with open('life-expectancy.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    for row in reader:
        entity, code, year, expectancy = row

        # Split each line into parts and convert year and expectancy to appropriate data types
        year = int(year)
        expectancy = float(expectancy)

        # Find the lowest and highest life expectancy values
        if expectancy < lowest_expectancy:
            lowest_expectancy = expectancy
        if expectancy > highest_expectancy:
            highest_expectancy = expectancy

        # Check for the largest drop between two years
        if year > 1950:
            previous_year = year - 1
            if entity in entity_data and previous_year in entity_data[entity]:
                drop = expectancy - entity_data[entity][previous_year]
                if drop < largest_drop:
                    largest_drop = drop
                    largest_drop_country = entity
                    largest_drop_year = year

        # Store life expectancy data by entity
        if entity not in entity_data:
            entity_data[entity] = {}
        entity_data[entity][year] = expectancy

# Allow the user to input a year
search_year = int(input("Enter the year of interest: "))

# Find the overall max and min life expectancy
overall_max_entity = ""
overall_max_expectancy = 0
overall_min_entity = ""
overall_min_expectancy = float('inf')

for entity, data in entity_data.items():
    if search_year in data:
        expectancy = data[search_year]
        if expectancy > overall_max_expectancy:
            overall_max_entity = entity
            overall_max_expectancy = expectancy
        if expectancy < overall_min_expectancy:
            overall_min_entity = entity
            overall_min_expectancy = expectancy

print(f"The overall max life expectancy is: {overall_max_expectancy:.2f} from {overall_max_entity} in {search_year}")
print(f"The overall min life expectancy is: {overall_min_expectancy:.2f} from {overall_min_entity} in {search_year}")

# Calculate average life expectancy and max/min for the given year
if search_year in entity_data:
    year_data = entity_data[search_year]
    expectancies = year_data.values()
    average_expectancy = sum(expectancies) / len(expectancies)
    max_expectancy = max(expectancies)
    min_expectancy = min(expectancies)
    max_entity = [entity for entity, expectancy in year_data.items() if expectancy == max_expectancy][0]
    min_entity = [entity for entity, expectancy in year_data.items() if expectancy == min_expectancy][0]
    print(f"\nFor the year {search_year}:")
    print(f"The average life expectancy across all countries was {average_expectancy:.3f}")
    print(f"The max life expectancy was in {max_entity} with {max_expectancy:.3f}")
    print(f"The min life expectancy was in {min_entity} with {min_expectancy:.3f}")
else:
    print(f"\nData for the year {search_year} is not available in the dataset.")

# Print the lowest and highest life expectancy values
print(f"\nLowest Life Expectancy: {lowest_expectancy:.2f}")
print(f"Highest Life Expectancy: {highest_expectancy:.2f}")

# Print the country and year with the largest drop
if largest_drop != 0:
    print(f"\nLargest Drop: {largest_drop:.2f} years in {largest_drop_country} in {largest_drop_year}")
else:
    print("\nNo data available to calculate the largest drop between two years.")