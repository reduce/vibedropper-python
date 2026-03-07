# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, VibedropperError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import forms, lists, pages, campaigns, customers, knowledge_bases
    from .resources.forms import FormsResource, AsyncFormsResource
    from .resources.pages import PagesResource, AsyncPagesResource
    from .resources.campaigns import CampaignsResource, AsyncCampaignsResource
    from .resources.customers import CustomersResource, AsyncCustomersResource
    from .resources.lists.lists import ListsResource, AsyncListsResource
    from .resources.knowledge_bases.knowledge_bases import KnowledgeBasesResource, AsyncKnowledgeBasesResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Vibedropper",
    "AsyncVibedropper",
    "Client",
    "AsyncClient",
]


class Vibedropper(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Vibedropper client instance.

        This automatically infers the `api_key` argument from the `VIBEDROPPER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("VIBEDROPPER_API_KEY")
        if api_key is None:
            raise VibedropperError(
                "The api_key client option must be set either by passing api_key to the client or by setting the VIBEDROPPER_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("VIBEDROPPER_BASE_URL")
        if base_url is None:
            base_url = f"https://vibedropper.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def lists(self) -> ListsResource:
        """Manage subscriber lists"""
        from .resources.lists import ListsResource

        return ListsResource(self)

    @cached_property
    def customers(self) -> CustomersResource:
        """Manage customers"""
        from .resources.customers import CustomersResource

        return CustomersResource(self)

    @cached_property
    def campaigns(self) -> CampaignsResource:
        """Access email campaigns (read-only)"""
        from .resources.campaigns import CampaignsResource

        return CampaignsResource(self)

    @cached_property
    def forms(self) -> FormsResource:
        """Manage forms and submissions"""
        from .resources.forms import FormsResource

        return FormsResource(self)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResource:
        """Manage knowledge bases and articles"""
        from .resources.knowledge_bases import KnowledgeBasesResource

        return KnowledgeBasesResource(self)

    @cached_property
    def pages(self) -> PagesResource:
        """Manage landing pages"""
        from .resources.pages import PagesResource

        return PagesResource(self)

    @cached_property
    def with_raw_response(self) -> VibedropperWithRawResponse:
        return VibedropperWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VibedropperWithStreamedResponse:
        return VibedropperWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncVibedropper(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncVibedropper client instance.

        This automatically infers the `api_key` argument from the `VIBEDROPPER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("VIBEDROPPER_API_KEY")
        if api_key is None:
            raise VibedropperError(
                "The api_key client option must be set either by passing api_key to the client or by setting the VIBEDROPPER_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("VIBEDROPPER_BASE_URL")
        if base_url is None:
            base_url = f"https://vibedropper.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def lists(self) -> AsyncListsResource:
        """Manage subscriber lists"""
        from .resources.lists import AsyncListsResource

        return AsyncListsResource(self)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        """Manage customers"""
        from .resources.customers import AsyncCustomersResource

        return AsyncCustomersResource(self)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResource:
        """Access email campaigns (read-only)"""
        from .resources.campaigns import AsyncCampaignsResource

        return AsyncCampaignsResource(self)

    @cached_property
    def forms(self) -> AsyncFormsResource:
        """Manage forms and submissions"""
        from .resources.forms import AsyncFormsResource

        return AsyncFormsResource(self)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResource:
        """Manage knowledge bases and articles"""
        from .resources.knowledge_bases import AsyncKnowledgeBasesResource

        return AsyncKnowledgeBasesResource(self)

    @cached_property
    def pages(self) -> AsyncPagesResource:
        """Manage landing pages"""
        from .resources.pages import AsyncPagesResource

        return AsyncPagesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncVibedropperWithRawResponse:
        return AsyncVibedropperWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVibedropperWithStreamedResponse:
        return AsyncVibedropperWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class VibedropperWithRawResponse:
    _client: Vibedropper

    def __init__(self, client: Vibedropper) -> None:
        self._client = client

    @cached_property
    def lists(self) -> lists.ListsResourceWithRawResponse:
        """Manage subscriber lists"""
        from .resources.lists import ListsResourceWithRawResponse

        return ListsResourceWithRawResponse(self._client.lists)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithRawResponse:
        """Manage customers"""
        from .resources.customers import CustomersResourceWithRawResponse

        return CustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def campaigns(self) -> campaigns.CampaignsResourceWithRawResponse:
        """Access email campaigns (read-only)"""
        from .resources.campaigns import CampaignsResourceWithRawResponse

        return CampaignsResourceWithRawResponse(self._client.campaigns)

    @cached_property
    def forms(self) -> forms.FormsResourceWithRawResponse:
        """Manage forms and submissions"""
        from .resources.forms import FormsResourceWithRawResponse

        return FormsResourceWithRawResponse(self._client.forms)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.KnowledgeBasesResourceWithRawResponse:
        """Manage knowledge bases and articles"""
        from .resources.knowledge_bases import KnowledgeBasesResourceWithRawResponse

        return KnowledgeBasesResourceWithRawResponse(self._client.knowledge_bases)

    @cached_property
    def pages(self) -> pages.PagesResourceWithRawResponse:
        """Manage landing pages"""
        from .resources.pages import PagesResourceWithRawResponse

        return PagesResourceWithRawResponse(self._client.pages)


class AsyncVibedropperWithRawResponse:
    _client: AsyncVibedropper

    def __init__(self, client: AsyncVibedropper) -> None:
        self._client = client

    @cached_property
    def lists(self) -> lists.AsyncListsResourceWithRawResponse:
        """Manage subscriber lists"""
        from .resources.lists import AsyncListsResourceWithRawResponse

        return AsyncListsResourceWithRawResponse(self._client.lists)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithRawResponse:
        """Manage customers"""
        from .resources.customers import AsyncCustomersResourceWithRawResponse

        return AsyncCustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def campaigns(self) -> campaigns.AsyncCampaignsResourceWithRawResponse:
        """Access email campaigns (read-only)"""
        from .resources.campaigns import AsyncCampaignsResourceWithRawResponse

        return AsyncCampaignsResourceWithRawResponse(self._client.campaigns)

    @cached_property
    def forms(self) -> forms.AsyncFormsResourceWithRawResponse:
        """Manage forms and submissions"""
        from .resources.forms import AsyncFormsResourceWithRawResponse

        return AsyncFormsResourceWithRawResponse(self._client.forms)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.AsyncKnowledgeBasesResourceWithRawResponse:
        """Manage knowledge bases and articles"""
        from .resources.knowledge_bases import AsyncKnowledgeBasesResourceWithRawResponse

        return AsyncKnowledgeBasesResourceWithRawResponse(self._client.knowledge_bases)

    @cached_property
    def pages(self) -> pages.AsyncPagesResourceWithRawResponse:
        """Manage landing pages"""
        from .resources.pages import AsyncPagesResourceWithRawResponse

        return AsyncPagesResourceWithRawResponse(self._client.pages)


class VibedropperWithStreamedResponse:
    _client: Vibedropper

    def __init__(self, client: Vibedropper) -> None:
        self._client = client

    @cached_property
    def lists(self) -> lists.ListsResourceWithStreamingResponse:
        """Manage subscriber lists"""
        from .resources.lists import ListsResourceWithStreamingResponse

        return ListsResourceWithStreamingResponse(self._client.lists)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithStreamingResponse:
        """Manage customers"""
        from .resources.customers import CustomersResourceWithStreamingResponse

        return CustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def campaigns(self) -> campaigns.CampaignsResourceWithStreamingResponse:
        """Access email campaigns (read-only)"""
        from .resources.campaigns import CampaignsResourceWithStreamingResponse

        return CampaignsResourceWithStreamingResponse(self._client.campaigns)

    @cached_property
    def forms(self) -> forms.FormsResourceWithStreamingResponse:
        """Manage forms and submissions"""
        from .resources.forms import FormsResourceWithStreamingResponse

        return FormsResourceWithStreamingResponse(self._client.forms)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.KnowledgeBasesResourceWithStreamingResponse:
        """Manage knowledge bases and articles"""
        from .resources.knowledge_bases import KnowledgeBasesResourceWithStreamingResponse

        return KnowledgeBasesResourceWithStreamingResponse(self._client.knowledge_bases)

    @cached_property
    def pages(self) -> pages.PagesResourceWithStreamingResponse:
        """Manage landing pages"""
        from .resources.pages import PagesResourceWithStreamingResponse

        return PagesResourceWithStreamingResponse(self._client.pages)


class AsyncVibedropperWithStreamedResponse:
    _client: AsyncVibedropper

    def __init__(self, client: AsyncVibedropper) -> None:
        self._client = client

    @cached_property
    def lists(self) -> lists.AsyncListsResourceWithStreamingResponse:
        """Manage subscriber lists"""
        from .resources.lists import AsyncListsResourceWithStreamingResponse

        return AsyncListsResourceWithStreamingResponse(self._client.lists)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithStreamingResponse:
        """Manage customers"""
        from .resources.customers import AsyncCustomersResourceWithStreamingResponse

        return AsyncCustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def campaigns(self) -> campaigns.AsyncCampaignsResourceWithStreamingResponse:
        """Access email campaigns (read-only)"""
        from .resources.campaigns import AsyncCampaignsResourceWithStreamingResponse

        return AsyncCampaignsResourceWithStreamingResponse(self._client.campaigns)

    @cached_property
    def forms(self) -> forms.AsyncFormsResourceWithStreamingResponse:
        """Manage forms and submissions"""
        from .resources.forms import AsyncFormsResourceWithStreamingResponse

        return AsyncFormsResourceWithStreamingResponse(self._client.forms)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.AsyncKnowledgeBasesResourceWithStreamingResponse:
        """Manage knowledge bases and articles"""
        from .resources.knowledge_bases import AsyncKnowledgeBasesResourceWithStreamingResponse

        return AsyncKnowledgeBasesResourceWithStreamingResponse(self._client.knowledge_bases)

    @cached_property
    def pages(self) -> pages.AsyncPagesResourceWithStreamingResponse:
        """Manage landing pages"""
        from .resources.pages import AsyncPagesResourceWithStreamingResponse

        return AsyncPagesResourceWithStreamingResponse(self._client.pages)


Client = Vibedropper

AsyncClient = AsyncVibedropper
