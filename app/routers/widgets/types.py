from pydantic import BaseModel, RootModel
from typing import List


class CreateWidget(BaseModel):
    name: str
    description: str
    config: dict


class CreateWidgetResponse(BaseModel):
    id: int
    name: str
    description: str
    config: dict


class WidgetResponse(BaseModel):
    id: int
    name: str
    description: str
    config: dict


class DeleteWidgetResponse(BaseModel):
    message: str
    id: int


class WidgetListResponse(RootModel):
    root: List[WidgetResponse]
