from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
import datetime
from typing import Optional, Dict
from parameters import JWT_SECRET, JWT_ALGORITHM, TIME_EXPIRES

oauth = OAuth2PasswordBearer(tokenUrl="/auth/login")


def generate_token(id_user: str, email: str) -> Optional[Dict[str, str]]:
    payload = {
        'sub': str(id_user),
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=TIME_EXPIRES),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {'access_token': token}


def verify_token(token: str = Depends(oauth)):

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        payload["sub"] = int(payload["sub"])
        return payload

    except jwt.MissingRequiredClaimError:
        raise HTTPException(
            detail={'msg': 'Missing token'}, status_code=status.HTTP_401_UNAUTHORIZED)
    except jwt.ExpiredSignatureError:
        raise HTTPException(detail={
                            'msg': 'Expired token. Login again.'}, status_code=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
        raise HTTPException(detail={
                            'msg': 'Ivalid token. Login again.'}, status_code=status.HTTP_401_UNAUTHORIZED)
