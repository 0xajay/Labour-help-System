from flask import Blueprint, request, render_template, jsonify, abort, url_for
from flask_restx import Api, Resource, fields
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
from lhs import jwt
from lhs.modules.utils.getvalidate import get_validate_permissions
from lhs.modules.payments.functions.add_new_card import add_new_card
from lhs.modules.payments.functions.get_user_cards import get_user_cards
import os

payments = Blueprint('payments',__name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}
if os.environ.get('HTTPS'):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        return url_for(self.endpoint('specs'), _external=True, _scheme='https')

    Api.specs_url = specs_url

api = Api(payments,version='1.0', title='LHS API version 1.0.10',
     description='Module : Payment',authorizations=authorizations, security='apikey')


parser = api.parser()
parser.add_argument('Authorization',type=str,location='headers',help='Bearer Access Token',required=True)

@api.route("/add/card")
class AddUserCard(Resource):
    card_fields = api.model('AddUserCard',{
            "name":fields.String,
            "card_number":fields.String,
            "expiry_date":fields.String,
            "cvv":fields.String,
        })
    @api.expect(card_fields)
    @jwt_required
    def post(self):
        try:
            req = request.json
            current_user = get_jwt_identity()
            user_data = get_validate_permissions(current_user,["USER"])
            if user_data:
                result = add_new_card(req, user_data)
                return result
            else:
                return {"statusCode":401, "message":"you are not authorized to use this route"},401
        except Exception as err:
            return {"statusCode":400,"message":str(err)},400

@api.route("/cards")
class GetUserCards(Resource):
    @jwt_required
    def get(self):
        try:
            current_user = get_jwt_identity()
            user_data = get_validate_permissions(current_user,["USER"])
            if user_data:
                result = get_user_cards(user_data)
                return result
            else:
                return {"statusCode":401, "message":"you are not authorized to use this route"},401
        except Exception as err:
            return {"statusCode":400, "message":str(err)},400
