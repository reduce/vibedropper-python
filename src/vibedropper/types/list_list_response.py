# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List as TypingList, Optional

from .list import List as ListList
from .._models import BaseModel
from .pagination import Pagination

__all__ = ["ListListResponse"]


class ListListResponse(BaseModel):
    lists: Optional[TypingList[ListList]] = None

    pagination: Optional[Pagination] = None
