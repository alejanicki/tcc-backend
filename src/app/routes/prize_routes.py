from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from dao import prize_dao

from models.prize_models import Prize

router = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_prize(prize: Prize):
    await prize_dao.create_new_prize(prize)
    return JSONResponse(content={'message': f'Prize created successfully'})

@router.get('/read', status_code=status.HTTP_200_OK)
async def read_all_prizes():

    query_battery = await prize_dao.select_all_prizes()

    data = {'battery': query_battery}
    return JSONResponse(content=data)

@router.get('/read-id', status_code=status.HTTP_302_FOUND)
async def read_prize_by_id(id_prize: int):

    query_prize = await prize_dao.select_prize_by_id(id_prize)

    if not query_prize:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'id not found')

    data = {'prize': query_prize}
    return JSONResponse(content=data)

@router.post('/update', status_code=status.HTTP_200_OK)
async def update_prize(prize_id: int, prize: Prize):

    result = await prize_dao.update_prize(
        id_prize=prize_id,
        prize=prize
    )

    if result:
        return JSONResponse(content={'message': f'Prize updated successfully'})

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Cannot update, there are data errors')

@router.post('/delete-id', status_code=status.HTTP_200_OK)
async def delete_prize_by_id(prize_id: int):

    check_prize_exists = await prize_dao.select_prize_by_id(prize_id)

    if check_prize_exists:
        await prize_dao.delete_prize_by_id(prize_id)
        return JSONResponse(content={'message': 'Prize deleted successfully'})

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Cannot found prize')