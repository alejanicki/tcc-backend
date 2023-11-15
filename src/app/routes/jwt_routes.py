from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import  OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Union
from dao import user_dao
from utils import user_utils, jwt_utils


router = APIRouter()

# criar novo usuario



@router.post('/login', status_code=status.HTTP_201_CREATED)
def login(user: OAuth2PasswordRequestForm = Depends()) -> JSONResponse:

    verify_user = user_dao.verify_user_exists(user.username)

    if verify_user is not None:
        if isinstance(verify_user, dict):
            if user_utils.check_pwd_hash(password_hash=verify_user.get("password_user"), password=user.password):
                token = jwt_utils.generate_token(id_user=verify_user['id_user'], email=user.username)
                return JSONResponse(status_code=status.HTTP_200_OK, content=token)
            else: 
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong password")
        else:
            # Handle other types if necessary
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unexpected user data type")
    
    else: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    


