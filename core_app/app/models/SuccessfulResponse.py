from pydantic import BaseModel, Field

class SuccessFulResponse(BaseModel):
    status_code: int = Field(ge=200, le=299)
    response_message: str