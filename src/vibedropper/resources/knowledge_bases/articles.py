# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ..._base_client import make_request_options
from ...types.knowledge_bases import article_list_params, article_create_params
from ...types.knowledge_bases.article_list_response import ArticleListResponse
from ...types.knowledge_bases.article_create_response import ArticleCreateResponse

__all__ = ["ArticlesResource", "AsyncArticlesResource"]


class ArticlesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArticlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reduce/vibedropper-python#accessing-raw-response-data-eg-headers
        """
        return ArticlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArticlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reduce/vibedropper-python#with_streaming_response
        """
        return ArticlesResourceWithStreamingResponse(self)

    def create(
        self,
        kb_id: str,
        *,
        title: str,
        category_id: Optional[str] | Omit = omit,
        content: str | Omit = omit,
        excerpt: Optional[str] | Omit = omit,
        published: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleCreateResponse:
        """
        Create an article

        Args:
          content: HTML content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not kb_id:
            raise ValueError(f"Expected a non-empty value for `kb_id` but received {kb_id!r}")
        return self._post(
            f"/knowledge-bases/{kb_id}/articles",
            body=maybe_transform(
                {
                    "title": title,
                    "category_id": category_id,
                    "content": content,
                    "excerpt": excerpt,
                    "published": published,
                },
                article_create_params.ArticleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleCreateResponse,
        )

    def list(
        self,
        kb_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleListResponse:
        """
        List articles in a knowledge base

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not kb_id:
            raise ValueError(f"Expected a non-empty value for `kb_id` but received {kb_id!r}")
        return self._get(
            f"/knowledge-bases/{kb_id}/articles",
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
                    article_list_params.ArticleListParams,
                ),
            ),
            cast_to=ArticleListResponse,
        )


class AsyncArticlesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArticlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reduce/vibedropper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArticlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArticlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reduce/vibedropper-python#with_streaming_response
        """
        return AsyncArticlesResourceWithStreamingResponse(self)

    async def create(
        self,
        kb_id: str,
        *,
        title: str,
        category_id: Optional[str] | Omit = omit,
        content: str | Omit = omit,
        excerpt: Optional[str] | Omit = omit,
        published: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleCreateResponse:
        """
        Create an article

        Args:
          content: HTML content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not kb_id:
            raise ValueError(f"Expected a non-empty value for `kb_id` but received {kb_id!r}")
        return await self._post(
            f"/knowledge-bases/{kb_id}/articles",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "category_id": category_id,
                    "content": content,
                    "excerpt": excerpt,
                    "published": published,
                },
                article_create_params.ArticleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleCreateResponse,
        )

    async def list(
        self,
        kb_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleListResponse:
        """
        List articles in a knowledge base

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not kb_id:
            raise ValueError(f"Expected a non-empty value for `kb_id` but received {kb_id!r}")
        return await self._get(
            f"/knowledge-bases/{kb_id}/articles",
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
                    article_list_params.ArticleListParams,
                ),
            ),
            cast_to=ArticleListResponse,
        )


class ArticlesResourceWithRawResponse:
    def __init__(self, articles: ArticlesResource) -> None:
        self._articles = articles

        self.create = to_raw_response_wrapper(
            articles.create,
        )
        self.list = to_raw_response_wrapper(
            articles.list,
        )


class AsyncArticlesResourceWithRawResponse:
    def __init__(self, articles: AsyncArticlesResource) -> None:
        self._articles = articles

        self.create = async_to_raw_response_wrapper(
            articles.create,
        )
        self.list = async_to_raw_response_wrapper(
            articles.list,
        )


class ArticlesResourceWithStreamingResponse:
    def __init__(self, articles: ArticlesResource) -> None:
        self._articles = articles

        self.create = to_streamed_response_wrapper(
            articles.create,
        )
        self.list = to_streamed_response_wrapper(
            articles.list,
        )


class AsyncArticlesResourceWithStreamingResponse:
    def __init__(self, articles: AsyncArticlesResource) -> None:
        self._articles = articles

        self.create = async_to_streamed_response_wrapper(
            articles.create,
        )
        self.list = async_to_streamed_response_wrapper(
            articles.list,
        )
