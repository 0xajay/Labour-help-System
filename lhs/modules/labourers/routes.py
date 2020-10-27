from flask import Blueprint, request, render_template, jsonify, abort, url_for
from flask_restx import Api, Resource, fields
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
from lhs import jwt
from lhs.modules.utils.getvalidate import get_validate_permissions
from lhs.modules.labourers.functions.create_labour import create_labour
from lhs.modules.labourers.functions.get_labour_by_id import get_labour_by_id, get_labour_range_by_id
from lhs.modules.labourers.functions.get_labourers import get_labourers
import os

labourers = Blueprint('labourers',__name__)

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

api = Api(labourers,version='1.0', title='LHS API version 1.0.10',
     description='Module : Labour',authorizations=authorizations, security='apikey')


parser = api.parser()
parser.add_argument('Authorization',type=str,location='headers',help='Bearer Access Token',required=True)

@api.route("/labourer")
class Labour(Resource):
    labour_fields = api.model('Lobourer',{
            "name":fields.String,
            "designation":fields.String,
            "email":fields.String,
            "phone":fields.String,
            "country_code":fields.String,
            "code":fields.String
        })
    @api.expect(labour_fields)
    @jwt_required
    def post(self):
        try:
            req = request.json
            current_user = get_jwt_identity()
            user_data = get_validate_permissions(current_user,"MANAGER")
            if user_data:
                result = create_labour(req, user_data)
                return result
            else:
                return {"statusCode":401, "message":"you are not authorized to use this route"},401
        except Exception as err:
            return {"statusCode":400,"message":str(err)},400

@api.route("/list")
class GetAllLabourers(Resource):
    @jwt_required
    def get(self):
        try:
            current_user = get_jwt_identity()
            user_data = get_validate_permissions(current_user,["MANAGER","USER"])
            if user_data:
                result = get_labourers(user_data)
                return result
            else:
                return {"statusCode":401, "message":"you are not authorized to use this route"},401
        except Exception as err:
            return {"statusCode":400,"message":str(err)},400

@api.route("/labour/<labour_id>")
class GetLabourById(Resource):
    @jwt_required
    def get(self, labour_id):
        try:
            current_user = get_jwt_identity()
            user_data = get_validate_permissions(current_user,["MANAGER","USER"])
            if user_data:
                result = get_labour_by_id(labour_id,user_data)
                return result
            else:
                return {"statusCode":401, "message":"you are not authorized to use this route"},401
        except Exception as err:
            return {"statusCode":400,"message":str(err)},400

@api.route("/labour/range/<labour_id>/fromdate/<from_date>/enddate/<end_date>")
class GetLabourById(Resource):
    @jwt_required
    def get(self, labour_id, from_date, end_date):
        try:
            current_user = get_jwt_identity()
            user_data = get_validate_permissions(current_user,["MANAGER","USER"])
            if user_data:
                result = get_labour_range_by_id(labour_id,from_date,end_date,user_data)
                return result
            else:
                return {"statusCode":401, "message":"you are not authorized to use this route"},401
        except Exception as err:
            return {"statusCode":400,"message":str(err)},400
