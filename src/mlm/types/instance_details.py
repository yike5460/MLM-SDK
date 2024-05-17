# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InstanceDetails", "ProductionVariant"]


class ProductionVariant(BaseModel):
    current_instance_count: Optional[int] = FieldInfo(alias="CurrentInstanceCount", default=None)

    desired_instance_count: Optional[int] = FieldInfo(alias="DesiredInstanceCount", default=None)

    instance_type: Optional[str] = FieldInfo(alias="InstanceType", default=None)

    api_model_name: Optional[str] = FieldInfo(alias="ModelName", default=None)

    variant_name: Optional[str] = FieldInfo(alias="VariantName", default=None)


class InstanceDetails(BaseModel):
    creation_time: Optional[datetime] = FieldInfo(alias="CreationTime", default=None)

    endpoint_arn: Optional[str] = FieldInfo(alias="EndpointArn", default=None)

    endpoint_config_name: Optional[str] = FieldInfo(alias="EndpointConfigName", default=None)

    endpoint_name: Optional[str] = FieldInfo(alias="EndpointName", default=None)

    endpoint_status: Optional[str] = FieldInfo(alias="EndpointStatus", default=None)

    last_modified_time: Optional[datetime] = FieldInfo(alias="LastModifiedTime", default=None)

    production_variants: Optional[List[ProductionVariant]] = FieldInfo(alias="ProductionVariants", default=None)
