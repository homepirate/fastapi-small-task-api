from uuid import UUID

from pydantic import BaseModel, field_validator


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STask(STaskAdd):
    id: UUID

    # @field_validator("id")  # кастит UUID к str
    # def validate_uuids(cls, value):
    #     if value:
    #         return str(value)
    #     return value


class STaskId(BaseModel):
    ok: bool = True
    task_id: UUID
