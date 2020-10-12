from validate_email import validate_email


def email_validate(email):
    if not validate_email(email):
        raise Exception("Email is not in proper format")
