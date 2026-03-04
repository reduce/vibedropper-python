# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FormUpdateParams"]


class FormUpdateParams(TypedDict, total=False):
    description: Optional[str]

    list_id: Annotated[Optional[str], PropertyInfo(alias="listId")]
    """List to subscribe form submitters to"""

    status: Literal["DRAFT", "ACTIVE", "ARCHIVED"]

    success_message: Annotated[Optional[str], PropertyInfo(alias="successMessage")]

    title: str
