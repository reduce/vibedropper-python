# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vibedropper import Vibedropper, AsyncVibedropper
from vibedropper.types import (
    KnowledgeBaseListResponse,
    KnowledgeBaseUpdateResponse,
    KnowledgeBaseRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeBases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Vibedropper) -> None:
        knowledge_base = client.knowledge_bases.retrieve(
            "kbId",
        )
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Vibedropper) -> None:
        response = client.knowledge_bases.with_raw_response.retrieve(
            "kbId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Vibedropper) -> None:
        with client.knowledge_bases.with_streaming_response.retrieve(
            "kbId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.knowledge_bases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Vibedropper) -> None:
        knowledge_base = client.knowledge_bases.update(
            kb_id="kbId",
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Vibedropper) -> None:
        knowledge_base = client.knowledge_bases.update(
            kb_id="kbId",
            description="description",
            name="name",
            sort_order=0,
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Vibedropper) -> None:
        response = client.knowledge_bases.with_raw_response.update(
            kb_id="kbId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Vibedropper) -> None:
        with client.knowledge_bases.with_streaming_response.update(
            kb_id="kbId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.knowledge_bases.with_raw_response.update(
                kb_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Vibedropper) -> None:
        knowledge_base = client.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Vibedropper) -> None:
        response = client.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Vibedropper) -> None:
        with client.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Vibedropper) -> None:
        knowledge_base = client.knowledge_bases.delete(
            "kbId",
        )
        assert knowledge_base is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Vibedropper) -> None:
        response = client.knowledge_bases.with_raw_response.delete(
            "kbId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert knowledge_base is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Vibedropper) -> None:
        with client.knowledge_bases.with_streaming_response.delete(
            "kbId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert knowledge_base is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            client.knowledge_bases.with_raw_response.delete(
                "",
            )


class TestAsyncKnowledgeBases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVibedropper) -> None:
        knowledge_base = await async_client.knowledge_bases.retrieve(
            "kbId",
        )
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.knowledge_bases.with_raw_response.retrieve(
            "kbId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVibedropper) -> None:
        async with async_client.knowledge_bases.with_streaming_response.retrieve(
            "kbId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseRetrieveResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.knowledge_bases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVibedropper) -> None:
        knowledge_base = await async_client.knowledge_bases.update(
            kb_id="kbId",
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVibedropper) -> None:
        knowledge_base = await async_client.knowledge_bases.update(
            kb_id="kbId",
            description="description",
            name="name",
            sort_order=0,
        )
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.knowledge_bases.with_raw_response.update(
            kb_id="kbId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVibedropper) -> None:
        async with async_client.knowledge_bases.with_streaming_response.update(
            kb_id="kbId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseUpdateResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.knowledge_bases.with_raw_response.update(
                kb_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVibedropper) -> None:
        knowledge_base = await async_client.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVibedropper) -> None:
        async with async_client.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncVibedropper) -> None:
        knowledge_base = await async_client.knowledge_bases.delete(
            "kbId",
        )
        assert knowledge_base is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.knowledge_bases.with_raw_response.delete(
            "kbId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert knowledge_base is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVibedropper) -> None:
        async with async_client.knowledge_bases.with_streaming_response.delete(
            "kbId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert knowledge_base is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `kb_id` but received ''"):
            await async_client.knowledge_bases.with_raw_response.delete(
                "",
            )
