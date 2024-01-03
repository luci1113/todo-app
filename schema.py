
from ariadne import ObjectType, QueryType, MutationType, make_executable_schema
from ariadne.asgi import GraphQL
from models import User, Todo, db_session
from auth import keycloak_auth

type_defs = """
    type Query {
        users: [User]
        todos: [Todo]
    }

    type Mutation {
        createTodo(title: String!, description: String!, time: String, image: String): Todo
    }

    type User {
        id: ID!
        keycloak_id: String!
        pro: Boolean!
        todos: [Todo]
    }

    type Todo {
        id: ID!
        title: String!
        description: String!
        time: String!
        user_id: ID!
        image: String
    }
"""

query = QueryType()
mutation = MutationType()

@query.field("users")
def resolve_users(*_):
    return db_session.query(User).all()

@query.field("todos")
def resolve_todos(*_):
    return db_session.query(Todo).all()

@mutation.field("createTodo")
def resolve_create_todo(_, info, title, description, time=None, image=None):
    token = info.context["request"].headers.get("Authorization")
    if not keycloak_auth.authenticate(token):
        raise Exception("Authentication failed")

    user = keycloak_auth.get_or_create_user(token)
    todo = Todo(title=title, description=description, time=time, user_id=user.id)

    if user.pro and image:
        todo.image = image

    db_session.add(todo)
    db_session.commit()

    return todo

schema = make_executable_schema(type_defs, query, mutation)
app = GraphQL(schema)

