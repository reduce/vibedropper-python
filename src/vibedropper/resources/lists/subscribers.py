# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.lists import subscriber_add_params
from ..._base_client import make_request_options
from ...types.lists.subscriber_add_response import SubscriberAddResponse
from ...types.lists.subscriber_list_response import SubscriberListResponse
from ...types.lists.subscriber_remove_response import SubscriberRemoveResponse

__all__ = ["SubscribersResource", "AsyncSubscribersResource"]


class SubscribersResource(SyncAPIResource):
    """Manage list subscribers"""

    @cached_property
    def with_raw_response(self) -> SubscribersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reduce/vibedropper-python#accessing-raw-response-data-eg-headers
        """
        return SubscribersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscribersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reduce/vibedropper-python#with_streaming_response
        """
        return SubscribersResourceWithStreamingResponse(self)

    def list(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriberListResponse:
        """
        Returns all subscribers for the list ordered by subscribe date descending.
        Includes linked customer data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get(
            f"/lists/{list_id}/subscribers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriberListResponse,
        )

    def add(
        self,
        list_id: str,
        *,
        email: str,
        custom_fields: object | Omit = omit,
        name: str | Omit = omit,
        pickup_location_id: str | Omit = omit,
        region_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriberAddResponse:
        """
        Creates or updates the matching customer record and adds a subscriber entry.
        Returns 400 with code `duplicate` if already subscribed.

        Args:
          custom_fields: Arbitrary key-value metadata

          pickup_location_id: Pickup location ID (must belong to the given regionId)

          region_id: Region ID to assign to the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._post(
            f"/lists/{list_id}/subscribers",
            body=maybe_transform(
                {
                    "email": email,
                    "custom_fields": custom_fields,
                    "name": name,
                    "pickup_location_id": pickup_location_id,
                    "region_id": region_id,
                },
                subscriber_add_params.SubscriberAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriberAddResponse,
        )

    def remove(
        self,
        subscriber_id: str,
        *,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriberRemoveResponse:
        """
        Remove a subscriber from a list

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not subscriber_id:
            raise ValueError(f"Expected a non-empty value for `subscriber_id` but received {subscriber_id!r}")
        return self._delete(
            f"/lists/{list_id}/subscribers/{subscriber_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriberRemoveResponse,
        )


class AsyncSubscribersResource(AsyncAPIResource):
    """Manage list subscribers"""

    @cached_property
    def with_raw_response(self) -> AsyncSubscribersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reduce/vibedropper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscribersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscribersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reduce/vibedropper-python#with_streaming_response
        """
        return AsyncSubscribersResourceWithStreamingResponse(self)

    async def list(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriberListResponse:
        """
        Returns all subscribers for the list ordered by subscribe date descending.
        Includes linked customer data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._get(
            f"/lists/{list_id}/subscribers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriberListResponse,
        )

    async def add(
        self,
        list_id: str,
        *,
        email: str,
        custom_fields: object | Omit = omit,
        name: str | Omit = omit,
        pickup_location_id: str | Omit = omit,
        region_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriberAddResponse:
        """
        Creates or updates the matching customer record and adds a subscriber entry.
        Returns 400 with code `duplicate` if already subscribed.

        Args:
          custom_fields: Arbitrary key-value metadata

          pickup_location_id: Pickup location ID (must belong to the given regionId)

          region_id: Region ID to assign to the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._post(
            f"/lists/{list_id}/subscribers",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "custom_fields": custom_fields,
                    "name": name,
                    "pickup_location_id": pickup_location_id,
                    "region_id": region_id,
                },
                subscriber_add_params.SubscriberAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriberAddResponse,
        )

    async def remove(
        self,
        subscriber_id: str,
        *,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriberRemoveResponse:
        """
        Remove a subscriber from a list

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not subscriber_id:
            raise ValueError(f"Expected a non-empty value for `subscriber_id` but received {subscriber_id!r}")
        return await self._delete(
            f"/lists/{list_id}/subscribers/{subscriber_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriberRemoveResponse,
        )


class SubscribersResourceWithRawResponse:
    def __init__(self, subscribers: SubscribersResource) -> None:
        self._subscribers = subscribers

        self.list = to_raw_response_wrapper(
            subscribers.list,
        )
        self.add = to_raw_response_wrapper(
            subscribers.add,
        )
        self.remove = to_raw_response_wrapper(
            subscribers.remove,
        )


class AsyncSubscribersResourceWithRawResponse:
    def __init__(self, subscribers: AsyncSubscribersResource) -> None:
        self._subscribers = subscribers

        self.list = async_to_raw_response_wrapper(
            subscribers.list,
        )
        self.add = async_to_raw_response_wrapper(
            subscribers.add,
        )
        self.remove = async_to_raw_response_wrapper(
            subscribers.remove,
        )


class SubscribersResourceWithStreamingResponse:
    def __init__(self, subscribers: SubscribersResource) -> None:
        self._subscribers = subscribers

        self.list = to_streamed_response_wrapper(
            subscribers.list,
        )
        self.add = to_streamed_response_wrapper(
            subscribers.add,
        )
        self.remove = to_streamed_response_wrapper(
            subscribers.remove,
        )


class AsyncSubscribersResourceWithStreamingResponse:
    def __init__(self, subscribers: AsyncSubscribersResource) -> None:
        self._subscribers = subscribers

        self.list = async_to_streamed_response_wrapper(
            subscribers.list,
        )
        self.add = async_to_streamed_response_wrapper(
            subscribers.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            subscribers.remove,
        )
