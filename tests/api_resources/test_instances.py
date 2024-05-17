# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mlm import Mlm, AsyncMlm
from mlm.types import (
    InstanceDetails,
    InstanceListResponse,
    InstanceCreateResponse,
    InstanceUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mlm) -> None:
        instance = client.instances.create()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mlm) -> None:
        instance = client.instances.create(
            instance_name="string",
            instance_type="string",
            model_name="string",
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mlm) -> None:
        response = client.instances.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mlm) -> None:
        with client.instances.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceCreateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Mlm) -> None:
        instance = client.instances.retrieve(
            "string",
        )
        assert_matches_type(InstanceDetails, instance, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mlm) -> None:
        response = client.instances.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceDetails, instance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mlm) -> None:
        with client.instances.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceDetails, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_name` but received ''"):
            client.instances.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Mlm) -> None:
        instance = client.instances.update(
            "string",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Mlm) -> None:
        instance = client.instances.update(
            "string",
            endpoint_config_name="string",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mlm) -> None:
        response = client.instances.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mlm) -> None:
        with client.instances.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_name` but received ''"):
            client.instances.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Mlm) -> None:
        instance = client.instances.list()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mlm) -> None:
        response = client.instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mlm) -> None:
        with client.instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceListResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Mlm) -> None:
        instance = client.instances.delete(
            "string",
        )
        assert instance is None

    @parametrize
    def test_raw_response_delete(self, client: Mlm) -> None:
        response = client.instances.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert instance is None

    @parametrize
    def test_streaming_response_delete(self, client: Mlm) -> None:
        with client.instances.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert instance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_name` but received ''"):
            client.instances.with_raw_response.delete(
                "",
            )


class TestAsyncInstances:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMlm) -> None:
        instance = await async_client.instances.create()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMlm) -> None:
        instance = await async_client.instances.create(
            instance_name="string",
            instance_type="string",
            model_name="string",
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMlm) -> None:
        response = await async_client.instances.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMlm) -> None:
        async with async_client.instances.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceCreateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMlm) -> None:
        instance = await async_client.instances.retrieve(
            "string",
        )
        assert_matches_type(InstanceDetails, instance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMlm) -> None:
        response = await async_client.instances.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceDetails, instance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMlm) -> None:
        async with async_client.instances.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceDetails, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_name` but received ''"):
            await async_client.instances.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMlm) -> None:
        instance = await async_client.instances.update(
            "string",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMlm) -> None:
        instance = await async_client.instances.update(
            "string",
            endpoint_config_name="string",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMlm) -> None:
        response = await async_client.instances.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMlm) -> None:
        async with async_client.instances.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_name` but received ''"):
            await async_client.instances.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMlm) -> None:
        instance = await async_client.instances.list()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMlm) -> None:
        response = await async_client.instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMlm) -> None:
        async with async_client.instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceListResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMlm) -> None:
        instance = await async_client.instances.delete(
            "string",
        )
        assert instance is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMlm) -> None:
        response = await async_client.instances.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert instance is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMlm) -> None:
        async with async_client.instances.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert instance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_name` but received ''"):
            await async_client.instances.with_raw_response.delete(
                "",
            )
