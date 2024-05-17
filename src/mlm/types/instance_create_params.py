# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InstanceCreateParams"]


class InstanceCreateParams(TypedDict, total=False):
    instance_name: Annotated[str, PropertyInfo(alias="instanceName")]

    instance_type: Annotated[str, PropertyInfo(alias="instanceType")]

    model_name: Annotated[str, PropertyInfo(alias="modelName")]
