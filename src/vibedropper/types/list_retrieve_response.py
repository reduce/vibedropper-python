# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .list import List
from .._models import BaseModel

__all__ = ["ListRetrieveResponse"]


class ListRetrieveResponse(BaseModel):
    list: Optional[List] = None
