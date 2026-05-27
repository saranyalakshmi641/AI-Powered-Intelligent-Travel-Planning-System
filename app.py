# =========================================================
# ULTRA PROFESSIONAL AI TRAVEL PLANNER
# FULL UPDATED app.py
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

from agents.coordinator_agent import handle_travel
from agents.chatbot_agent import trip_chatbot

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Luxury AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================

if "trip_result" not in st.session_state:
    st.session_state.trip_result = None

if "latest_chat" not in st.session_state:
    st.session_state.latest_chat = {
        "question": "",
        "answer": ""
    }

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

/* ======================================================= */
/* HIDE STREAMLIT */
/* ======================================================= */

#MainMenu,
footer,
header {
    visibility: hidden;
}

/* ======================================================= */
/* PAGE */
/* ======================================================= */

.block-container {
    max-width: 100%;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* ======================================================= */
/* BACKGROUND */
/* ======================================================= */

.stApp {

    background:
    linear-gradient(
        135deg,
        rgba(5,10,25,0.95),
        rgba(18,24,55,0.92),
        rgba(76,29,149,0.88)
    ),

    url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;

    color: white;
}

/* ======================================================= */
/* SIDEBAR */
/* ======================================================= */

section[data-testid="stSidebar"] {

    background: #020817 !important;

    border-right:
    1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {

    color: white !important;

    font-weight: 700 !important;
}

/* ======================================================= */
/* TEXT INPUT */
/* ======================================================= */

.stTextInput input {

    background: white !important;

    color: black !important;

    border-radius: 12px !important;

    font-weight: 700 !important;
}

/* ======================================================= */
/* SELECTBOX FIX */
/* ======================================================= */

div[data-baseweb="select"] {

    background: white !important;

    border-radius: 12px !important;
}

/* Selected text */

div[data-baseweb="select"] * {

    color: black !important;

    fill: black !important;

    opacity: 1 !important;

    font-weight: 700 !important;
}

/* Dropdown popup */

div[data-baseweb="popover"] {

    background: white !important;
}

/* Dropdown options */

li[role="option"] {

    background: white !important;

    color: black !important;

    font-weight: 700 !important;

    font-size: 16px !important;
}

/* Hover */

li[role="option"]:hover {

    background: #dbeafe !important;

    color: black !important;
}

/* ======================================================= */
/* SLIDER */
/* ======================================================= */

.stSlider * {

    color: white !important;

    font-weight: 700 !important;
}

/* ======================================================= */
/* TITLE */
/* ======================================================= */

.main-title {

    text-align: center;

    font-size: 72px;

    font-weight: 900;

    background:
    linear-gradient(
        to right,
        #38bdf8,
        #818cf8,
        #c084fc
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    margin-bottom: 8px;
}

.subtitle {

    text-align: center;

    font-size: 24px;

    color: #e2e8f0;

    margin-bottom: 40px;
}

/* ======================================================= */
/* BUTTON */
/* ======================================================= */

.stButton > button {

    width: 100%;

    height: 58px;

    border: none;

    border-radius: 16px;

    background:
    linear-gradient(
        to right,
        #06b6d4,
        #6366f1,
        #8b5cf6
    );

    color: white;

    font-size: 18px;

    font-weight: 700;

    transition: 0.3s;
}

.stButton > button:hover {

    transform: scale(1.02);

    box-shadow:
    0px 8px 24px rgba(0,0,0,0.35);
}

/* ======================================================= */
/* GLASS CARD */
/* ======================================================= */

.glass {

    background:
    rgba(255,255,255,0.10);

    padding: 24px;

    border-radius: 22px;

    backdrop-filter: blur(14px);

    border:
    1px solid rgba(255,255,255,0.08);

    margin-bottom: 20px;

    color: white !important;

    line-height: 1.8;
}

/* ======================================================= */
/* FLIGHT CARD */
/* ======================================================= */

.flight-card {

    background:
    linear-gradient(
        135deg,
        rgba(59,130,246,0.22),
        rgba(139,92,246,0.22)
    );

    padding: 18px;

    border-radius: 20px;

    border:
    1px solid rgba(255,255,255,0.08);

    color: white !important;

    min-height: 280px;

    text-align: center;

    margin-bottom: 18px;
}

/* ======================================================= */
/* METRICS */
/* ======================================================= */

[data-testid="metric-container"] {

    background:
    rgba(255,255,255,0.10);

    border-radius: 18px;

    padding: 18px;

    border:
    1px solid rgba(255,255,255,0.08);
}

[data-testid="metric-container"] * {

    color: white !important;

    font-weight: 700 !important;
}

/* ======================================================= */
/* CHAT */
/* ======================================================= */

.chat-box {

    background:
    rgba(255,255,255,0.10);

    padding: 22px;

    border-radius: 18px;

    border:
    1px solid rgba(255,255,255,0.08);

    margin-top: 20px;

    color: white;

    line-height: 1.8;
}

/* ======================================================= */
/* TEXT */
/* ======================================================= */

h1,h2,h3,h4,h5,p,li {

    color: white !important;
}

</style>
""", unsafe_allow_html=True)
# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌍 Travel Preferences")

departure = st.sidebar.text_input(
    "Departure City",
    "Chennai"
)

destination = st.sidebar.text_input(
    "Destination City",
    "Dubai"
)

budget = st.sidebar.slider(
    "Budget",
    5000,
    200000,
    50000
)

travel_type = st.sidebar.selectbox(
    "Travel Type",
    [
        "Solo",
        "Family",
        "Friends",
        "Business",
        "Luxury"
    ]
)

days = st.sidebar.slider(
    "Trip Duration",
    1,
    15,
    5
)

seat_pref = st.sidebar.selectbox(
    "Seat Preference",
    [
        "Window",
        "Aisle",
        "Middle"
    ]
)

# =========================================================
# TITLE
# =========================================================

st.markdown("""
<div class="main-title">
✈️ Luxury AI Travel Planner
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Smart Travel Planning Using Multi-Agent AI + LLaMA
</div>
""", unsafe_allow_html=True)

# =========================================================
# BUTTON
# =========================================================

if st.button("🚀 Generate AI Travel Plan"):

    with st.spinner("🤖 AI Agents Planning Your Trip..."):

        result = handle_travel(
            departure,
            destination,
            budget,
            seat_pref,
            travel_type,
            days
        )

        st.session_state.trip_result = result

# =========================================================
# RESULTS
# =========================================================

if st.session_state.trip_result:

    result = st.session_state.trip_result

    flight = result["flight"]

    hotel = result["hotel"]

    budget_data = result["budget"]

    # =====================================================
    # METRICS
    # =====================================================

    st.subheader("📊 Travel Analytics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("✈️ Flight", f"₹{flight['price']}")
    c2.metric("🏨 Hotel", f"₹{hotel['price']}")
    c3.metric("💰 Remaining", f"₹{budget_data['remaining']}")
    c4.metric("⭐ Rating", hotel["rating"])

    # =====================================================
    # FLIGHT OPTIONS
    # =====================================================

    st.subheader("✈️ Flight Options")

    col1, col2, col3 = st.columns(3)

    flight_cols = [col1, col2, col3]

    for idx, f in enumerate(result["all_flights"][:3]):

        with flight_cols[idx]:

            st.markdown(f"""
            <div class="flight-card">

            <h2>✈️ {f['airline']}</h2>

            <h4>Flight: {f['flight_no']}</h4>

            <p>📍 {f['departure']} → {f['arrival']}</p>

            <p>⏱️ {f['duration']}</p>

            <h2 style="color:#22c55e;">
            ₹{f['price']}
            </h2>

            </div>
            """, unsafe_allow_html=True)

    # =====================================================
    # HOTEL
    # =====================================================

    st.subheader("🏨 Recommended Hotel")

    st.markdown(f"""
    <div class="glass">

    <h2>{hotel['name']}</h2>

    <p>📍 {hotel['location']}</p>

    <p>⭐ Rating: {hotel['rating']}</p>

    <h2 style="color:#22c55e;">
    ₹{hotel['price']}
    </h2>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    #ITINERARY IN POINTS
    # =====================================================

    st.subheader("🗓️ Complete Travel Itinerary")

    itinerary_lines = result["itinerary"].split("\n")

    clean_lines = []

    for line in itinerary_lines:

        line = (
            line.replace("*", "")
            .replace("#", "")
            .replace("•", "")
            .strip()
        )

        if len(line) > 8:
            clean_lines.append(line)

    st.markdown("""
    <div class="glass">
    """, unsafe_allow_html=True)

    for item in clean_lines:

    # Highlight Day headings
        if "Day" in item:

            st.markdown(
                f"### 🌟 {item}"
            )

        else:

            st.markdown(
                f"- {item}"
            )

    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # ATTRACTIONS
    # =====================================================

    st.subheader("🌟 Top Attractions")

    recommendations = result["recommendations"]

    recommendation_points = recommendations.split("\n")

    clean_rec = []

    for r in recommendation_points:

        r = r.strip()

        if len(r) > 5:

            clean_rec.append(r)

    clean_rec = clean_rec[:6]

    final_rec = ""

    for r in clean_rec:

        final_rec += f"<li>{r}</li>"

    st.markdown(f"""
    <div class="glass">

    <ul>
    {final_rec}
    </ul>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # PIE CHART
    # =====================================================

    st.subheader("💸 Budget Analytics")

    df = pd.DataFrame({

        "Category": [
            "Flight",
            "Hotel",
            "Remaining"
        ],

        "Amount": [
            budget_data["flight_cost"],
            budget_data["hotel_cost"],
            max(0, budget_data["remaining"])
        ]
    })

    fig = px.pie(
        df,
        values="Amount",
        names="Category",
        hole=0.5
    )

    fig.update_traces(
        textinfo='label+percent',
        textfont_size=18,
        textfont_color='white'
    )

    fig.update_layout(

        paper_bgcolor='rgba(0,0,0,0)',

        plot_bgcolor='rgba(0,0,0,0)',

        font=dict(
            color='white',
            size=18
        ),

        legend=dict(
            font=dict(
                color='white',
                size=15
            )
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # CHATBOT
    # =====================================================

    st.subheader("🤖 AI Travel Assistant")

    user_question = st.text_input(
        "Ask Anything About Your Trip",
        key="chat_input"
    )

    if st.button("Send"):

        if user_question.strip():

            with st.spinner("🤖 AI Thinking..."):

                response = trip_chatbot(
                    user_question,
                    result
                )

                # REMOVE HTML TAGS
                response = response.replace("<div>", "")
                response = response.replace("</div>", "")
                response = response.replace("<p>", "")
                response = response.replace("</p>", "")
                response = response.replace("<h3>", "")
                response = response.replace("</h3>", "")
                response = response.replace("<br>", " ")

                # SHORT RESPONSE
                response = trip_chatbot(
                    f"Answer shortly in 4-5 lines only: {user_question}",
                    result
                )

                st.session_state.latest_chat = {
                    "question": user_question,
                    "answer": response
                }

    # =====================================================
    # SHOW ONLY LATEST CHAT
    # =====================================================

    if st.session_state.latest_chat["question"]:
         st.markdown("### 🧑 You:")
         st.write(st.session_state.latest_chat["question"])
         
         st.markdown("### 🤖 AI:")
         st.success(st.session_state.latest_chat["answer"])


        
        