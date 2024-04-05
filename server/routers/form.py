from server.schemas.form import FormCreate, FormResponse
from fastapi import APIRouter, Depends, Body, Path, HTTPException, Query, status
from typing import Annotated
from server.managers.form import Form

form_router = APIRouter(prefix='/api/forms')


@form_router.post('', status_code=201)
def create_form(form: Annotated[FormCreate, Body()]) -> str:
    form_db = Form()
    form_db.fill_form(form.dict())
    form_db.add()
    return 'OK'


# def create_form(data: dict, user: dict = None):
#     return 'OK'


# @form_router.get('', status_code=200, response_model=list[FormCreate])
@form_router.get('', status_code=200)
def get_all_forms():
    forms_db = Form.get_all()
    return forms_db


@form_router.get('/{form_id}', status_code=200, response_model=FormResponse)
def get_form(form_id: Annotated[str, Path()]):
    form_db = Form.get(id=form_id)
    if not form_db:
        raise HTTPException(status_code=404, detail='Form this id not found')
    return form_db
