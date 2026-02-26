# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["List", "_Count"]


class _Count(BaseModel):
    subscribers: Optional[int] = None


class List(BaseModel):
    id: Optional[str] = None

    api_count: Optional[_Count] = FieldInfo(alias="_count", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    name: Optional[str] = None

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
