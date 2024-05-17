# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InstanceUpdateResponse"]


class InstanceUpdateResponse(BaseModel):
    endpoint_arn: Optional[str] = FieldInfo(alias="EndpointArn", default=None)

    endpoint_name: Optional[str] = FieldInfo(alias="EndpointName", default=None)
