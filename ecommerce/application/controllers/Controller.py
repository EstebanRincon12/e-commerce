from flask import Flask, request, jsonify
from ecommerce.application.services.ServiceUser import UserService
from ecommerce.application.services.SessionService import SessionService
from ecommerce.domain.repositories.UserRepository import UserRepository
from ecommerce.infraestruture.adapters.postgres_repository import PostgresUserRepository

app = Flask(__name__)
db = PostgresUserRepository()
service =  UserService(db)
sessionService = SessionService()



@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    login = data['login']
    rol_name =  data['rol_name']
    id_person = data['id_person']
    password = data['password']

    try:
        user = service.create_user(login, rol_name, id_person, password)
        return jsonify(user.serialize()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    login = data['login']
    password = data['password']
    
    try:
        response = db.authenticate_user(login, password)
        response = sessionService.generate_token(response)
        return jsonify(response), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug= True, port=5000)

