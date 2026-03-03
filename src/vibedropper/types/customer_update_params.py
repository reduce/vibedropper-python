# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerUpdateParams"]


class CustomerUpdateParams(TypedDict, total=False):
    address_line1: Annotated[Optional[str], PropertyInfo(alias="addressLine1")]

    address_line2: Annotated[Optional[str], PropertyInfo(alias="addressLine2")]

    city: Optional[str]

    country: Optional[str]

    first_name: Annotated[Optional[str], PropertyInfo(alias="firstName")]

    last_name: Annotated[Optional[str], PropertyInfo(alias="lastName")]

    name: str

    pickup_location_id: Annotated[Optional[str], PropertyInfo(alias="pickupLocationId")]

    postal_code: Annotated[Optional[str], PropertyInfo(alias="postalCode")]

    region_id: Annotated[Optional[str], PropertyInfo(alias="regionId")]

    state: Optional[str]
