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

import razorpay

client = razorpay.Client(auth=("rzp_test_crBwqIL2Ugwr91", "Ll5g9dMDf3LmrVIlWgC4vif7"))

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
     description='Module : Payments',authorizations=authorizations, security='apikey')


parser = api.parser()
parser.add_argument('Authorization',type=str,location='headers',help='Bearer Access Token',required=True)

@api.route("/order/<amount>")
class PaymentOrder(Resource):
    def get(self, amount):
        try:
            data = {
            "amount":amount,
            "currency":'AED'
            }
            order = client.order.create(data=data)
            print(order)
            return render_template("checkout.html", order_id=order["id"])
        except Exception as err:
            return {"statusCode":400,"message":str(err)},400
