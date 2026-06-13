import streamlit as st
import pandas as pd

from database import (
    get_users,
    get_recommendations,
    get_consultations
)


def show_admin_dashboard():

    st.title("📊 DivineGem Admin Portal")

    st.write(
        "Monitor users, recommendations, consultations, "
        "and overall platform performance."
    )

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Analytics",
        "👥 Users",
        "💎 Recommendations",
        "📞 Consultations"
    ])

    # ==========================
    # Analytics Tab
    # ==========================
    with tab1:

        st.header("📈 Platform Analytics")

        users = get_users()
        recommendations = get_recommendations()
        consultations = get_consultations()

        rec_df = None

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

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "👥 Users",
                len(users)
            )

        with col2:

            st.metric(
                "💎 Recommendations",
                len(recommendations)
            )

        with col3:

            st.metric(
                "📞 Consultations",
                len(consultations)
            )

        with col4:

            if rec_df is not None:

                common_gem = (
                    rec_df["Gemstone"]
                    .mode()[0]
                )

                st.metric(
                    "🏆 Top Gem",
                    common_gem
                )

            else:

                st.metric(
                    "🏆 Top Gem",
                    "N/A"
                )

        if rec_df is not None:

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.subheader(
                    "💎 Gemstone Trends"
                )

                st.bar_chart(
                    rec_df["Gemstone"]
                    .value_counts()
                )

            with col2:

                st.subheader(
                    "🎯 User Concerns"
                )

                st.bar_chart(
                    rec_df["Concern"]
                    .value_counts()
                )

    # ==========================
    # Users Tab
    # ==========================
    with tab2:

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
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No users found."
            )

    # ==========================
    # Recommendations Tab
    # ==========================
    with tab3:

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
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No recommendations found."
            )

    # ==========================
    # Consultations Tab
    # ==========================
    with tab4:

        st.header(
            "📞 Consultation Requests"
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
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No consultation requests."
            )