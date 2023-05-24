from application.services.ServiceUser import AuthenticationService
from application.services.ServiceUser import UserCreationService
from ecommerce.domain.repositories.UserRepository import UserRepository

# ...

authentication_service = AuthenticationService(user_repository)
user_creation_service = UserCreationService(UserRepository)

@app.route('/login', methods=['POST'])
def login():
    # Obtener los datos de la solicitud
    username = request.form['username']
    password = request.form['password']
    
    # Llamar al caso de uso correspondiente
    user = authentication_service.authenticate(username, password)
    
    # ...
    
@app.route('/register', methods=['POST'])
def register():
    # Obtener los datos de la solicitud
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']
    description = request.form['description']
    
    # Llamar al caso de uso correspondiente
    user = user_creation_service.create_user(username, password, role, description)
    
    # ...
