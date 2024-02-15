"""types for conversation responses"""
from pydantic import BaseModel, UUID4, Field


class CreatedResponse(BaseModel):
    """type for CreatedResponse"""
    id: UUID4 = Field(...)


class UpdatedResponse(BaseModel):
    """type for UpdatedResponse"""
    class Config:
        schema_extra = {
            "description": "Successfully updated specified resource"
        }


class DeletedResponse(BaseModel):
    """type for DeletedResponse"""
    class Config:
        schema_extra = {
            "description": "Successfully deleted specified resource(s)"
        }
