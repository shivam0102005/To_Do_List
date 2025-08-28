from app import create_app, db
# from app.models import User

# app = create_app()

# with app.app_context():
#     # Ensure tables exist
#     db.create_all()

#     # Check if admin user already exists
#     existing_user = User.query.filter_by(username="admin").first()
#     if existing_user:
#         print("User 'admin' already exists!")
#     else:
#         # Create default admin user
#         user = User(username="admin", password="1234")
#         db.session.add(user)
#         db.session.commit()
#         print("User created successfully: admin / 1234")
