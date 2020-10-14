from lhs.redis.connection import conn
from lhs.modules.users.schemas.user import User

def get_validate_permissions(ses_id,activity):
    user_session = conn.hgetall(ses_id)
    if user_session[b'valid'] == b'True':
        user = User.objects.get(pk=user_session[b'userid'].decode('utf-8'))
        if user:
            if user.permission == activity:
                return user
            else:
                return False
        else:
            return False
    else:
        return False
