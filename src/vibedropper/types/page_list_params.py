# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PageListParams"]


class PageListParams(TypedDict, total=False):
    limit: int

    page: int

    status: Literal["DRAFT", "ACTIVE", "ENDED", "ARCHIVED", "all"]
    """Filter by status. Omit or use "all" to return all pages."""
