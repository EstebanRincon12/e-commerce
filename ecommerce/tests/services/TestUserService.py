from ecommerce.application.services.ServiceUser import UserService
from ecommerce.infraestruture.adapters.postgres_repository import PostgresUserRepository

# Crear una instancia de UserRepository
user_repository = PostgresUserRepository()

# Crear una instancia de UserService con el UserRepository
user_service = UserService(user_repository)

# Datos del usuario a crear
login = "ejemplo"
rol_name = "admin"
id_person = 12345
password = "secreto"

# Crear el usuario
user = user_service.create_user(login, rol_name, id_person, password)

# Verificar si el usuario se creó correctamente
if user:
    print("Usuario creado exitosamente:")
    print("Login:", user.login)
    print("Rol:", user.rol_name)
    print("ID de persona:", user.id_person)
    print("Contraseña:", user.password)
else:
    print("No se pudo crear el usuario")
