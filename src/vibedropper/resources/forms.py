# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import form_list_params, form_update_params, form_list_submissions_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.form_list_response import FormListResponse
from ..types.form_delete_response import FormDeleteResponse
from ..types.form_update_response import FormUpdateResponse
from ..types.form_retrieve_response import FormRetrieveResponse
from ..types.form_list_submissions_response import FormListSubmissionsResponse

__all__ = ["FormsResource", "AsyncFormsResource"]


class FormsResource(SyncAPIResource):
    """Manage forms and submissions"""

    @cached_property
    def with_raw_response(self) -> FormsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reduce/vibedropper-python#accessing-raw-response-data-eg-headers
        """
        return FormsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FormsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reduce/vibedropper-python#with_streaming_response
        """
        return FormsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        form_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormRetrieveResponse:
        """
        Get a form

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return self._get(
            path_template("/forms/{form_id}", form_id=form_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormRetrieveResponse,
        )

    def update(
        self,
        form_id: str,
        *,
        description: Optional[str] | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        status: Literal["DRAFT", "ACTIVE", "ARCHIVED"] | Omit = omit,
        success_message: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormUpdateResponse:
        """
        Update a form

        Args:
          list_id: List to subscribe form submitters to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return self._put(
            path_template("/forms/{form_id}", form_id=form_id),
            body=maybe_transform(
                {
                    "description": description,
                    "list_id": list_id,
                    "status": status,
                    "success_message": success_message,
                    "title": title,
                },
                form_update_params.FormUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        status: Literal["DRAFT", "ACTIVE", "ARCHIVED", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormListResponse:
        """List forms

        Args:
          status: Filter by status.

        Omit or use "all" to return all forms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/forms",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    form_list_params.FormListParams,
                ),
            ),
            cast_to=FormListResponse,
        )

    def delete(
        self,
        form_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDeleteResponse:
        """
        Delete a form

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return self._delete(
            path_template("/forms/{form_id}", form_id=form_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormDeleteResponse,
        )

    def list_submissions(
        self,
        form_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormListSubmissionsResponse:
        """
        List form submissions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return self._get(
            path_template("/forms/{form_id}/submissions", form_id=form_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    form_list_submissions_params.FormListSubmissionsParams,
                ),
            ),
            cast_to=FormListSubmissionsResponse,
        )


class AsyncFormsResource(AsyncAPIResource):
    """Manage forms and submissions"""

    @cached_property
    def with_raw_response(self) -> AsyncFormsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reduce/vibedropper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFormsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFormsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reduce/vibedropper-python#with_streaming_response
        """
        return AsyncFormsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        form_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormRetrieveResponse:
        """
        Get a form

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return await self._get(
            path_template("/forms/{form_id}", form_id=form_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormRetrieveResponse,
        )

    async def update(
        self,
        form_id: str,
        *,
        description: Optional[str] | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        status: Literal["DRAFT", "ACTIVE", "ARCHIVED"] | Omit = omit,
        success_message: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormUpdateResponse:
        """
        Update a form

        Args:
          list_id: List to subscribe form submitters to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return await self._put(
            path_template("/forms/{form_id}", form_id=form_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "list_id": list_id,
                    "status": status,
                    "success_message": success_message,
                    "title": title,
                },
                form_update_params.FormUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormUpdateResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        status: Literal["DRAFT", "ACTIVE", "ARCHIVED", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormListResponse:
        """List forms

        Args:
          status: Filter by status.

        Omit or use "all" to return all forms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/forms",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    form_list_params.FormListParams,
                ),
            ),
            cast_to=FormListResponse,
        )

    async def delete(
        self,
        form_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDeleteResponse:
        """
        Delete a form

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return await self._delete(
            path_template("/forms/{form_id}", form_id=form_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormDeleteResponse,
        )

    async def list_submissions(
        self,
        form_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormListSubmissionsResponse:
        """
        List form submissions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return await self._get(
            path_template("/forms/{form_id}/submissions", form_id=form_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    form_list_submissions_params.FormListSubmissionsParams,
                ),
            ),
            cast_to=FormListSubmissionsResponse,
        )


class FormsResourceWithRawResponse:
    def __init__(self, forms: FormsResource) -> None:
        self._forms = forms

        self.retrieve = to_raw_response_wrapper(
            forms.retrieve,
        )
        self.update = to_raw_response_wrapper(
            forms.update,
        )
        self.list = to_raw_response_wrapper(
            forms.list,
        )
        self.delete = to_raw_response_wrapper(
            forms.delete,
        )
        self.list_submissions = to_raw_response_wrapper(
            forms.list_submissions,
        )


class AsyncFormsResourceWithRawResponse:
    def __init__(self, forms: AsyncFormsResource) -> None:
        self._forms = forms

        self.retrieve = async_to_raw_response_wrapper(
            forms.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            forms.update,
        )
        self.list = async_to_raw_response_wrapper(
            forms.list,
        )
        self.delete = async_to_raw_response_wrapper(
            forms.delete,
        )
        self.list_submissions = async_to_raw_response_wrapper(
            forms.list_submissions,
        )


class FormsResourceWithStreamingResponse:
    def __init__(self, forms: FormsResource) -> None:
        self._forms = forms

        self.retrieve = to_streamed_response_wrapper(
            forms.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            forms.update,
        )
        self.list = to_streamed_response_wrapper(
            forms.list,
        )
        self.delete = to_streamed_response_wrapper(
            forms.delete,
        )
        self.list_submissions = to_streamed_response_wrapper(
            forms.list_submissions,
        )


class AsyncFormsResourceWithStreamingResponse:
    def __init__(self, forms: AsyncFormsResource) -> None:
        self._forms = forms

        self.retrieve = async_to_streamed_response_wrapper(
            forms.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            forms.update,
        )
        self.list = async_to_streamed_response_wrapper(
            forms.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            forms.delete,
        )
        self.list_submissions = async_to_streamed_response_wrapper(
            forms.list_submissions,
        )
