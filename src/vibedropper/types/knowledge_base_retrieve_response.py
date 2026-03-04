# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .knowledge_base import KnowledgeBase

__all__ = ["KnowledgeBaseRetrieveResponse"]


class KnowledgeBaseRetrieveResponse(BaseModel):
    knowledge_base: Optional[KnowledgeBase] = FieldInfo(alias="knowledgeBase", default=None)
