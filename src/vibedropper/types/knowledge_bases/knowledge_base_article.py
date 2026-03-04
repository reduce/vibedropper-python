# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["KnowledgeBaseArticle", "Category"]


class Category(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    slug: Optional[str] = None


class KnowledgeBaseArticle(BaseModel):
    id: Optional[str] = None

    category: Optional[Category] = None

    category_id: Optional[str] = FieldInfo(alias="categoryId", default=None)

    content: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    excerpt: Optional[str] = None

    knowledge_base_id: Optional[str] = FieldInfo(alias="knowledgeBaseId", default=None)

    published: Optional[bool] = None

    slug: Optional[str] = None

    sort_order: Optional[int] = FieldInfo(alias="sortOrder", default=None)

    title: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
