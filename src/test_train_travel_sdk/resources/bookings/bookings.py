# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import booking_list_params, booking_create_params, booking_payment_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.booking import Booking
from ...types.booking_list_response import BookingListResponse
from ...types.bookings.booking_payment import BookingPayment

__all__ = ["BookingsResource", "AsyncBookingsResource"]


class BookingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BookingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ChristopheDujarric/test-train-travel-sdk#accessing-raw-response-data-eg-headers
        """
        return BookingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BookingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ChristopheDujarric/test-train-travel-sdk#with_streaming_response
        """
        return BookingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        has_bicycle: bool | NotGiven = NOT_GIVEN,
        has_dog: bool | NotGiven = NOT_GIVEN,
        passenger_name: str | NotGiven = NOT_GIVEN,
        trip_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Booking:
        """A booking is a temporary hold on a trip.

        It is not confirmed until the payment
        is processed.

        Args:
          has_bicycle: Indicates whether the passenger has a bicycle.

          has_dog: Indicates whether the passenger has a dog.

          passenger_name: Name of the passenger

          trip_id: Identifier of the booked trip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/bookings",
            body=maybe_transform(
                {
                    "has_bicycle": has_bicycle,
                    "has_dog": has_dog,
                    "passenger_name": passenger_name,
                    "trip_id": trip_id,
                },
                booking_create_params.BookingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Booking,
        )

    def retrieve(
        self,
        booking_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Booking:
        """
        Returns the details of a specific booking.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not booking_id:
            raise ValueError(f"Expected a non-empty value for `booking_id` but received {booking_id!r}")
        return self._get(
            f"/bookings/{booking_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Booking,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookingListResponse:
        """
        Returns a list of all trip bookings by the authenticated user.

        Args:
          limit: The number of items to return per page

          page: The page number to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/bookings",
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
                    booking_list_params.BookingListParams,
                ),
            ),
            cast_to=BookingListResponse,
        )

    def delete(
        self,
        booking_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a booking, cancelling the hold on the trip.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not booking_id:
            raise ValueError(f"Expected a non-empty value for `booking_id` but received {booking_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/bookings/{booking_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def payment(
        self,
        booking_id: str,
        *,
        amount: float | NotGiven = NOT_GIVEN,
        currency: Literal["bam", "bgn", "chf", "eur", "gbp", "nok", "sek", "try"] | NotGiven = NOT_GIVEN,
        source: booking_payment_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookingPayment:
        """
        A payment is an attempt to pay for the booking, which will confirm the booking
        for the user and enable them to get their tickets.

        Args:
          amount: Amount intended to be collected by this payment. A positive decimal figure
              describing the amount to be collected.

          currency: Three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
              lowercase.

          source: The payment source to take the payment from. This can be a card or a bank
              account. Some of these properties will be hidden on read to protect PII leaking.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not booking_id:
            raise ValueError(f"Expected a non-empty value for `booking_id` but received {booking_id!r}")
        return self._post(
            f"/bookings/{booking_id}/payment",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "source": source,
                },
                booking_payment_params.BookingPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookingPayment,
        )


class AsyncBookingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBookingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ChristopheDujarric/test-train-travel-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBookingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBookingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ChristopheDujarric/test-train-travel-sdk#with_streaming_response
        """
        return AsyncBookingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        has_bicycle: bool | NotGiven = NOT_GIVEN,
        has_dog: bool | NotGiven = NOT_GIVEN,
        passenger_name: str | NotGiven = NOT_GIVEN,
        trip_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Booking:
        """A booking is a temporary hold on a trip.

        It is not confirmed until the payment
        is processed.

        Args:
          has_bicycle: Indicates whether the passenger has a bicycle.

          has_dog: Indicates whether the passenger has a dog.

          passenger_name: Name of the passenger

          trip_id: Identifier of the booked trip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/bookings",
            body=await async_maybe_transform(
                {
                    "has_bicycle": has_bicycle,
                    "has_dog": has_dog,
                    "passenger_name": passenger_name,
                    "trip_id": trip_id,
                },
                booking_create_params.BookingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Booking,
        )

    async def retrieve(
        self,
        booking_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Booking:
        """
        Returns the details of a specific booking.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not booking_id:
            raise ValueError(f"Expected a non-empty value for `booking_id` but received {booking_id!r}")
        return await self._get(
            f"/bookings/{booking_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Booking,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookingListResponse:
        """
        Returns a list of all trip bookings by the authenticated user.

        Args:
          limit: The number of items to return per page

          page: The page number to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/bookings",
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
                    booking_list_params.BookingListParams,
                ),
            ),
            cast_to=BookingListResponse,
        )

    async def delete(
        self,
        booking_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a booking, cancelling the hold on the trip.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not booking_id:
            raise ValueError(f"Expected a non-empty value for `booking_id` but received {booking_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/bookings/{booking_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def payment(
        self,
        booking_id: str,
        *,
        amount: float | NotGiven = NOT_GIVEN,
        currency: Literal["bam", "bgn", "chf", "eur", "gbp", "nok", "sek", "try"] | NotGiven = NOT_GIVEN,
        source: booking_payment_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookingPayment:
        """
        A payment is an attempt to pay for the booking, which will confirm the booking
        for the user and enable them to get their tickets.

        Args:
          amount: Amount intended to be collected by this payment. A positive decimal figure
              describing the amount to be collected.

          currency: Three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
              lowercase.

          source: The payment source to take the payment from. This can be a card or a bank
              account. Some of these properties will be hidden on read to protect PII leaking.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not booking_id:
            raise ValueError(f"Expected a non-empty value for `booking_id` but received {booking_id!r}")
        return await self._post(
            f"/bookings/{booking_id}/payment",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "source": source,
                },
                booking_payment_params.BookingPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookingPayment,
        )


class BookingsResourceWithRawResponse:
    def __init__(self, bookings: BookingsResource) -> None:
        self._bookings = bookings

        self.create = to_raw_response_wrapper(
            bookings.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bookings.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bookings.list,
        )
        self.delete = to_raw_response_wrapper(
            bookings.delete,
        )
        self.payment = to_raw_response_wrapper(
            bookings.payment,
        )


class AsyncBookingsResourceWithRawResponse:
    def __init__(self, bookings: AsyncBookingsResource) -> None:
        self._bookings = bookings

        self.create = async_to_raw_response_wrapper(
            bookings.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bookings.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bookings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bookings.delete,
        )
        self.payment = async_to_raw_response_wrapper(
            bookings.payment,
        )


class BookingsResourceWithStreamingResponse:
    def __init__(self, bookings: BookingsResource) -> None:
        self._bookings = bookings

        self.create = to_streamed_response_wrapper(
            bookings.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bookings.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bookings.list,
        )
        self.delete = to_streamed_response_wrapper(
            bookings.delete,
        )
        self.payment = to_streamed_response_wrapper(
            bookings.payment,
        )


class AsyncBookingsResourceWithStreamingResponse:
    def __init__(self, bookings: AsyncBookingsResource) -> None:
        self._bookings = bookings

        self.create = async_to_streamed_response_wrapper(
            bookings.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bookings.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bookings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bookings.delete,
        )
        self.payment = async_to_streamed_response_wrapper(
            bookings.payment,
        )
