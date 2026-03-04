# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import page_list_params, page_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.page_list_response import PageListResponse
from ..types.page_delete_response import PageDeleteResponse
from ..types.page_update_response import PageUpdateResponse
from ..types.page_retrieve_response import PageRetrieveResponse

__all__ = ["PagesResource", "AsyncPagesResource"]


class PagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vibedropper-python#accessing-raw-response-data-eg-headers
        """
        return PagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vibedropper-python#with_streaming_response
        """
        return PagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        page_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageRetrieveResponse:
        """
        Get a page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return self._get(
            f"/pages/{page_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageRetrieveResponse,
        )

    def update(
        self,
        page_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        status: Literal["DRAFT", "ACTIVE", "ENDED", "ARCHIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageUpdateResponse:
        """
        Update a page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return self._put(
            f"/pages/{page_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "status": status,
                },
                page_update_params.PageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        status: Literal["DRAFT", "ACTIVE", "ENDED", "ARCHIVED", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageListResponse:
        """List pages

        Args:
          status: Filter by status.

        Omit or use "all" to return all pages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/pages",
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
                    page_list_params.PageListParams,
                ),
            ),
            cast_to=PageListResponse,
        )

    def delete(
        self,
        page_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageDeleteResponse:
        """
        Delete a page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return self._delete(
            f"/pages/{page_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageDeleteResponse,
        )


class AsyncPagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vibedropper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vibedropper-python#with_streaming_response
        """
        return AsyncPagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        page_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageRetrieveResponse:
        """
        Get a page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return await self._get(
            f"/pages/{page_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageRetrieveResponse,
        )

    async def update(
        self,
        page_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        status: Literal["DRAFT", "ACTIVE", "ENDED", "ARCHIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageUpdateResponse:
        """
        Update a page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return await self._put(
            f"/pages/{page_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "status": status,
                },
                page_update_params.PageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageUpdateResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        status: Literal["DRAFT", "ACTIVE", "ENDED", "ARCHIVED", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageListResponse:
        """List pages

        Args:
          status: Filter by status.

        Omit or use "all" to return all pages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/pages",
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
                    page_list_params.PageListParams,
                ),
            ),
            cast_to=PageListResponse,
        )

    async def delete(
        self,
        page_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageDeleteResponse:
        """
        Delete a page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return await self._delete(
            f"/pages/{page_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageDeleteResponse,
        )


class PagesResourceWithRawResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.retrieve = to_raw_response_wrapper(
            pages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pages.update,
        )
        self.list = to_raw_response_wrapper(
            pages.list,
        )
        self.delete = to_raw_response_wrapper(
            pages.delete,
        )


class AsyncPagesResourceWithRawResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.retrieve = async_to_raw_response_wrapper(
            pages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pages.update,
        )
        self.list = async_to_raw_response_wrapper(
            pages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pages.delete,
        )


class PagesResourceWithStreamingResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.retrieve = to_streamed_response_wrapper(
            pages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pages.update,
        )
        self.list = to_streamed_response_wrapper(
            pages.list,
        )
        self.delete = to_streamed_response_wrapper(
            pages.delete,
        )


class AsyncPagesResourceWithStreamingResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.retrieve = async_to_streamed_response_wrapper(
            pages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pages.delete,
        )
