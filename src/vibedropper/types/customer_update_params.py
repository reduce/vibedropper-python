# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerUpdateParams"]


class CustomerUpdateParams(TypedDict, total=False):
    name: str

    pickup_location_id: Annotated[Optional[str], PropertyInfo(alias="pickupLocationId")]

    region_id: Annotated[Optional[str], PropertyInfo(alias="regionId")]
