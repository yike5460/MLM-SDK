# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelCreateParams", "PrimaryContainer"]


class ModelCreateParams(TypedDict, total=False):
    execution_role_arn: Annotated[str, PropertyInfo(alias="executionRoleArn")]

    model_name: Annotated[str, PropertyInfo(alias="modelName")]

    primary_container: Annotated[PrimaryContainer, PropertyInfo(alias="primaryContainer")]


class PrimaryContainer(TypedDict, total=False):
    image: Annotated[str, PropertyInfo(alias="Image")]

    model_data_url: Annotated[str, PropertyInfo(alias="ModelDataUrl")]
