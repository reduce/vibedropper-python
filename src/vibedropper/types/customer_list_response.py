# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .customer import Customer

__all__ = ["CustomerListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: Optional[int] = None

    page: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)


class CustomerListResponse(BaseModel):
    customers: Optional[List[Customer]] = None

    pagination: Optional[Pagination] = None
