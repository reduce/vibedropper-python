# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import list_list_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .subscribers import (
    SubscribersResource,
    AsyncSubscribersResource,
    SubscribersResourceWithRawResponse,
    AsyncSubscribersResourceWithRawResponse,
    SubscribersResourceWithStreamingResponse,
    AsyncSubscribersResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.list_list_response import ListListResponse
from ...types.list_retrieve_response import ListRetrieveResponse

__all__ = ["ListsResource", "AsyncListsResource"]


class ListsResource(SyncAPIResource):
    """Manage subscriber lists"""

    @cached_property
    def subscribers(self) -> SubscribersResource:
        """Manage list subscribers"""
        return SubscribersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reduce/vibedropper-python#accessing-raw-response-data-eg-headers
        """
        return ListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reduce/vibedropper-python#with_streaming_response
        """
        return ListsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListRetrieveResponse:
        """
        Get a list

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get(
            path_template("/lists/{list_id}", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListListResponse:
        """
        List lists

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/lists",
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
                    list_list_params.ListListParams,
                ),
            ),
            cast_to=ListListResponse,
        )


class AsyncListsResource(AsyncAPIResource):
    """Manage subscriber lists"""

    @cached_property
    def subscribers(self) -> AsyncSubscribersResource:
        """Manage list subscribers"""
        return AsyncSubscribersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reduce/vibedropper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reduce/vibedropper-python#with_streaming_response
        """
        return AsyncListsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListRetrieveResponse:
        """
        Get a list

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._get(
            path_template("/lists/{list_id}", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListRetrieveResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListListResponse:
        """
        List lists

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/lists",
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
                    list_list_params.ListListParams,
                ),
            ),
            cast_to=ListListResponse,
        )


class ListsResourceWithRawResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.retrieve = to_raw_response_wrapper(
            lists.retrieve,
        )
        self.list = to_raw_response_wrapper(
            lists.list,
        )

    @cached_property
    def subscribers(self) -> SubscribersResourceWithRawResponse:
        """Manage list subscribers"""
        return SubscribersResourceWithRawResponse(self._lists.subscribers)


class AsyncListsResourceWithRawResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.retrieve = async_to_raw_response_wrapper(
            lists.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            lists.list,
        )

    @cached_property
    def subscribers(self) -> AsyncSubscribersResourceWithRawResponse:
        """Manage list subscribers"""
        return AsyncSubscribersResourceWithRawResponse(self._lists.subscribers)


class ListsResourceWithStreamingResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.retrieve = to_streamed_response_wrapper(
            lists.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            lists.list,
        )

    @cached_property
    def subscribers(self) -> SubscribersResourceWithStreamingResponse:
        """Manage list subscribers"""
        return SubscribersResourceWithStreamingResponse(self._lists.subscribers)


class AsyncListsResourceWithStreamingResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.retrieve = async_to_streamed_response_wrapper(
            lists.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            lists.list,
        )

    @cached_property
    def subscribers(self) -> AsyncSubscribersResourceWithStreamingResponse:
        """Manage list subscribers"""
        return AsyncSubscribersResourceWithStreamingResponse(self._lists.subscribers)
