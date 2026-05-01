# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Form", "_Count"]


class _Count(BaseModel):
    form_submissions: Optional[int] = FieldInfo(alias="formSubmissions", default=None)


class Form(BaseModel):
    id: Optional[str] = None

    api_count: Optional[_Count] = FieldInfo(alias="_count", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    list_id: Optional[str] = FieldInfo(alias="listId", default=None)

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)

    slug: Optional[str] = None

    status: Optional[Literal["DRAFT", "ACTIVE", "ARCHIVED"]] = None

    success_message: Optional[str] = FieldInfo(alias="successMessage", default=None)

    title: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
