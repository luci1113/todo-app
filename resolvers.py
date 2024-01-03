
from ariadne import ObjectType
from models import User, Todo, db_session
from auth import keycloak_auth

query = ObjectType("Query")
mutation = ObjectType("Mutation")

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

