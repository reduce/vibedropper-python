# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .subscriber import Subscriber

__all__ = ["SubscriberAddResponse"]


class SubscriberAddResponse(BaseModel):
    subscriber: Optional[Subscriber] = None
