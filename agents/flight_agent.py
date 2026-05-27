import random

airlines = [
    "IndiGo",
    "Air India",
    "Vistara",
    "SpiceJet"
]

def search_flights(departure, destination):

    flights = []

    for i in range(3):

        flights.append({
            "airline": random.choice(airlines),
            "flight_no": f"AI{random.randint(100,999)}",
            "price": random.randint(4000, 25000),
            "departure": departure,
            "arrival": destination,
            "duration": f"{random.randint(1,5)}h {random.randint(10,59)}m"
        })

    return flights