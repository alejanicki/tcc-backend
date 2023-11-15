from typing import Any, Optional
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from models.user_models import User, UserUpdate
from dao import user_dao
from utils import user_utils, jwt_utils


router = APIRouter()

# criar novo usuario


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(user: User):

    if not user.terms_conditions:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Cannot create user due to authorization of the terms and conditions')

    email_verify = await user_dao.verify_email(user.email)

    if email_verify:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. email: {user.email} alredy exist')

    user.password_user = user_utils.get_pwd_hash(user.password_user)

    await user_dao.create_new_user(user)

    return JSONResponse(content={'message': f'User {user.name_user}, created successfully'})

# ler todos os usuarios


@router.get('/read', status_code=status.HTTP_200_OK)
async def read_all_user():

    query_user: Optional[Any] = await user_dao.select_all_user()

    if query_user is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'An error has occurred. We apologize for any inconvenience and are actively working to resolve the issue.')

    for user in query_user:
        user['date_birth'] = user_utils.format_date(user['date_birth'])

    return JSONResponse(content=query_user)

# ler usuario pelo id


@router.get('/read-id', status_code=status.HTTP_302_FOUND)
async def read_user_by_id(token: dict = Depends(jwt_utils.verify_token)):

    query_user: Optional[Any] = await user_dao.select_user_by_id(token['sub'])

    if query_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'user not found')

    query_user['date_birth'] = user_utils.format_date(query_user['date_birth'])

    return JSONResponse(content=query_user)

# Atualizar usuario


@router.post('/update', status_code=status.HTTP_200_OK)
async def update_user(user: UserUpdate, token: dict = Depends(jwt_utils.verify_token)):

    # Processando dados
    if user.cpf and user.cellphone and user.email is not None:
        await user_utils.user_data_processing(user.cpf, user.cellphone, user.email)

    # atualizando usuário
    result = await user_dao.update_user(
        id_user=token['sub'],
        user=user
    )

    if result:
        return JSONResponse(content={'message': f'User {user.name_user}, updated successfully'})

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Cannot update, there are data errors')


# Deletando usuario
@router.post('/delete-id', status_code=status.HTTP_200_OK)
async def delete_user_by_id(token: dict = Depends(jwt_utils.verify_token)):

    check_user_exists = await user_dao.select_user_by_id(token['sub'])

    if check_user_exists:
        await user_dao.delete_user_by_id(token['sub'])
        return JSONResponse(content={'message': 'User deleted successfully'})

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Cannot found user')
