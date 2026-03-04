# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .knowledge_base_article import KnowledgeBaseArticle

__all__ = ["ArticleCreateResponse"]


class ArticleCreateResponse(BaseModel):
    article: Optional[KnowledgeBaseArticle] = None
