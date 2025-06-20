from models.user_model import UserModel
from commands.add_user_command import AddUserCommand
from queries.get_users_query import GetUsersQuery

def main():
    # Inicializar el modelo
    model = UserModel()

    # Crear instancias de los comandos y consultas
    add_user_command = AddUserCommand(model)
    get_users_query = GetUsersQuery(model)

    # Ejecutar comandos
    add_user_command.execute("Alice")
    add_user_command.execute("Bob")

    # Ejecutar consulta
    users = get_users_query.execute()

    # Mostrar resultados
    print("Usuarios registrados:")
    for user in users:
        print(f"- {user}")

if __name__ == "__main__":
    main()