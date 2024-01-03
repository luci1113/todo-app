
from flask import jsonify
from models import User, db_session

class ProFeatures:
    @staticmethod
    def upgrade_to_pro(user):
        if not user.pro:
            user.pro = True
            db_session.commit()
            return jsonify({'message': 'Successfully upgraded to Pro.'}), 200
        else:
            return jsonify({'message': 'You are already a Pro user.'}), 400

