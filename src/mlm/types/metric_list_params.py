# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetricListParams"]


class MetricListParams(TypedDict, total=False):
    instance_name: Required[Annotated[str, PropertyInfo(alias="instanceName")]]

    metric_name: Required[Annotated[str, PropertyInfo(alias="metricName")]]
