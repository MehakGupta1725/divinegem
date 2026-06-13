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
st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-left: 5rem;
    padding-right: 5rem;
}

.stButton > button {
    width: 100%;
    height: 3em;
    border-radius: 12px;
    font-weight: 600;
}

div[data-testid="metric-container"] {
    border: 1px solid #31333F;
    padding: 20px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------
# LOGIN / SIGNUP
# ------------------------

if not st.session_state.logged_in:

    st.markdown(
        """
        <div style='text-align: center;'>

        <h1>💎 DivineGem</h1>

        <h3>
        Personalized Gemstone Guidance
        for Modern Spiritual Wellness
        </h3>

        </div>

        <hr>

        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.success(
            "✨ Personalized Recommendations"
        )

    with col2:

        st.success(
            "🧙 Expert Consultations"
        )

    with col3:

        st.success(
            "📈 Track Your Journey"
        )

    st.divider()

    tab1, tab2 = st.tabs(
        ["🔐 Login", "📝 Sign Up"]
    )

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

        from user_dashboard import (
            show_user_dashboard
        )

        show_user_dashboard(
            st.session_state.username
        )

    elif st.session_state.role == "admin":

        from admin_dashboard import (
            show_admin_dashboard
        )

        show_admin_dashboard()