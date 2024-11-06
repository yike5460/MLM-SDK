# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .metric_datapoint import MetricDatapoint

__all__ = ["MetricListResponse"]

MetricListResponse: TypeAlias = List[MetricDatapoint]
