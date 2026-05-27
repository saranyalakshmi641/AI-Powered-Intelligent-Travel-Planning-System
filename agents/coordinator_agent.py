from agents.flight_agent import search_flights
from agents.hotel_agent import recommend_hotel
from agents.itinerary_agent import create_itinerary
from agents.recommendation_agent import recommend_places
from agents.budget_agent import optimize_budget

def handle_travel(
    departure,
    destination,
    budget,
    seat_pref,
    travel_type,
    days
):

    flights = search_flights(
        departure,
        destination
    )

    selected_flight = flights[0]

    hotel = recommend_hotel(
        destination,
        budget
    )

    budget_data = optimize_budget(
        budget,
        selected_flight["price"],
        hotel["price"]
    )

    itinerary = create_itinerary(
        destination,
        days,
        travel_type
    )

    recommendations = recommend_places(
        destination
    )

    return {
        "flight": selected_flight,
        "hotel": hotel,
        "budget": budget_data,
        "itinerary": itinerary,
        "recommendations": recommendations,
        "all_flights": flights
    }