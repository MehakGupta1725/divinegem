import streamlit as st
from database import (
    create_tables,
    initialize_admin,
    create_user,
    authenticate_user
)

# Initialize database
create_tables()
initialize_admin()

# Session State Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "role" not in st.session_state:
    st.session_state.role = ""

# Page Config
st.set_page_config(
    page_title="DivineGem",
    page_icon="💎",
    layout="wide"
)

# ------------------------
# LOGIN / SIGNUP
# ------------------------

if not st.session_state.logged_in:

    st.title("💎 DivineGem")
    st.subheader("Gemstone Consultation Platform")

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    # LOGIN
    with tab1:

        st.header("Login")

        username = st.text_input(
            "Username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button("Login"):

            user = authenticate_user(
                username,
                password
            )

            if user:

                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = user[0]

                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )

    # SIGNUP
    with tab2:

        st.header("Create Account")

        new_username = st.text_input(
            "Choose Username"
        )

        new_password = st.text_input(
            "Choose Password",
            type="password"
        )

        if st.button("Sign Up"):

            if (
                new_username.strip()
                and new_password.strip()
            ):

                success = create_user(
                    new_username,
                    new_password
                )

                if success:

                    st.success(
                        "Account created successfully!"
                    )

                    st.info(
                        "Please login."
                    )

                else:

                    st.error(
                        "Username already exists."
                    )

            else:

                st.error(
                    "Please fill all fields."
                )

# ------------------------
# DASHBOARD ROUTING
# ------------------------

else:

    st.sidebar.success(
        f"Logged in as: "
        f"{st.session_state.username}"
    )

    st.sidebar.write(
        f"Role: {st.session_state.role}"
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""

        st.rerun()

    if st.session_state.role == "user":

        from pages.user_dashboard import (
            show_user_dashboard
        )

        show_user_dashboard(
            st.session_state.username
        )

    elif st.session_state.role == "admin":

        from pages.admin_dashboard import (
            show_admin_dashboard
        )

        show_admin_dashboard()