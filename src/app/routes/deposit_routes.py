import string
from typing import Any, Optional
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from models.deposit_models import Deposit
from dao import deposit_dao, user_dao
from utils import jwt_utils, user_utils
import battery_predict


router = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_deposit(deposit: Deposit):
    await deposit_dao.create_new_deposit(deposit)
    return JSONResponse(content={'message': f'Deposit created successfully'})


@router.get('/read', status_code=status.HTTP_200_OK)
async def read_all_deposits():

    query_deposit: Optional[Any] = await deposit_dao.select_all_deposit()

    if query_deposit is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'An error has occurred. We apologize for any inconvenience and are actively working to resolve the issue.')

    for deposit in query_deposit:
        deposit['date_deposit'] = user_utils.format_date(deposit['date_deposit'])

    return JSONResponse(content=query_deposit)


@router.get('/read-id', status_code=status.HTTP_302_FOUND)
async def read_deposit_by_id(id_deposit: int):

    query_deposit = await deposit_dao.select_deposit_by_id(id_deposit)

    if not query_deposit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'id not found')

    data = {'deposit': query_deposit}
    return JSONResponse(content=data)

@router.post('/update', status_code=status.HTTP_200_OK)
async def update_deposit(id_deposit: int, deposit: Deposit):

    result = await deposit_dao.update_deposit(
        id_deposit=id_deposit,
        deposit=deposit
    )

    if result:
        return JSONResponse(content={'message': f'deposit updated successfully'})

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Cannot update, there are data errors')

@router.post('/delete-id', status_code=status.HTTP_200_OK)
async def delete_deposit_by_id(id_deposit: int):

    check_deposit_exists = await deposit_dao.select_deposit_by_id(id_deposit)

    if check_deposit_exists:
        await deposit_dao.select_deposit_by_id(id_deposit)
        return JSONResponse(content={'message': 'Battery deleted successfully'})

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Cannot found battery')

@router.get('/battery-count', status_code=status.HTTP_200_OK)
async def count_battery(battery_quantity):
    
    batteries_count = battery_predict.count_batteries(int(battery_quantity))
    
    return JSONResponse(content={'count': batteries_count})
      