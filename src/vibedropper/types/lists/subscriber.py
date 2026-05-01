# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..customer import Customer

__all__ = ["Subscriber"]


class Subscriber(BaseModel):
    id: Optional[str] = None

    customer: Optional[Customer] = None

    custom_fields: Optional[object] = FieldInfo(alias="customFields", default=None)

    email: Optional[str] = None

    list_id: Optional[str] = FieldInfo(alias="listId", default=None)

    name: Optional[str] = None

    status: Optional[Literal["SUBSCRIBED", "UNSUBSCRIBED", "PENDING", "BOUNCED"]] = None

    subscribed_at: Optional[datetime] = FieldInfo(alias="subscribedAt", default=None)
