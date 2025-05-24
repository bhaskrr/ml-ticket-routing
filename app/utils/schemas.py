from pydantic import BaseModel, Field


class PredictionInputSchema(BaseModel):
    text: str = Field(
        ...,
        min_length=20,
        max_length=1000,
        description="The input text. Must be between 20 and 1000 characters.",
    )


class PredictionOutputSchema(BaseModel):
    category: str
    priority: str
    response_time: float
