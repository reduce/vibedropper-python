# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .subscriber import Subscriber

__all__ = ["SubscriberListResponse"]


class SubscriberListResponse(BaseModel):
    subscribers: Optional[List[Subscriber]] = None
