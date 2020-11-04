import stripe
import os

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


def create_stripe_customer(email):
    try:
        customer = stripe.Customer.create(
                    description="My First Test Customer (created for API docs)",
                    email = email
                    )
        setup_intent = stripe.SetupIntent.create(
                payment_method_types=["card"],
                )
        return customer["id"],setup_intent["client_secret"]
    except Exception as err:
        return str(err)
