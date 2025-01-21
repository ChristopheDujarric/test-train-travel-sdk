# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import trips, stations
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TestTrainTravelSDKError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.bookings import bookings

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "TestTrainTravelSDK",
    "AsyncTestTrainTravelSDK",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.example.com",
    "environment_1": "https://try.microcks.io/rest/Train+Travel+API/1.0.0",
}


class TestTrainTravelSDK(SyncAPIClient):
    __test__ = False
    stations: stations.StationsResource
    trips: trips.TripsResource
    bookings: bookings.BookingsResource
    with_raw_response: TestTrainTravelSDKWithRawResponse
    with_streaming_response: TestTrainTravelSDKWithStreamedResponse

    # client options
    client_id: str
    client_secret: str
    authorization_code: str | None
    access_token: str | None
    refresh_token: str | None

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        authorization_code: str | None = None,
        access_token: str | None = None,
        refresh_token: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new synchronous test-train-travel-sdk client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `client_id` from `OAUTH2_CLIENT_ID`
        - `client_secret` from `OAUTH2_CLIENT_SECRET`
        - `authorization_code` from `OAUTH2_AUTHORIZATION_CODE`
        - `access_token` from `OAUTH2_ACCESS_TOKEN`
        - `refresh_token` from `OAUTH2_REFRESH_TOKEN`
        """
        if client_id is None:
            client_id = os.environ.get("OAUTH2_CLIENT_ID")
        if client_id is None:
            raise TestTrainTravelSDKError(
                "The client_id client option must be set either by passing client_id to the client or by setting the OAUTH2_CLIENT_ID environment variable"
            )
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("OAUTH2_CLIENT_SECRET")
        if client_secret is None:
            raise TestTrainTravelSDKError(
                "The client_secret client option must be set either by passing client_secret to the client or by setting the OAUTH2_CLIENT_SECRET environment variable"
            )
        self.client_secret = client_secret

        if authorization_code is None:
            authorization_code = os.environ.get("OAUTH2_AUTHORIZATION_CODE")
        self.authorization_code = authorization_code

        if access_token is None:
            access_token = os.environ.get("OAUTH2_ACCESS_TOKEN")
        self.access_token = access_token

        if refresh_token is None:
            refresh_token = os.environ.get("OAUTH2_REFRESH_TOKEN")
        self.refresh_token = refresh_token

        self._environment = environment

        base_url_env = os.environ.get("TEST_TRAIN_TRAVEL_SDK_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TEST_TRAIN_TRAVEL_SDK_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

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

        self.stations = stations.StationsResource(self)
        self.trips = trips.TripsResource(self)
        self.bookings = bookings.BookingsResource(self)
        self.with_raw_response = TestTrainTravelSDKWithRawResponse(self)
        self.with_streaming_response = TestTrainTravelSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

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
        client_id: str | None = None,
        client_secret: str | None = None,
        authorization_code: str | None = None,
        access_token: str | None = None,
        refresh_token: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            authorization_code=authorization_code or self.authorization_code,
            access_token=access_token or self.access_token,
            refresh_token=refresh_token or self.refresh_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
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


class AsyncTestTrainTravelSDK(AsyncAPIClient):
    stations: stations.AsyncStationsResource
    trips: trips.AsyncTripsResource
    bookings: bookings.AsyncBookingsResource
    with_raw_response: AsyncTestTrainTravelSDKWithRawResponse
    with_streaming_response: AsyncTestTrainTravelSDKWithStreamedResponse

    # client options
    client_id: str
    client_secret: str
    authorization_code: str | None
    access_token: str | None
    refresh_token: str | None

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        authorization_code: str | None = None,
        access_token: str | None = None,
        refresh_token: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new async test-train-travel-sdk client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `client_id` from `OAUTH2_CLIENT_ID`
        - `client_secret` from `OAUTH2_CLIENT_SECRET`
        - `authorization_code` from `OAUTH2_AUTHORIZATION_CODE`
        - `access_token` from `OAUTH2_ACCESS_TOKEN`
        - `refresh_token` from `OAUTH2_REFRESH_TOKEN`
        """
        if client_id is None:
            client_id = os.environ.get("OAUTH2_CLIENT_ID")
        if client_id is None:
            raise TestTrainTravelSDKError(
                "The client_id client option must be set either by passing client_id to the client or by setting the OAUTH2_CLIENT_ID environment variable"
            )
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("OAUTH2_CLIENT_SECRET")
        if client_secret is None:
            raise TestTrainTravelSDKError(
                "The client_secret client option must be set either by passing client_secret to the client or by setting the OAUTH2_CLIENT_SECRET environment variable"
            )
        self.client_secret = client_secret

        if authorization_code is None:
            authorization_code = os.environ.get("OAUTH2_AUTHORIZATION_CODE")
        self.authorization_code = authorization_code

        if access_token is None:
            access_token = os.environ.get("OAUTH2_ACCESS_TOKEN")
        self.access_token = access_token

        if refresh_token is None:
            refresh_token = os.environ.get("OAUTH2_REFRESH_TOKEN")
        self.refresh_token = refresh_token

        self._environment = environment

        base_url_env = os.environ.get("TEST_TRAIN_TRAVEL_SDK_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TEST_TRAIN_TRAVEL_SDK_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

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

        self.stations = stations.AsyncStationsResource(self)
        self.trips = trips.AsyncTripsResource(self)
        self.bookings = bookings.AsyncBookingsResource(self)
        self.with_raw_response = AsyncTestTrainTravelSDKWithRawResponse(self)
        self.with_streaming_response = AsyncTestTrainTravelSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

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
        client_id: str | None = None,
        client_secret: str | None = None,
        authorization_code: str | None = None,
        access_token: str | None = None,
        refresh_token: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            authorization_code=authorization_code or self.authorization_code,
            access_token=access_token or self.access_token,
            refresh_token=refresh_token or self.refresh_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
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


class TestTrainTravelSDKWithRawResponse:
    __test__ = False

    def __init__(self, client: TestTrainTravelSDK) -> None:
        self.stations = stations.StationsResourceWithRawResponse(client.stations)
        self.trips = trips.TripsResourceWithRawResponse(client.trips)
        self.bookings = bookings.BookingsResourceWithRawResponse(client.bookings)


class AsyncTestTrainTravelSDKWithRawResponse:
    def __init__(self, client: AsyncTestTrainTravelSDK) -> None:
        self.stations = stations.AsyncStationsResourceWithRawResponse(client.stations)
        self.trips = trips.AsyncTripsResourceWithRawResponse(client.trips)
        self.bookings = bookings.AsyncBookingsResourceWithRawResponse(client.bookings)


class TestTrainTravelSDKWithStreamedResponse:
    __test__ = False

    def __init__(self, client: TestTrainTravelSDK) -> None:
        self.stations = stations.StationsResourceWithStreamingResponse(client.stations)
        self.trips = trips.TripsResourceWithStreamingResponse(client.trips)
        self.bookings = bookings.BookingsResourceWithStreamingResponse(client.bookings)


class AsyncTestTrainTravelSDKWithStreamedResponse:
    def __init__(self, client: AsyncTestTrainTravelSDK) -> None:
        self.stations = stations.AsyncStationsResourceWithStreamingResponse(client.stations)
        self.trips = trips.AsyncTripsResourceWithStreamingResponse(client.trips)
        self.bookings = bookings.AsyncBookingsResourceWithStreamingResponse(client.bookings)


Client = TestTrainTravelSDK

AsyncClient = AsyncTestTrainTravelSDK
