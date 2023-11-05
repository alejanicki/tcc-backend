from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from dao import battery_dao

from models.battery_models import Battery

router = APIRouter()


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_battery(battery: Battery):
    await battery_dao.create_new_battery(battery)
    return JSONResponse(content={'message': f'Battery created successfully'})


@router.get('/read', status_code=status.HTTP_200_OK)
async def read_all_batteries():

    query_battery = await battery_dao.select_all_batteries()

    data = {'battery': query_battery}
    return JSONResponse(content=data)


@router.get('/read-id', status_code=status.HTTP_302_FOUND)
async def read_battery_by_id(id_battery: int):

    query_battery = await battery_dao.select_battery_by_id(id_battery)

    if not query_battery:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'id not found')

    data = {'battery': query_battery}
    return JSONResponse(content=data)


@router.post('/update', status_code=status.HTTP_200_OK)
async def update_battery(battery_id: int, battery: Battery):

    result = await battery_dao.update_battery(
        id_battery=battery_id,
        battery=battery
    )

    if result:
        return JSONResponse(content={'message': f'battery updated successfully'})

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Cannot update, there are data errors')


@router.post('/delete-id', status_code=status.HTTP_200_OK)
async def delete_battery_by_id(battery_id: int):

    check_battery_exists = await battery_dao.select_battery_by_id(battery_id)

    if check_battery_exists:
        await battery_dao.delete_battery_by_id(battery_id)
        return JSONResponse(content={'message': 'Battery deleted successfully'})

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Cannot found battery')
