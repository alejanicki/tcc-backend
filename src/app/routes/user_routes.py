from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from models.user_models import User
from dao import user_dao
from utils import user_utils


router = APIRouter()


@router.post('/create-user', status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    # Processando dados do novo usuário
    user.cpf, user.cellphone, user.email = await user_utils.user_data_processing(user.cpf, user.cellphone, user.email)
    cpf_verify, email_verify = await user_dao.verify_data_overwrite(user.cpf, user.email)
    ddi_verify = user_utils.consult_ddi(user.cellphone)

    # Verificando Erros
    if not ddi_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'cannot create user. ddi {user.cellphone} is invalid')
    if cpf_verify:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. CPF {user.cpf} alredy exist')
    if email_verify:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. email: {user.email} alredy exist')
    if not user.terms_conds:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Cannot create user due to authorization of the terms')

     # Criando linha na tabela users
    await user_dao.create_new_user(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password_user=user_utils.get_pwd_hash(user.password_user),
        terms_conds=user.terms_conds,
        share_data=user.share_data
    )

    return JSONResponse(content={'message': f'User {user.first_name}, created successfully'})
