# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .form import Form
from .._models import BaseModel
from .pagination import Pagination

__all__ = ["FormListResponse"]


class FormListResponse(BaseModel):
    forms: Optional[List[Form]] = None

    pagination: Optional[Pagination] = None
