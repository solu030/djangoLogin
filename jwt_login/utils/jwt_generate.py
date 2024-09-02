import jwt
import datetime
from djangoLogin.settings import SECRET_KEY
def generate_jwt_token(payload, exp=1):
    salt = SECRET_KEY
    header = {
        'typ': 'JWT',
        'alg': 'HS256',
    }
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=exp)
    token = jwt.encode(payload, salt,headers=header).decode('utf-8')