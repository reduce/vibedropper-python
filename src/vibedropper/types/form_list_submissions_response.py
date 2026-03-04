# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .pagination import Pagination

__all__ = ["FormListSubmissionsResponse", "Submission", "SubmissionSubscriber"]


class SubmissionSubscriber(BaseModel):
    id: Optional[str] = None

    email: Optional[str] = None

    name: Optional[str] = None


class Submission(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    data: Optional[object] = None
    """Key-value pairs of submitted form fields"""

    form_id: Optional[str] = FieldInfo(alias="formId", default=None)

    subscriber: Optional[SubmissionSubscriber] = None


class FormListSubmissionsResponse(BaseModel):
    pagination: Optional[Pagination] = None

    submissions: Optional[List[Submission]] = None
