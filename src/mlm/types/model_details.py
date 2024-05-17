# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelDetails", "PrimaryContainer"]


class PrimaryContainer(BaseModel):
    image: Optional[str] = FieldInfo(alias="Image", default=None)

    api_model_data_url: Optional[str] = FieldInfo(alias="ModelDataUrl", default=None)


class ModelDetails(BaseModel):
    creation_time: Optional[datetime] = FieldInfo(alias="CreationTime", default=None)

    execution_role_arn: Optional[str] = FieldInfo(alias="ExecutionRoleArn", default=None)

    api_model_arn: Optional[str] = FieldInfo(alias="ModelArn", default=None)

    api_model_name: Optional[str] = FieldInfo(alias="ModelName", default=None)

    primary_container: Optional[PrimaryContainer] = FieldInfo(alias="PrimaryContainer", default=None)
