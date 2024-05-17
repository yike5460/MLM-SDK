# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InstanceCreateResponse", "ProductionVariant"]


class ProductionVariant(BaseModel):
    initial_instance_count: Optional[int] = FieldInfo(alias="InitialInstanceCount", default=None)

    instance_type: Optional[str] = FieldInfo(alias="InstanceType", default=None)

    api_model_name: Optional[str] = FieldInfo(alias="ModelName", default=None)

    variant_name: Optional[str] = FieldInfo(alias="VariantName", default=None)


class InstanceCreateResponse(BaseModel):
    endpoint_arn: Optional[str] = FieldInfo(alias="EndpointArn", default=None)

    endpoint_config_name: Optional[str] = FieldInfo(alias="EndpointConfigName", default=None)

    endpoint_name: Optional[str] = FieldInfo(alias="EndpointName", default=None)

    production_variants: Optional[List[ProductionVariant]] = FieldInfo(alias="ProductionVariants", default=None)
