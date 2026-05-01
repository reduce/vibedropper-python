# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import typing
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Customer", "List", "Role"]


class List(BaseModel):
    id: typing.Optional[str] = None

    name: typing.Optional[str] = None


class Role(BaseModel):
    id: typing.Optional[str] = None

    color: typing.Optional[str] = None

    description: typing.Optional[str] = None

    name: typing.Optional[str] = None


class Customer(BaseModel):
    id: typing.Optional[str] = None

    address_line1: typing.Optional[str] = FieldInfo(alias="addressLine1", default=None)

    address_line2: typing.Optional[str] = FieldInfo(alias="addressLine2", default=None)

    average_order_value: typing.Optional[float] = FieldInfo(alias="averageOrderValue", default=None)

    city: typing.Optional[str] = None

    country: typing.Optional[str] = None

    created_at: typing.Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    email: typing.Optional[str] = None

    first_name: typing.Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: typing.Optional[str] = FieldInfo(alias="lastName", default=None)

    last_purchase_date: typing.Optional[datetime] = FieldInfo(alias="lastPurchaseDate", default=None)

    lists: typing.Optional[typing.List[List]] = None
    """Lists this customer is subscribed to"""

    name: typing.Optional[str] = None

    org_id: typing.Optional[str] = FieldInfo(alias="orgId", default=None)

    pickup_location: typing.Optional[object] = FieldInfo(alias="pickupLocation", default=None)

    postal_code: typing.Optional[str] = FieldInfo(alias="postalCode", default=None)

    purchase_count: typing.Optional[int] = FieldInfo(alias="purchaseCount", default=None)

    region: typing.Optional[object] = None

    roles: typing.Optional[typing.List[Role]] = None
    """Roles assigned to this customer"""

    state: typing.Optional[str] = None

    total_spent: typing.Optional[float] = FieldInfo(alias="totalSpent", default=None)
    """Total amount spent across all orders"""

    updated_at: typing.Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
