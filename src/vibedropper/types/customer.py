# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Customer"]


class Customer(BaseModel):
    id: Optional[str] = None

    average_order_value: Optional[float] = FieldInfo(alias="averageOrderValue", default=None)

    email: Optional[str] = None

    last_purchase_date: Optional[datetime] = FieldInfo(alias="lastPurchaseDate", default=None)

    lists: Optional[List[object]] = None

    name: Optional[str] = None

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)

    pickup_location: Optional[object] = FieldInfo(alias="pickupLocation", default=None)

    purchase_count: Optional[int] = FieldInfo(alias="purchaseCount", default=None)

    region: Optional[object] = None

    roles: Optional[List[object]] = None

    total_spent: Optional[float] = FieldInfo(alias="totalSpent", default=None)
