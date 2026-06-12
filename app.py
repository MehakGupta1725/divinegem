import streamlit as st
from database import create_tables, save_recommendation
from recommendation_engine import get_recommendation
from gemstones import gemstones

# Initialize database
create_tables()
from database import initialize_admin

initialize_admin()
# Page configuration
st.set_page_config(
    page_title="DivineGem",
    page_icon="💎",
    layout="wide"
)

# App title
st.title("💎 DivineGem")
st.subheader("AI-Assisted Gemstone Recommendation Platform")

st.markdown("""
Get personalized gemstone recommendations based on your
**zodiac sign** and **life concerns**.
""")

st.divider()

# User Input Form
with st.form("recommendation_form"):

    st.header("🔮 Gemstone Assessment")

    name = st.text_input("Full Name")

    zodiac = st.selectbox(
        "Select Your Zodiac Sign",
        [
            "Aries",
            "Taurus",
            "Gemini",
            "Cancer",
            "Leo",
            "Virgo",
            "Libra",
            "Scorpio",
            "Sagittarius",
            "Capricorn",
            "Aquarius",
            "Pisces"
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

    submitted = st.form_submit_button(
        "✨ Get Recommendation"
    )

if submitted:

    if not name.strip():
        st.error("Please enter your name.")
    else:

        result = get_recommendation(
            zodiac,
            concern
        )

        primary = result["primary"]
        alternative = result["alternative"]

        save_recommendation(
            name,
            zodiac,
            concern,
            primary
        )

        st.success(
            f"Thank you, {name}! "
            "Here are your recommendations."
        )

        st.divider()

        st.header("💎 Recommended Gemstone")

        gem = gemstones[primary]

        st.subheader(primary)

        st.write(
            f"**Associated Planet:** "
            f"{gem['planet']}"
        )

        st.write("### Benefits")

        for benefit in gem["benefits"]:
            st.write(f"✅ {benefit}")

        st.write(
            "### Wearing Instructions"
        )

        st.info(
            gem["wearing_instructions"]
        )

        st.write("### Precautions")

        st.warning(
            gem["precautions"]
        )

        st.write("### Why This Recommendation?")

        st.write(result["reason"])

        if primary != alternative:

            st.divider()

            st.header(
                "🔹 Alternative Recommendation"
            )

            alt = gemstones[alternative]

            st.subheader(alternative)

            st.write(
                f"**Associated Planet:** "
                f"{alt['planet']}"
            )

            st.divider()

st.header("🧙 Book an Astrologer Consultation")

st.write(
    "Need personalized guidance? "
    "Submit a consultation request."
)

with st.form("consultation_form"):

    consult_name = st.text_input(
        "Full Name",
        key="consult_name"
    )

    phone = st.text_input(
        "Phone Number"
    )

    preferred_date = st.date_input(
        "Preferred Consultation Date"
    )

    consultation_submitted = (
        st.form_submit_button(
            "📅 Request Consultation"
        )
    )

if consultation_submitted:

    if (
        consult_name.strip()
        and phone.strip()
    ):

        from database import (
            save_consultation
        )

        save_consultation(
            consult_name,
            phone,
            str(preferred_date)
        )

        st.success(
            "Consultation request "
            "submitted successfully!"
        )

    else:

        st.error(
            "Please fill all fields."
        )