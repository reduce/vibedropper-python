# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination import Pagination
from .knowledge_base_article import KnowledgeBaseArticle

__all__ = ["ArticleListResponse"]


class ArticleListResponse(BaseModel):
    articles: Optional[List[KnowledgeBaseArticle]] = None

    pagination: Optional[Pagination] = None
