def optimize_budget(
    user_budget,
    flight_price,
    hotel_price
):

    remaining = (
        user_budget
        - flight_price
        - hotel_price
    )

    return {
        "total_budget": user_budget,
        "flight_cost": flight_price,
        "hotel_cost": hotel_price,
        "remaining": remaining
    }