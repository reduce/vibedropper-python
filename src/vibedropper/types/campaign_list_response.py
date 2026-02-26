# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .campaign import Campaign

__all__ = ["CampaignListResponse"]


class CampaignListResponse(BaseModel):
    campaigns: Optional[List[Campaign]] = None
