# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Page", "_Count"]


class _Count(BaseModel):
    items: Optional[int] = None


class Page(BaseModel):
    id: Optional[str] = None

    api_count: Optional[_Count] = FieldInfo(alias="_count", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    name: Optional[str] = None

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)

    slug: Optional[str] = None

    status: Optional[Literal["DRAFT", "ACTIVE", "ENDED", "ARCHIVED"]] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
