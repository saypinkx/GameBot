
from fastapi import APIRouter, Depends, Body, Path, HTTPException, Query, status
from typing import Annotated
from server.managers.user import User

user_router = APIRouter(prefix='/api/users')


@user_router.get('/{chat_id}', status_code=200)
def get_user(chat_id: Annotated[int, Path()]):
    user = User.get(chat_id)
    if not user:
        raise HTTPException(status_code=404, detail='User with chat_id not found')
    return user


@user_router.post('', status_code=201)
def create_user(chat_id: Annotated[int, Body()], parameters: Annotated[dict, Body()]):
    try:
        user = User(chat_id=chat_id, parameters=parameters)
        user.add()
    except:
        raise HTTPException(status_code=400, detail='User with chat_id already registered')
    else:
        return 'OK'


@user_router.put('/{chat_id}', status_code=200)
def update_user(chat_id: Annotated[int, Path()], parameters: Annotated[dict, Body()]):
    user = User.get(chat_id=chat_id)
    if not user:
        raise HTTPException(status_code=404, detail='User with chat_id not found')
    user.update(parameters=parameters)
    return 'OK'


@user_router.delete('/{chat_id}', status_code=200)
def delete_user(chat_id: Annotated[int, Path()]):
    user = User.get(chat_id=chat_id)
    if not user:
        raise HTTPException(status_code=404, detail='User with chat_id not found')
    user.delete()
    return 'OK'
