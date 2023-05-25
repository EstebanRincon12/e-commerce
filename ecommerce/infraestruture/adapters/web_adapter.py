from flask import Flask, request, jsonify
from ecommerce.application.services.ServiceUser import UserService

app = Flask(__name__)
user_service = UserService()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    login = data['login']
    rol_name = data['rol_name']
    id_person = data['id_person']
    password = data['password']

    try:
        user = user_service.create_user(login, rol_name, id_person, password)
        return jsonify(user.serialize()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()
