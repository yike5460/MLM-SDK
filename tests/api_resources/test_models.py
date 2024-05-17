# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mlm import Mlm, AsyncMlm
from mlm.types import (
    ModelDetails,
    ModelListResponse,
    ModelCreateResponse,
    ModelUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mlm) -> None:
        model = client.models.create()
        assert_matches_type(ModelCreateResponse, model, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mlm) -> None:
        model = client.models.create(
            execution_role_arn="string",
            model_name="string",
            primary_container={
                "image": "string",
                "model_data_url": "string",
            },
        )
        assert_matches_type(ModelCreateResponse, model, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mlm) -> None:
        response = client.models.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelCreateResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mlm) -> None:
        with client.models.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelCreateResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Mlm) -> None:
        model = client.models.retrieve(
            "string",
        )
        assert_matches_type(ModelDetails, model, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mlm) -> None:
        response = client.models.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelDetails, model, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mlm) -> None:
        with client.models.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelDetails, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.models.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Mlm) -> None:
        model = client.models.update(
            "string",
            body={},
        )
        assert_matches_type(ModelUpdateResponse, model, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mlm) -> None:
        response = client.models.with_raw_response.update(
            "string",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelUpdateResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mlm) -> None:
        with client.models.with_streaming_response.update(
            "string",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelUpdateResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.models.with_raw_response.update(
                "",
                body={},
            )

    @parametrize
    def test_method_list(self, client: Mlm) -> None:
        model = client.models.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mlm) -> None:
        response = client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mlm) -> None:
        with client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Mlm) -> None:
        model = client.models.delete(
            "string",
        )
        assert_matches_type(object, model, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mlm) -> None:
        response = client.models.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(object, model, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mlm) -> None:
        with client.models.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(object, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.models.with_raw_response.delete(
                "",
            )


class TestAsyncModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMlm) -> None:
        model = await async_client.models.create()
        assert_matches_type(ModelCreateResponse, model, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMlm) -> None:
        model = await async_client.models.create(
            execution_role_arn="string",
            model_name="string",
            primary_container={
                "image": "string",
                "model_data_url": "string",
            },
        )
        assert_matches_type(ModelCreateResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMlm) -> None:
        response = await async_client.models.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelCreateResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMlm) -> None:
        async with async_client.models.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelCreateResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMlm) -> None:
        model = await async_client.models.retrieve(
            "string",
        )
        assert_matches_type(ModelDetails, model, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMlm) -> None:
        response = await async_client.models.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelDetails, model, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMlm) -> None:
        async with async_client.models.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelDetails, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.models.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMlm) -> None:
        model = await async_client.models.update(
            "string",
            body={},
        )
        assert_matches_type(ModelUpdateResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMlm) -> None:
        response = await async_client.models.with_raw_response.update(
            "string",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelUpdateResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMlm) -> None:
        async with async_client.models.with_streaming_response.update(
            "string",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelUpdateResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.models.with_raw_response.update(
                "",
                body={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMlm) -> None:
        model = await async_client.models.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMlm) -> None:
        response = await async_client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMlm) -> None:
        async with async_client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMlm) -> None:
        model = await async_client.models.delete(
            "string",
        )
        assert_matches_type(object, model, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMlm) -> None:
        response = await async_client.models.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(object, model, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMlm) -> None:
        async with async_client.models.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(object, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMlm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.models.with_raw_response.delete(
                "",
            )
