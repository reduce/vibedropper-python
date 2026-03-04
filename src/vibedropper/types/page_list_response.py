# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .page import Page
from .._models import BaseModel
from .pagination import Pagination

__all__ = ["PageListResponse"]


class PageListResponse(BaseModel):
    pages: Optional[List[Page]] = None

    pagination: Optional[Pagination] = None
