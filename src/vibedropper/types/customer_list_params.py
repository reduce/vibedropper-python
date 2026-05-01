# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    limit: int

    page: int

    search: str
    """Search by name or email (case-insensitive)"""
