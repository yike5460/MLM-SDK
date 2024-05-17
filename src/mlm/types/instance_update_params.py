# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InstanceUpdateParams"]


class InstanceUpdateParams(TypedDict, total=False):
    endpoint_config_name: Annotated[str, PropertyInfo(alias="endpointConfigName")]
