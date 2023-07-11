"""
Theme: Car brands

The project features 11 highly regarded car brands on the market along with three attributes to find out which brand is the best option.
"""

# Database
cars = [
    {"brand": "Jaguar", "attributes": {"Consumption": 7, "Security": 8, "Design": 9, "Speed": 7, "Comfort": 8, "Price": 7}},
    {"brand": "Porsche", "attributes": {"Consumption": 6, "Security": 9, "Design": 10, "Speed": 9, "Comfort": 8, "Price": 8}},
    {"brand": "Mercedez-Benz", "attributes": {"Consumption": 7, "Security": 9, "Design": 9, "Speed": 8, "Comfort": 9, "Price": 8}},
    {"brand": "Chevrolet", "attributes": {"Consumption": 8, "Security": 7, "Design": 7, "Speed": 6, "Comfort": 7, "Price": 6}},
    {"brand": "Ferrari", "attributes": {"Consumption": 5, "Security": 8, "Design": 10, "Speed": 10, "Comfort": 7, "Price": 10}},
    {"brand": "Ford", "attributes": {"Consumption": 8, "Security": 7, "Design": 7, "Speed": 7, "Comfort": 8, "Price": 6}},
    {"brand": "McLaren", "attributes": {"Consumption": 6, "Security": 8, "Design": 10, "Speed": 10, "Comfort": 7, "Price": 10}},
    {"brand": "Maserati", "attributes": {"Consumption": 6, "Security": 9, "Design": 9, "Speed": 9, "Comfort": 8, "Price": 9}},
    {"brand": "Lamborghini", "attributes": {"Consumption": 5, "Security": 8, "Design": 9, "Speed": 10, "Comfort": 7, "Price": 9}},
    {"brand": "Dodge", "attributes": {"Consumption": 7, "Security": 7, "Design": 6, "Speed": 7, "comfort": 7, "Price": 6}},
    {"brand": "Rolls-Royce", "attributes": {"Consumption": 6, "Security": 10, "Design": 10, "Speed": 8, "Comfort": 10, "Price": 10}}
]

# Request three attributes
print("Enter the three main features to choose a car:")
print("Consumption | Security | Design | Speed | Comfort | Price")

validAttributes = False
while not validAttributes:
    firstFeature = input("Feature 1: ")
    secondFeature = input("Feature 2: ")
    thirdFeature = input("Feature 3: ")

    # Values ​​of the three resources
    attributes = [firstFeature, secondFeature, thirdFeature]

    # Check user-entered attributes
    foundAttributes = set()
    for car in cars:
        for attr in attributes:
            if attr in car['attributes']:
                foundAttributes.add(attr)

    if set(attributes) == foundAttributes:
        validAttributes = True
    else:
        print("One or more of the entered attributes are not present in the dataset. Please enter the attributes again.")

# Calculates the probability that each brand is the best choice


def calculateProportion(brand):
    allAttributes = sum(brand['attributes'].values())
    userAttributes = sum([brand['attributes'][attr] for attr in attributes])
    proportion = userAttributes / allAttributes
    return proportion


# Put the results obtained into "probability"
probability = {}
for car in cars:
    brand = car['brand']
    proportion = calculateProportion(car)
    probability[brand] = proportion

# Sort results in descending order
classification = sorted(probability.items(), key=lambda x: x[1], reverse=True)

# Prints the odds
for brand, proportion in classification:
    print(f"\n{brand}: {round(proportion * 100, 2)}%\n")
