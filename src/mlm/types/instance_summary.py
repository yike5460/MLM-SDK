# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InstanceSummary"]


class InstanceSummary(BaseModel):
    creation_time: Optional[datetime] = FieldInfo(alias="CreationTime", default=None)

    endpoint_arn: Optional[str] = FieldInfo(alias="EndpointArn", default=None)

    endpoint_name: Optional[str] = FieldInfo(alias="EndpointName", default=None)

    endpoint_status: Optional[str] = FieldInfo(alias="EndpointStatus", default=None)

    last_modified_time: Optional[datetime] = FieldInfo(alias="LastModifiedTime", default=None)
