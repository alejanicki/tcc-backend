from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from dao import trade_dao
from utils import jwt_utils

from models.trade_models import Trade

router = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_trade(trade: Trade, token: dict = Depends(jwt_utils.verify_token)):
    trade.id_user = token['sub']
    await trade_dao.create_new_trade(trade)
    return JSONResponse(content={'message': f'Trade created successfully'})

@router.get('/read', status_code=status.HTTP_200_OK)
async def read_all_trades():

    query_battery = await trade_dao.select_all_trades()

    data = {'battery': query_battery}
    return JSONResponse(content=data)

@router.get('/read-id', status_code=status.HTTP_302_FOUND)
async def read_trade_by_id(id_trade: int):

    query_trade = await trade_dao.select_trade_by_id(id_trade)

    if not query_trade:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'id not found')

    data = {'trade': query_trade}
    return JSONResponse(content=data)

@router.post('/update', status_code=status.HTTP_200_OK)
async def update_trade(trade_id: int, trade: Trade):

    result = await trade_dao.update_trade(
        id_trade=trade_id,
        trade=trade
    )

    if result:
        return JSONResponse(content={'message': f'Trade updated successfully'})

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Cannot update, there are data errors')

@router.post('/delete-id', status_code=status.HTTP_200_OK)
async def delete_trade_by_id(trade_id: int):

    check_trade_exists = await trade_dao.select_trade_by_id(trade_id)

    if check_trade_exists:
        await trade_dao.delete_trade_by_id(trade_id)
        return JSONResponse(content={'message': 'trade deleted successfully'})

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Cannot found Trade')