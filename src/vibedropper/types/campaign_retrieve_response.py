# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .campaign import Campaign

__all__ = ["CampaignRetrieveResponse"]


class CampaignRetrieveResponse(BaseModel):
    campaign: Optional[Campaign] = None
