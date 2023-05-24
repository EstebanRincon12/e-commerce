import os
import sys

# Obtener la ruta del directorio principal del proyecto
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Agregar la ruta del directorio principal al sistema de rutas de Python
sys.path.append(project_dir)

from ecommerce.infraestruture.adapters.postgres_repository import PostgresUserRepository
from ecommerce.domain.models.User  import User

connection_string = "dbname=e-commerce user=postgres password=a123 host=localhost port=5432"

# Crear una instancia del adaptador de base de datos
repository = PostgresUserRepository(connection_string)


# Crear una instancia del usuario
user = User(login='cata', rol_name='admin', id_person=1007381664, password='a123')

# Llamar al método create_user del adaptador de base de datos
repository.create_user(user)