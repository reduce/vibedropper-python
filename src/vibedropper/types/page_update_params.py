# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["PageUpdateParams"]


class PageUpdateParams(TypedDict, total=False):
    description: Optional[str]

    name: str

    status: Literal["DRAFT", "ACTIVE", "ENDED", "ARCHIVED"]
