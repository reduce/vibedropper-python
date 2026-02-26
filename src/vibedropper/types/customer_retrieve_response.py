# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .customer import Customer

__all__ = ["CustomerRetrieveResponse"]


class CustomerRetrieveResponse(BaseModel):
    customer: Optional[Customer] = None
