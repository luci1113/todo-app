from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from flask_login import LoginManager, current_user
from models import db_session
from schema import schema
from auth import keycloak_openid
from pro_features import ProFeatures

app = Flask(__name__)
app.debug = True

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class AuthenticatedGraphQLView(GraphQLView):
    def parse_body(self, request):
        if 'application/graphql' in (request.content_type, request.mimetype):
            return {'query': request.data.decode()}
        return super(AuthenticatedGraphQLView, self).parse_body(request)

    def dispatch_request(self):
        if current_user.is_authenticated:
            return super(AuthenticatedGraphQLView, self).dispatch_request()
        else:
            return jsonify({'message': 'Please log in.'}), 401

app.add_url_rule(
    '/graphql',
    view_func=AuthenticatedGraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
        context={'session': db_session}
    )
)

@app.route('/pro', methods=['POST'])
def pro():
    if current_user.is_authenticated:
        return ProFeatures.upgrade_to_pro(current_user)
    else:
        return jsonify({'message': 'Please log in.'}), 401

if __name__ == '__main__':
    app.run()

