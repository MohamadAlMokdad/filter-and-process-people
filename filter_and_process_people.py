def filter_and_process_people(people):
    # Advanced list filtering with multiple conditions
    filtered_people = [
        person for person in people
        if person['age'] >= 30 and person['income'] > 65000 and person['city'] == "New York"
    ]

    # Processing the filtered list to extract names
    names_of_filtered_people = [person['name'] for person in filtered_people]

    # Using nested loop to check for specific city and print their info
    for person in people:
        if person['city'] == 'Chicago':
            print(f"Checking person from Chicago: {person['name']}, Age: {person['age']}, Income: {person['income']}")

    # Output the names of people who meet the advanced filtering criteria
    print("\nFiltered people based on conditions (Age >= 30, Income > 65000, City = 'New York'):")
    print(names_of_filtered_people)

    # Example with if-else in list comprehension for custom messages
    income_brackets = [
        "High Income" if person['income'] >= 80000 else "Medium Income" 
        for person in people
    ]

    # Printing income brackets based on the logic above
    print("\nIncome brackets of all people:")
    print(income_brackets)

    # Advanced use of list comprehension with nested if conditions
    people_with_high_income_in_ny = [
        person for person in people
        if person['income'] > 80000 and person['city'] == "New York"
    ]

    # Output names of people with high income in New York
    print("\nPeople with high income in New York:")
    for person in people_with_high_income_in_ny:
        print(person['name'])

# Sample list of dictionaries containing people data
people = [
    {"name": "Alice", "age": 30, "city": "New York", "income": 70000},
    {"name": "Bob", "age": 25, "city": "Los Angeles", "income": 80000},
    {"name": "Charlie", "age": 35, "city": "Chicago", "income": 60000},
    {"name": "David", "age": 40, "city": "New York", "income": 90000},
    {"name": "Eve", "age": 29, "city": "San Francisco", "income": 95000},
    {"name": "Frank", "age": 32, "city": "Chicago", "income": 55000},
]

# Call the function with the sample data
filter_and_process_people(people)
