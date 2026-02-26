# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vibedropper import Vibedropper, AsyncVibedropper
from vibedropper.types import (
    CustomerListResponse,
    CustomerUpdateResponse,
    CustomerRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Vibedropper) -> None:
        customer = client.customers.retrieve(
            "customerId",
        )
        assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Vibedropper) -> None:
        response = client.customers.with_raw_response.retrieve(
            "customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Vibedropper) -> None:
        with client.customers.with_streaming_response.retrieve(
            "customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Vibedropper) -> None:
        customer = client.customers.update(
            customer_id="customerId",
        )
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Vibedropper) -> None:
        customer = client.customers.update(
            customer_id="customerId",
            name="name",
            pickup_location_id="pickupLocationId",
            region_id="regionId",
        )
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Vibedropper) -> None:
        response = client.customers.with_raw_response.update(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Vibedropper) -> None:
        with client.customers.with_streaming_response.update(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.with_raw_response.update(
                customer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Vibedropper) -> None:
        customer = client.customers.list()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Vibedropper) -> None:
        customer = client.customers.list(
            limit=0,
            page=0,
            search="search",
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Vibedropper) -> None:
        response = client.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Vibedropper) -> None:
        with client.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerListResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVibedropper) -> None:
        customer = await async_client.customers.retrieve(
            "customerId",
        )
        assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.customers.with_raw_response.retrieve(
            "customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVibedropper) -> None:
        async with async_client.customers.with_streaming_response.retrieve(
            "customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVibedropper) -> None:
        customer = await async_client.customers.update(
            customer_id="customerId",
        )
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVibedropper) -> None:
        customer = await async_client.customers.update(
            customer_id="customerId",
            name="name",
            pickup_location_id="pickupLocationId",
            region_id="regionId",
        )
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.customers.with_raw_response.update(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVibedropper) -> None:
        async with async_client.customers.with_streaming_response.update(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.with_raw_response.update(
                customer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVibedropper) -> None:
        customer = await async_client.customers.list()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVibedropper) -> None:
        customer = await async_client.customers.list(
            limit=0,
            page=0,
            search="search",
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVibedropper) -> None:
        async with async_client.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerListResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True
