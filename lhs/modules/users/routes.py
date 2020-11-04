from flask import Blueprint, request, render_template, jsonify, abort, url_for
from flask_restx import Api, Resource, fields
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
from lhs import jwt
from lhs.modules.utils.emailvalidate import email_validate
from lhs.modules.users.functions.register import user_register
from lhs.modules.users.functions.login import get_login
from lhs.modules.utils.getvalidate import get_validate_permissions
from lhs.modules.users.functions.get_my_cards import get_my_cards
import os

users = Blueprint('users',__name__)

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

api = Api(users,version='1.0', title='LHS API version 1.0.10',
     description='Module : User',authorizations=authorizations, security='apikey')


parser = api.parser()
parser.add_argument('Authorization',type=str,location='headers',help='Bearer Access Token',required=True)

@api.route("/register")
class Register(Resource):
    register_fields = api.model('Register',{
        'firstname':fields.String,
        'lastname':fields.String,
        'email':fields.String,
        'password':fields.String
        })
    @api.expect(register_fields)
    def post(self):
        try:
            req = request.json
            email_validate(req.get('email'))
            res = user_register(req)
            return res
        except Exception as err:
            return {"statusCode":400,"message":str(err)},400


@api.route("/login")
class Login(Resource):
    login_fields = api.model('Login',{
        'email' : fields.String,
        'password':fields.String
        })
    @api.expect(login_fields)
    def post(self):
        try:
            req = request.json
            res = get_login(req)
            return res

        except Exception as err:
            return {"statusCode":400,"message":str(err)},400

@api.route("/get/cards")
class GetMyCards(Resource):
    @jwt_required
    def get(self):
        try:
            current_user = get_jwt_identity()
            user_data = get_validate_permissions(current_user,["USER"])
            if user_data:
                result = get_my_cards(user_data)
                return result
            else:
                return {"statusCode":401, "message":"you are not authorized to use this route"},401
        except Exception as err:
            return {"statusCode":400, "message":str(err)},400
