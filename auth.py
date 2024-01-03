
from keycloak import KeycloakOpenID
from flask import current_app
from models import User, db_session

class KeycloakAuth:
    def __init__(self):
        self.keycloak_openid = KeycloakOpenID(server_url="YOUR_KEYCLOAK_SERVER_URL",
                                              client_id="YOUR_CLIENT_ID",
                                              realm_name="YOUR_REALM_NAME",
                                              client_secret_key="YOUR_CLIENT_SECRET_KEY")

    def authenticate(self, token):
        try:
            self.keycloak_openid.token_info(token)
            return True
        except:
            return False

    def get_keycloak_user(self, token):
        return self.keycloak_openid.userinfo(token)

    def get_or_create_user(self, token):
        keycloak_user = self.get_keycloak_user(token)
        user = User.query.filter_by(keycloak_id=keycloak_user['sub']).first()
        if not user:
            user = User(keycloak_id=keycloak_user['sub'])
            db_session.add(user)
            db_session.commit()
        return user

keycloak_auth = KeycloakAuth()

