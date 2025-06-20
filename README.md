# Example of CQRS pattern

The CQRS pattern separates read (Query ) and write (Command ) operations into different components. This allows you to optimize each side according to your needs:

Commands : Handle write operations (create, update, delete).
Queries : Handle read operations (get data).
This pattern is useful in systems where read and write operations have very different requirements, such as high concurrency applications or complex systems.

This program implements the CQRS pattern to separate read and write operations.

## Structure
- Commands**: Contains the write logic (`add_user_command.py`).
- Queries**: Contains the read logic (`get_users_query.py`).
- **Models**: Represents the data and business logic (`user_model.py`).

## Execution
1. Install Python 3.x.
Navigate to the project directory.
3. Execute the command:
 ````bash
 python main.py