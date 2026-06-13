import streamlit as st
import pandas as pd

from database import (
    save_recommendation,
    save_consultation,
    get_user_recommendations
)

from recommendation_engine import get_recommendation
from gemstones import gemstones

gem_images = {
    "Emerald": "assets/Emerald.png",
    "Ruby": "assets/Ruby.png",
    "Diamond": "assets/Diamond.png",
    "Pearl": "assets/Pearl.png",
    "Yellow Sapphire": "assets/Yellow Sapphire.png",
    "Blue Sapphire": "assets/Blue Sapphire.png",
    "Coral": "assets/Coral.png",
}


def show_user_dashboard(username):

    st.title("💎 DivineGem")

    st.subheader(
    f"Welcome back, {username} 👋"
)

    st.write(
    "Explore personalized gemstone guidance "
    "and manage your consultations."
)

    st.divider()

    tab1, tab2, tab3 = st.tabs([
    "🔮 Get Recommendation",
    "📜 My History",
    "📅 Book Consultation"
])

    # Recommendation
    with tab1:

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

            st.markdown(f"""
## 💎 {primary}

Your personalized recommendation.
""")

            st.write(
                f"**Planet:** {gem['planet']}"
            )

            st.subheader("✨ Benefits")

            for benefit in gem["benefits"]:
                st.write(f"✅ {benefit}")

            with st.expander(
           "🧿 Wearing Instructions"
            ):
             st.write(
            gem["wearing_instructions"]
    )

            with st.expander(
                "⚠️ Precautions"
            ):
             st.write(
             gem["precautions"]
            )

            st.write(
                f"**Reason:** {result['reason']}"
            )

    # Recommendation History
    with tab2:

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
    with tab3:

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

