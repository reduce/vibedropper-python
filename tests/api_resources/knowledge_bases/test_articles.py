# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vibedropper import Vibedropper, AsyncVibedropper
from vibedropper.types.knowledge_bases import (
    ArticleListResponse,
    ArticleCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArticles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Vibedropper) -> None:
        article = client.knowledge_bases.articles.create(
            kb_id="kbId",
            title="title",
        )
        assert_matches_type(ArticleCreateResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Vibedropper) -> None:
        article = client.knowledge_bases.articles.create(
            kb_id="kbId",
            title="title",
            category_id="categoryId",
            content="content",
            excerpt="excerpt",
            published=True,
        )
        assert_matches_type(ArticleCreateResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Vibedropper) -> None:
        response = client.knowledge_bases.articles.with_raw_response.create(
            kb_id="kbId",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(ArticleCreateResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Vibedropper) -> None:
        with client.knowledge_bases.articles.with_streaming_response.create(
            kb_id="kbId",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(ArticleCreateResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.knowledge_bases.articles.with_raw_response.create(
                kb_id="",
                title="title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Vibedropper) -> None:
        article = client.knowledge_bases.articles.list(
            kb_id="kbId",
        )
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Vibedropper) -> None:
        article = client.knowledge_bases.articles.list(
            kb_id="kbId",
            limit=100,
            page=0,
        )
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Vibedropper) -> None:
        response = client.knowledge_bases.articles.with_raw_response.list(
            kb_id="kbId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Vibedropper) -> None:
        with client.knowledge_bases.articles.with_streaming_response.list(
            kb_id="kbId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(ArticleListResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.knowledge_bases.articles.with_raw_response.list(
                kb_id="",
            )


class TestAsyncArticles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVibedropper) -> None:
        article = await async_client.knowledge_bases.articles.create(
            kb_id="kbId",
            title="title",
        )
        assert_matches_type(ArticleCreateResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVibedropper) -> None:
        article = await async_client.knowledge_bases.articles.create(
            kb_id="kbId",
            title="title",
            category_id="categoryId",
            content="content",
            excerpt="excerpt",
            published=True,
        )
        assert_matches_type(ArticleCreateResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.knowledge_bases.articles.with_raw_response.create(
            kb_id="kbId",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(ArticleCreateResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVibedropper) -> None:
        async with async_client.knowledge_bases.articles.with_streaming_response.create(
            kb_id="kbId",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(ArticleCreateResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.knowledge_bases.articles.with_raw_response.create(
                kb_id="",
                title="title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVibedropper) -> None:
        article = await async_client.knowledge_bases.articles.list(
            kb_id="kbId",
        )
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVibedropper) -> None:
        article = await async_client.knowledge_bases.articles.list(
            kb_id="kbId",
            limit=100,
            page=0,
        )
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.knowledge_bases.articles.with_raw_response.list(
            kb_id="kbId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVibedropper) -> None:
        async with async_client.knowledge_bases.articles.with_streaming_response.list(
            kb_id="kbId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(ArticleListResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.knowledge_bases.articles.with_raw_response.list(
                kb_id="",
            )
