# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vibedropper import Vibedropper, AsyncVibedropper
from vibedropper.types import (
    FormListResponse,
    FormDeleteResponse,
    FormUpdateResponse,
    FormRetrieveResponse,
    FormListSubmissionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestForms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Vibedropper) -> None:
        form = client.forms.retrieve(
            "formId",
        )
        assert_matches_type(FormRetrieveResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Vibedropper) -> None:
        response = client.forms.with_raw_response.retrieve(
            "formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormRetrieveResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Vibedropper) -> None:
        with client.forms.with_streaming_response.retrieve(
            "formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormRetrieveResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.forms.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Vibedropper) -> None:
        form = client.forms.update(
            form_id="formId",
        )
        assert_matches_type(FormUpdateResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Vibedropper) -> None:
        form = client.forms.update(
            form_id="formId",
            description="description",
            list_id="listId",
            status="DRAFT",
            success_message="successMessage",
            title="title",
        )
        assert_matches_type(FormUpdateResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Vibedropper) -> None:
        response = client.forms.with_raw_response.update(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormUpdateResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Vibedropper) -> None:
        with client.forms.with_streaming_response.update(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormUpdateResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.forms.with_raw_response.update(
                form_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Vibedropper) -> None:
        form = client.forms.list()
        assert_matches_type(FormListResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Vibedropper) -> None:
        form = client.forms.list(
            limit=100,
            page=0,
            status="DRAFT",
        )
        assert_matches_type(FormListResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Vibedropper) -> None:
        response = client.forms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormListResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Vibedropper) -> None:
        with client.forms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormListResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Vibedropper) -> None:
        form = client.forms.delete(
            "formId",
        )
        assert_matches_type(FormDeleteResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Vibedropper) -> None:
        response = client.forms.with_raw_response.delete(
            "formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormDeleteResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Vibedropper) -> None:
        with client.forms.with_streaming_response.delete(
            "formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormDeleteResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.forms.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_submissions(self, client: Vibedropper) -> None:
        form = client.forms.list_submissions(
            form_id="formId",
        )
        assert_matches_type(FormListSubmissionsResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_submissions_with_all_params(self, client: Vibedropper) -> None:
        form = client.forms.list_submissions(
            form_id="formId",
            limit=100,
            page=0,
        )
        assert_matches_type(FormListSubmissionsResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_submissions(self, client: Vibedropper) -> None:
        response = client.forms.with_raw_response.list_submissions(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormListSubmissionsResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_submissions(self, client: Vibedropper) -> None:
        with client.forms.with_streaming_response.list_submissions(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormListSubmissionsResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_submissions(self, client: Vibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.forms.with_raw_response.list_submissions(
                form_id="",
            )


class TestAsyncForms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVibedropper) -> None:
        form = await async_client.forms.retrieve(
            "formId",
        )
        assert_matches_type(FormRetrieveResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.forms.with_raw_response.retrieve(
            "formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormRetrieveResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVibedropper) -> None:
        async with async_client.forms.with_streaming_response.retrieve(
            "formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormRetrieveResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.forms.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVibedropper) -> None:
        form = await async_client.forms.update(
            form_id="formId",
        )
        assert_matches_type(FormUpdateResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVibedropper) -> None:
        form = await async_client.forms.update(
            form_id="formId",
            description="description",
            list_id="listId",
            status="DRAFT",
            success_message="successMessage",
            title="title",
        )
        assert_matches_type(FormUpdateResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.forms.with_raw_response.update(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormUpdateResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVibedropper) -> None:
        async with async_client.forms.with_streaming_response.update(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormUpdateResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.forms.with_raw_response.update(
                form_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVibedropper) -> None:
        form = await async_client.forms.list()
        assert_matches_type(FormListResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVibedropper) -> None:
        form = await async_client.forms.list(
            limit=100,
            page=0,
            status="DRAFT",
        )
        assert_matches_type(FormListResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.forms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormListResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVibedropper) -> None:
        async with async_client.forms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormListResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncVibedropper) -> None:
        form = await async_client.forms.delete(
            "formId",
        )
        assert_matches_type(FormDeleteResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.forms.with_raw_response.delete(
            "formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormDeleteResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVibedropper) -> None:
        async with async_client.forms.with_streaming_response.delete(
            "formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormDeleteResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.forms.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_submissions(self, async_client: AsyncVibedropper) -> None:
        form = await async_client.forms.list_submissions(
            form_id="formId",
        )
        assert_matches_type(FormListSubmissionsResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_submissions_with_all_params(self, async_client: AsyncVibedropper) -> None:
        form = await async_client.forms.list_submissions(
            form_id="formId",
            limit=100,
            page=0,
        )
        assert_matches_type(FormListSubmissionsResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_submissions(self, async_client: AsyncVibedropper) -> None:
        response = await async_client.forms.with_raw_response.list_submissions(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormListSubmissionsResponse, form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_submissions(self, async_client: AsyncVibedropper) -> None:
        async with async_client.forms.with_streaming_response.list_submissions(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormListSubmissionsResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_submissions(self, async_client: AsyncVibedropper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.forms.with_raw_response.list_submissions(
                form_id="",
            )
