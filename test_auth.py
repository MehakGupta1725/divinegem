from database import (
    create_tables,
    initialize_admin,
    authenticate_user
)

create_tables()

initialize_admin()

print(
    authenticate_user(
        "admin",
        "admin123"
    )
)