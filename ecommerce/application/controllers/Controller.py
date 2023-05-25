from flask import Flask, request
from ecommerce.infraestruture.adapters.postgres_repository import PostgresUserRepository
from ecommerce.application.services.ServiceUser import UserService

app = Flask(__name__)
user_repository = PostgresUserRepository()
user_service = UserService(user_repository)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    login = data["login"]
    rol_name = data["rol_name"]
    id_person = data["id_person"]
    password = data["password"]

    created_user = user_service.create_user(login, rol_name, id_person, password)

    if created_user:
        return {"message": "User created successfully"}, 201
    else:
        return {"message": "Failed to create user"}, 500

if __name__ == "__main__":
    app.run()
