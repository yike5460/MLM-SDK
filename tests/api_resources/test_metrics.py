# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mlm import Mlm, AsyncMlm
from mlm.types import MetricListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Mlm) -> None:
        metric = client.metrics.list(
            instance_name="string",
            metric_name="string",
        )
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mlm) -> None:
        response = client.metrics.with_raw_response.list(
            instance_name="string",
            metric_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mlm) -> None:
        with client.metrics.with_streaming_response.list(
            instance_name="string",
            metric_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricListResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMlm) -> None:
        metric = await async_client.metrics.list(
            instance_name="string",
            metric_name="string",
        )
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMlm) -> None:
        response = await async_client.metrics.with_raw_response.list(
            instance_name="string",
            metric_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMlm) -> None:
        async with async_client.metrics.with_streaming_response.list(
            instance_name="string",
            metric_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricListResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True
