# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ArticleCreateParams"]


class ArticleCreateParams(TypedDict, total=False):
    title: Required[str]

    category_id: Annotated[Optional[str], PropertyInfo(alias="categoryId")]

    content: str
    """HTML or markdown content"""

    excerpt: Optional[str]

    published: bool
