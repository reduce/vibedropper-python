# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .page import Page
from .._models import BaseModel

__all__ = ["PageUpdateResponse"]


class PageUpdateResponse(BaseModel):
    page: Optional[Page] = None
