# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelCreateResponse"]


class ModelCreateResponse(BaseModel):
    api_model_arn: Optional[str] = FieldInfo(alias="ModelArn", default=None)

    api_model_name: Optional[str] = FieldInfo(alias="ModelName", default=None)
