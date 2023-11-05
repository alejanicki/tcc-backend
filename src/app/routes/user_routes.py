from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from models.user_models import User, UserUpdate
from dao import user_dao
from utils import user_utils


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

    query_user = await user_dao.select_all_user()

    data = {'user': query_user}
    return JSONResponse(content=data)

# ler usuario pelo id


@router.get('/read-id', status_code=status.HTTP_302_FOUND)
async def read_user_by_id(user_id: int):

    query_user = await user_dao.select_user_by_id(user_id)

    if not query_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'id not found')

    data = {'user': query_user}
    return JSONResponse(content=data)

# Atualizar usuario


@router.post('/update', status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: UserUpdate):

    # Processando dados
    if user.cpf and user.cellphone and user.email is not None:
        await user_utils.user_data_processing(user.cpf, user.cellphone, user.email)

    # atualizando usuário
    result = await user_dao.update_user(
        id_user=user_id,
        user=user
    )

    if result:
        return JSONResponse(content={'message': f'User {user.name_user}, updated successfully'})

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Cannot update, there are data errors')


# Deletando usuario
@router.post('/delete-id', status_code=status.HTTP_200_OK)
async def delete_user_by_id(user_id: int):

    check_user_exists = await user_dao.select_user_by_id(user_id)

    if check_user_exists:
        await user_dao.delete_user_by_id(user_id)
        return JSONResponse(content={'message': 'User deleted successfully'})

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Cannot found user')
