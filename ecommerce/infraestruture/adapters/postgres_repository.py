import psycopg2
from ecommerce.domain.models.User import User
from ecommerce.domain.repositories.UserRepository import UserRepository

from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la cadena de conexión de la variable de entorno
connection_string = os.getenv("DB_CONNECTION_STRING")

class PostgresUserRepository(UserRepository):

    def __init__(self):
        self.connection_string = connection_string

    def create_user(self, user: User) -> None:
        try:
            with psycopg2.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                insert_query = """
                    INSERT INTO "Users" (login, rol_name, id_person, password)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(
                    insert_query,
                    (user.login, user.rol_name._role, user.id_person, user.password._hash)
                )
                conn.commit()
        except (psycopg2.Error, Exception) as error:
            print(f"Error creating user: {error}")

    def get_user_by_id(self, user_id: int) -> User:
        try:
            with psycopg2.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                select_query = """
                    SELECT login, rol_name, id_person, password
                    FROM "Users"
                    WHERE id_person = %s
                """
                cursor.execute(select_query, (user_id,))
                row = cursor.fetchone()
                if row:
                    login, rol_name, id_person, password = row
                    return User(login, rol_name, id_person, password)
        except (psycopg2.Error, Exception) as error:
            print(f"Error getting user by id: {error}")

        return None

    def get_user_by_login(self, login: str) -> User:
        try:
            with psycopg2.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                select_query = """
                    SELECT login, rol_name, id_person, password
                    FROM "Users"
                    WHERE login = %s
                """
                cursor.execute(select_query, (login,))
                row = cursor.fetchone()
                if row:
                    login, rol_name, id_person, password = row
                    return User(login, rol_name, id_person, password)
        except (psycopg2.Error, Exception) as error:
            print(f"Error getting user by login: {error}")

        return None

    def update_user(self, user: User) -> None:
        try:
            with psycopg2.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                update_query = """
                    UPDATE "User"
                    SET login = %s, rol_name = %s, password = %s
                    WHERE id_person = %s
                """
                cursor.execute(
                    update_query,
                    (user.login, user.rol_name, user.password, user.id_person)
                )
                conn.commit()
        except (psycopg2.Error, Exception) as error:
            print(f"Error updating user: {error}")

    def delete_user(self, user_id: int) -> None:
        try:
            with psycopg2.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                delete_query = """
                    DELETE FROM "User"
                    WHERE id_person = %s
                """
                cursor.execute(delete_query, (user_id,))
                conn.commit()
        except (psycopg2.Error, Exception) as error:
            print(f"Error deleting user: {error}")

    def authenticate_user(self, login: str, password: str) -> User:
        try:
            with psycopg2.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                select_query = """
                    SELECT login, rol_name, id_person, password
                    FROM "User"
                    WHERE login = %s AND password = %s
                """
                cursor.execute(select_query, (login, password))
                row = cursor.fetchone()
                if row:
                    login, rol_name, id_person, password = row
                    return User(login, rol_name, id_person, password)
        except (psycopg2.Error, Exception) as error:
            print(f"Error authenticating user: {error}")

        return None
