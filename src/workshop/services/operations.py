from http.client import HTTPException
from typing import List, Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.operations import OperationKind, OperationCreate, OperationUpdate


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, operation_id: int) -> tables.Operation:
        operation = (
            self.session
            .query(tables.Operation)
            .filter_by(id=operation_id)
            .first()
        )
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation

    def get_list(self, kind: Optional[OperationKind] = None) -> List[tables.Operation]:
        query = self.session.query(tables.Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operation = query.all()
        return operation

    def get(self, operation_id: int) -> tables.Operation:
        return self._get(operation_id)

    def create(self, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, operation_id, operation_data: OperationUpdate) -> tables.Operation:
        operation = self._get(operation_id)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, operation_id):
        operation = self._get(operation_id)
        self.session.delete(operation)
        self.session.commit()