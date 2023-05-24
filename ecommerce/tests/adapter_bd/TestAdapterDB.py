from ecommerce.domain.models.User  import User
from ecommerce.infraestruture.adapters.repositories.postgres_repository import PostgresUserRepository

connection_string = "dbname=e-commerce user=postgres password=a123 host=localhost port=5432"

# Crear una instancia del adaptador de base de datos
repository = PostgresUserRepository(connection_string)


# Crear una instancia del usuario
user = User(login='lola', rol_name='user', id_person=2, password='password')

# Llamar al método create_user del adaptador de base de datos
repository.create_user(user)