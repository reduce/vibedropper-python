# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .form import Form
from .._models import BaseModel

__all__ = ["FormUpdateResponse"]


class FormUpdateResponse(BaseModel):
    form: Optional[Form] = None
