from pydantic import BaseModel


class VersionResponse(BaseModel):
    version: float

    class Config:
        from_attributes = True
