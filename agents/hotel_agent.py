import random

hotels = [
    "Taj Palace",
    "ITC Grand",
    "The Oberoi",
    "Holiday Inn",
    "Radisson Blu"
]

def recommend_hotel(destination, budget):

    hotel = random.choice(hotels)

    price = random.randint(3000, 12000)

    return {
        "name": hotel,
        "price": price,
        "location": destination,
        "rating": round(random.uniform(3.5, 5.0), 1)
    }