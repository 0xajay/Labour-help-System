from resonance.conn.red import conn
from resonance.modules.users.db.userdb import User

def get_validatewithoutEmailVerified(ses_id,activity):
    user_session = conn.hgetall(ses_id)
    if user_session[b'valid']== b'True':
        user = User.query.filter_by(id=int(user_session[b'userid'])).first()
        if user:
            if set(activity) & set(user.activity):
                return user
            else:
                return False
        else:
            return False
    else:
        return False

def get_validatewithEmailVerified(ses_id,activity):
    user_session = conn.hgetall(ses_id)
    if user_session[b'valid']== b'True':
        user = User.query.filter_by(id=int(user_session[b'userid']),verified=True).first()
        if user:
            if set(activity) & set(user.activity):
                return user
            else:
                return False
        else:
            return False
    else:
        return False
