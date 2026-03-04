# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .knowledge_base import KnowledgeBase

__all__ = ["KnowledgeBaseListResponse"]


class KnowledgeBaseListResponse(BaseModel):
    knowledge_bases: Optional[List[KnowledgeBase]] = FieldInfo(alias="knowledgeBases", default=None)
