# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelSummary"]


class ModelSummary(BaseModel):
    creation_time: Optional[datetime] = FieldInfo(alias="CreationTime", default=None)

    api_model_arn: Optional[str] = FieldInfo(alias="ModelArn", default=None)

    api_model_name: Optional[str] = FieldInfo(alias="ModelName", default=None)
