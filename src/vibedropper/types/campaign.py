# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Campaign"]


class Campaign(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    from_email: Optional[str] = FieldInfo(alias="fromEmail", default=None)

    from_name: Optional[str] = FieldInfo(alias="fromName", default=None)

    name: Optional[str] = None

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    reply_to: Optional[str] = FieldInfo(alias="replyTo", default=None)

    scheduled_at: Optional[datetime] = FieldInfo(alias="scheduledAt", default=None)

    sent_at: Optional[datetime] = FieldInfo(alias="sentAt", default=None)

    status: Optional[Literal["DRAFT", "SCHEDULED", "SENDING", "SENT"]] = None

    subject: Optional[str] = None

    total_bounces: Optional[int] = FieldInfo(alias="totalBounces", default=None)

    total_clicks: Optional[int] = FieldInfo(alias="totalClicks", default=None)
    """Total click events"""

    total_opens: Optional[int] = FieldInfo(alias="totalOpens", default=None)
    """Unique opens"""

    total_sent: Optional[int] = FieldInfo(alias="totalSent", default=None)

    total_unsubscribes: Optional[int] = FieldInfo(alias="totalUnsubscribes", default=None)

    total_views: Optional[int] = FieldInfo(alias="totalViews", default=None)
    """Total view events (all pixel loads)"""

    unique_clicks: Optional[int] = FieldInfo(alias="uniqueClicks", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
