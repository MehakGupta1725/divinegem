import streamlit as st
import pandas as pd

from database import (
    save_recommendation,
    save_consultation,
    get_user_recommendations
)

from recommendation_engine import get_recommendation
from gemstones import gemstones


def show_user_dashboard(username):

    st.title("💎 User Dashboard")

    st.write(f"Welcome, **{username}**!")

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Get Recommendation",
            "My Recommendations",
            "Book Consultation"
        ]
    )

    # Recommendation
    if menu == "Get Recommendation":

        st.header("🔮 Gemstone Assessment")

        zodiac = st.selectbox(
            "Select Your Zodiac Sign",
            [
                "Aries", "Taurus", "Gemini", "Cancer",
                "Leo", "Virgo", "Libra", "Scorpio",
                "Sagittarius", "Capricorn",
                "Aquarius", "Pisces"
            ]
        )

        concern = st.selectbox(
            "Primary Concern",
            [
                "Career",
                "Finance",
                "Love & Marriage",
                "Health",
                "Education"
            ]
        )

        if st.button("✨ Get Recommendation"):

            result = get_recommendation(
                zodiac,
                concern
            )

            primary = result["primary"]

            save_recommendation(
                username,
                zodiac,
                concern,
                primary
            )

            gem = gemstones[primary]

            st.success(
                f"Recommended Gemstone: {primary}"
            )

            st.write(
                f"**Planet:** {gem['planet']}"
            )

            st.write("### Benefits")

            for benefit in gem["benefits"]:
                st.write(f"✅ {benefit}")

            st.info(
                gem["wearing_instructions"]
            )

            st.warning(
                gem["precautions"]
            )

            st.write(
                f"**Reason:** {result['reason']}"
            )

    # Recommendation History
    elif menu == "My Recommendations":

        st.header("📜 My Recommendations")

        recommendations = (
            get_user_recommendations(
                username
            )
        )

        if recommendations:

            df = pd.DataFrame(
                recommendations,
                columns=[
                    "ID",
                    "Username",
                    "Zodiac",
                    "Concern",
                    "Gemstone",
                    "Date"
                ]
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info(
                "No recommendations found."
            )

    # Consultation
    elif menu == "Book Consultation":

        st.header(
            "🧙 Book Consultation"
        )

        phone = st.text_input(
            "Phone Number"
        )

        preferred_date = (
            st.date_input(
                "Preferred Date"
            )
        )

        if st.button(
            "📅 Request Consultation"
        ):

            if phone.strip():

                save_consultation(
                    username,
                    phone,
                    str(preferred_date)
                )

                st.success(
                    "Consultation request submitted!"
                )

            else:

                st.error(
                    "Please enter phone number."
                )