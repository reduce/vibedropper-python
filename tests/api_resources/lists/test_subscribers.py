# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vibedropper import Vibedropper, AsyncVibedropper
from vibedropper.types.lists import (
    SubscriberAddResponse,
    SubscriberListResponse,
    SubscriberRemoveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscribers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Vibedropper) -> None:
        subscriber = client.lists.subscribers.list(
            "listId",
        )
        assert_matches_type(SubscriberListResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Vibedropper) -> None:
        response = client.lists.subscribers.with_raw_response.list(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscriber = response.parse()
        assert_matches_type(SubscriberListResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Vibedropper) -> None:
        with client.lists.subscribers.with_streaming_response.list(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscriber = response.parse()
            assert_matches_type(SubscriberListResponse, subscriber, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.lists.subscribers.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Vibedropper) -> None:
        subscriber = client.lists.subscribers.add(
            list_id="listId",
            email="dev@stainless.com",
        )
        assert_matches_type(SubscriberAddResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Vibedropper) -> None:
        subscriber = client.lists.subscribers.add(
            list_id="listId",
            email="dev@stainless.com",
            custom_fields={},
            name="name",
            pickup_location_id="pickupLocationId",
            region_id="regionId",
        )
        assert_matches_type(SubscriberAddResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Vibedropper) -> None:
        response = client.lists.subscribers.with_raw_response.add(
            list_id="listId",
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscriber = response.parse()
        assert_matches_type(SubscriberAddResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Vibedropper) -> None:
        with client.lists.subscribers.with_streaming_response.add(
            list_id="listId",
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscriber = response.parse()
            assert_matches_type(SubscriberAddResponse, subscriber, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.lists.subscribers.with_raw_response.add(
                list_id="",
                email="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Vibedropper) -> None:
        subscriber = client.lists.subscribers.remove(
            subscriber_id="subscriberId",
            list_id="listId",
        )
        assert_matches_type(SubscriberRemoveResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Vibedropper) -> None:
        response = client.lists.subscribers.with_raw_response.remove(
            subscriber_id="subscriberId",
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscriber = response.parse()
        assert_matches_type(SubscriberRemoveResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Vibedropper) -> None:
        with client.lists.subscribers.with_streaming_response.remove(
            subscriber_id="subscriberId",
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscriber = response.parse()
            assert_matches_type(SubscriberRemoveResponse, subscriber, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.lists.subscribers.with_raw_response.remove(
                subscriber_id="subscriberId",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id` but received ''"):
            client.lists.subscribers.with_raw_response.remove(
                subscriber_id="",
                list_id="listId",
            )


class TestAsyncSubscribers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVibedropper) -> None:
        subscriber = await async_client.lists.subscribers.list(
            "listId",
        )
        assert_matches_type(SubscriberListResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.lists.subscribers.with_raw_response.list(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscriber = await response.parse()
        assert_matches_type(SubscriberListResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVibedropper) -> None:
        async with async_client.lists.subscribers.with_streaming_response.list(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscriber = await response.parse()
            assert_matches_type(SubscriberListResponse, subscriber, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.lists.subscribers.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncVibedropper) -> None:
        subscriber = await async_client.lists.subscribers.add(
            list_id="listId",
            email="dev@stainless.com",
        )
        assert_matches_type(SubscriberAddResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncVibedropper) -> None:
        subscriber = await async_client.lists.subscribers.add(
            list_id="listId",
            email="dev@stainless.com",
            custom_fields={},
            name="name",
            pickup_location_id="pickupLocationId",
            region_id="regionId",
        )
        assert_matches_type(SubscriberAddResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.lists.subscribers.with_raw_response.add(
            list_id="listId",
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscriber = await response.parse()
        assert_matches_type(SubscriberAddResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncVibedropper) -> None:
        async with async_client.lists.subscribers.with_streaming_response.add(
            list_id="listId",
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscriber = await response.parse()
            assert_matches_type(SubscriberAddResponse, subscriber, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.lists.subscribers.with_raw_response.add(
                list_id="",
                email="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncVibedropper) -> None:
        subscriber = await async_client.lists.subscribers.remove(
            subscriber_id="subscriberId",
            list_id="listId",
        )
        assert_matches_type(SubscriberRemoveResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.lists.subscribers.with_raw_response.remove(
            subscriber_id="subscriberId",
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscriber = await response.parse()
        assert_matches_type(SubscriberRemoveResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncVibedropper) -> None:
        async with async_client.lists.subscribers.with_streaming_response.remove(
            subscriber_id="subscriberId",
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscriber = await response.parse()
            assert_matches_type(SubscriberRemoveResponse, subscriber, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.lists.subscribers.with_raw_response.remove(
                subscriber_id="subscriberId",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id` but received ''"):
            await async_client.lists.subscribers.with_raw_response.remove(
                subscriber_id="",
                list_id="listId",
            )
