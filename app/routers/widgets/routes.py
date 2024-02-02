from fastapi import APIRouter, Depends, HTTPException
from dependencies.dependencies import get_db
from sqlalchemy.orm import Session
from .types import CreateWidget, CreateWidgetResponse, DeleteWidgetResponse, WidgetResponse, WidgetListResponse
import controllers

router = APIRouter(
    prefix="/widgets",
    tags=["Widgets"],
    # dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/all", response_model=WidgetListResponse)
async def get_all_widgets(db: Session = Depends(get_db)):
    """
    This will return a list of all widgets in the database.

    """
    widget_list = controllers.widgets.read_all(db)
    return WidgetListResponse(widget_list)


@router.get("/{record_id}", response_model=WidgetResponse)
def get_individual_widget(record_id: int, db: Session = Depends(get_db)):
    """
    Will return an individual widget record by id.
    """
    widget = controllers.widgets.read(db, record_id)
    if widget == None:
        raise HTTPException(status_code=404, detail="Item not found")

    return WidgetResponse(**widget)


@router.post("/", response_model=CreateWidgetResponse)
async def create_a_new_widget(widget_data: CreateWidget,  db: Session = Depends(get_db)):
    """
    This endpoint can be used to create a new widget.

    """
    payload = widget_data.dict()

    created_widget = controllers.widgets.create(db, payload)
    return CreateWidgetResponse(**created_widget)


@router.delete("/{record_id}", response_model=DeleteWidgetResponse)
async def delete_widget(record_id: int, db: Session = Depends(get_db)):
    """
    This endpoint allows you to delete a widget record by id.
    """
    deleted_response = controllers.widgets.delete(db, record_id)
    return DeleteWidgetResponse(**deleted_response)


@router.put("/{record_id}", response_model=WidgetResponse)
async def update_widget(widget_data: CreateWidget, record_id: int,  db: Session = Depends(get_db)):
    """
    This endpoint is meant to update a widget given a record id.

    """
    updated_widget = controllers.widgets.update(
        db, widget_data.dict(), record_id)
    if updated_widget == None:
        raise HTTPException(status_code=404, detail="Item not found")

    return WidgetResponse(**updated_widget)
