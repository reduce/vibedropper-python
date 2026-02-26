# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Campaign"]


class Campaign(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    list_ids: Optional[List[str]] = FieldInfo(alias="listIds", default=None)

    name: Optional[str] = None

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)

    sent_at: Optional[datetime] = FieldInfo(alias="sentAt", default=None)

    status: Optional[Literal["DRAFT", "SCHEDULED", "SENDING", "SENT"]] = None

    subject: Optional[str] = None
