import stripe
import os

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

def get_my_cards(user_data):
    print(user_data)
    result = stripe.PaymentMethod.list(
                customer=user_data['stripe_customer_id'],
                type="card",
                )
    return {"data":result}
