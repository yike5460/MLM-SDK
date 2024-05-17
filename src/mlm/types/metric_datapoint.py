# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MetricDatapoint"]


class MetricDatapoint(BaseModel):
    average: Optional[float] = FieldInfo(alias="Average", default=None)

    timestamp: Optional[datetime] = FieldInfo(alias="Timestamp", default=None)

    unit: Optional[str] = FieldInfo(alias="Unit", default=None)
