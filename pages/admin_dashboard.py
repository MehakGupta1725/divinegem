import streamlit as st
import pandas as pd

from database import (
    get_users,
    get_recommendations,
    get_consultations
)


def show_admin_dashboard():

    st.title("📊 Admin Dashboard")

    menu = st.sidebar.selectbox(
        "Admin Menu",
        [
            "Analytics",
            "Users",
            "Recommendations",
            "Consultations"
        ]
    )

    # Analytics
    if menu == "Analytics":

        st.header("📈 Platform Analytics")

        users = get_users()
        recommendations = get_recommendations()
        consultations = get_consultations()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Total Users",
                len(users)
            )

            st.metric(
                "Total Recommendations",
                len(recommendations)
            )

        with col2:

            st.metric(
                "Total Consultations",
                len(consultations)
            )

            if recommendations:

                rec_df = pd.DataFrame(
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

                common_gem = (
                    rec_df["Gemstone"]
                    .mode()[0]
                )

                st.metric(
                    "Most Recommended Gemstone",
                    common_gem
                )

    # Users
    elif menu == "Users":

        st.header("👥 Registered Users")

        users = get_users()

        if users:

            df = pd.DataFrame(
                users,
                columns=[
                    "ID",
                    "Username",
                    "Role"
                ]
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info(
                "No users found."
            )

    # Recommendations
    elif menu == "Recommendations":

        st.header(
            "💎 Recommendation History"
        )

        recommendations = (
            get_recommendations()
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

    # Consultations
    elif menu == "Consultations":

        st.header(
            "🧙 Consultation Requests"
        )

        consultations = (
            get_consultations()
        )

        if consultations:

            df = pd.DataFrame(
                consultations,
                columns=[
                    "ID",
                    "Username",
                    "Phone",
                    "Preferred Date",
                    "Created At"
                ]
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info(
                "No consultation requests."
            )