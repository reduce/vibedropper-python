# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vibedropper import Vibedropper, AsyncVibedropper
from vibedropper.types import (
    PageListResponse,
    PageDeleteResponse,
    PageUpdateResponse,
    PageRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Vibedropper) -> None:
        page = client.pages.retrieve(
            "pageId",
        )
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Vibedropper) -> None:
        response = client.pages.with_raw_response.retrieve(
            "pageId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Vibedropper) -> None:
        with client.pages.with_streaming_response.retrieve(
            "pageId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageRetrieveResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.pages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Vibedropper) -> None:
        page = client.pages.update(
            page_id="pageId",
        )
        assert_matches_type(PageUpdateResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Vibedropper) -> None:
        page = client.pages.update(
            page_id="pageId",
            description="description",
            name="name",
            status="DRAFT",
        )
        assert_matches_type(PageUpdateResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Vibedropper) -> None:
        response = client.pages.with_raw_response.update(
            page_id="pageId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageUpdateResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Vibedropper) -> None:
        with client.pages.with_streaming_response.update(
            page_id="pageId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageUpdateResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.pages.with_raw_response.update(
                page_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Vibedropper) -> None:
        page = client.pages.list()
        assert_matches_type(PageListResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Vibedropper) -> None:
        page = client.pages.list(
            limit=100,
            page=0,
            status="DRAFT",
        )
        assert_matches_type(PageListResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Vibedropper) -> None:
        response = client.pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageListResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Vibedropper) -> None:
        with client.pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageListResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Vibedropper) -> None:
        page = client.pages.delete(
            "pageId",
        )
        assert_matches_type(PageDeleteResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Vibedropper) -> None:
        response = client.pages.with_raw_response.delete(
            "pageId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageDeleteResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Vibedropper) -> None:
        with client.pages.with_streaming_response.delete(
            "pageId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageDeleteResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.pages.with_raw_response.delete(
                "",
            )


class TestAsyncPages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVibedropper) -> None:
        page = await async_client.pages.retrieve(
            "pageId",
        )
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.pages.with_raw_response.retrieve(
            "pageId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVibedropper) -> None:
        async with async_client.pages.with_streaming_response.retrieve(
            "pageId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageRetrieveResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.pages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVibedropper) -> None:
        page = await async_client.pages.update(
            page_id="pageId",
        )
        assert_matches_type(PageUpdateResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVibedropper) -> None:
        page = await async_client.pages.update(
            page_id="pageId",
            description="description",
            name="name",
            status="DRAFT",
        )
        assert_matches_type(PageUpdateResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.pages.with_raw_response.update(
            page_id="pageId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageUpdateResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVibedropper) -> None:
        async with async_client.pages.with_streaming_response.update(
            page_id="pageId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageUpdateResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.pages.with_raw_response.update(
                page_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVibedropper) -> None:
        page = await async_client.pages.list()
        assert_matches_type(PageListResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVibedropper) -> None:
        page = await async_client.pages.list(
            limit=100,
            page=0,
            status="DRAFT",
        )
        assert_matches_type(PageListResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageListResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVibedropper) -> None:
        async with async_client.pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageListResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncVibedropper) -> None:
        page = await async_client.pages.delete(
            "pageId",
        )
        assert_matches_type(PageDeleteResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.pages.with_raw_response.delete(
            "pageId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageDeleteResponse, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVibedropper) -> None:
        async with async_client.pages.with_streaming_response.delete(
            "pageId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageDeleteResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.pages.with_raw_response.delete(
                "",
            )
