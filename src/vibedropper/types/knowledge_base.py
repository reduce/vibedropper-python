# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["KnowledgeBase", "_Count"]


class _Count(BaseModel):
    articles: Optional[int] = None

    categories: Optional[int] = None


class KnowledgeBase(BaseModel):
    id: Optional[str] = None

    api_count: Optional[_Count] = FieldInfo(alias="_count", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    name: Optional[str] = None

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)

    slug: Optional[str] = None

    sort_order: Optional[int] = FieldInfo(alias="sortOrder", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
