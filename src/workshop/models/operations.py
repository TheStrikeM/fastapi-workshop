from datetime import date
from typing import Optional
from enum import Enum
from decimal import Decimal

from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = "income"
    OUTCOME = "outcome"


class OperationBase(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
    desc: Optional[str]


class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True

class OperationCreate(OperationBase):
    pass