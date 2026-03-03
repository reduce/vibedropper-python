# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Customer"]


class Customer(BaseModel):
    id: Optional[str] = None

    address_line1: Optional[str] = FieldInfo(alias="addressLine1", default=None)

    address_line2: Optional[str] = FieldInfo(alias="addressLine2", default=None)

    average_order_value: Optional[float] = FieldInfo(alias="averageOrderValue", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    email: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    last_purchase_date: Optional[datetime] = FieldInfo(alias="lastPurchaseDate", default=None)

    lists: Optional[List[object]] = None

    name: Optional[str] = None

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)

    pickup_location: Optional[object] = FieldInfo(alias="pickupLocation", default=None)

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)

    purchase_count: Optional[int] = FieldInfo(alias="purchaseCount", default=None)

    region: Optional[object] = None

    roles: Optional[List[object]] = None

    state: Optional[str] = None

    total_spent: Optional[float] = FieldInfo(alias="totalSpent", default=None)
