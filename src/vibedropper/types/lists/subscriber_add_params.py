# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriberAddParams"]


class SubscriberAddParams(TypedDict, total=False):
    email: Required[str]

    custom_fields: Annotated[object, PropertyInfo(alias="customFields")]

    name: str

    pickup_location_id: Annotated[str, PropertyInfo(alias="pickupLocationId")]

    region_id: Annotated[str, PropertyInfo(alias="regionId")]
