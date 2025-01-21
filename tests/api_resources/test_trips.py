# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from test_train_travel_sdk import TestTrainTravelSDK, AsyncTestTrainTravelSDK
from test_train_travel_sdk.types import TripListResponse
from test_train_travel_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrips:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TestTrainTravelSDK) -> None:
        trip = client.trips.list(
            bicycles=True,
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TripListResponse, trip, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TestTrainTravelSDK) -> None:
        trip = client.trips.list(
            bicycles=True,
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dogs=True,
            limit=1,
            page=1,
        )
        assert_matches_type(TripListResponse, trip, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TestTrainTravelSDK) -> None:
        response = client.trips.with_raw_response.list(
            bicycles=True,
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trip = response.parse()
        assert_matches_type(TripListResponse, trip, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TestTrainTravelSDK) -> None:
        with client.trips.with_streaming_response.list(
            bicycles=True,
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trip = response.parse()
            assert_matches_type(TripListResponse, trip, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrips:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTestTrainTravelSDK) -> None:
        trip = await async_client.trips.list(
            bicycles=True,
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TripListResponse, trip, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTestTrainTravelSDK) -> None:
        trip = await async_client.trips.list(
            bicycles=True,
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dogs=True,
            limit=1,
            page=1,
        )
        assert_matches_type(TripListResponse, trip, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTestTrainTravelSDK) -> None:
        response = await async_client.trips.with_raw_response.list(
            bicycles=True,
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trip = await response.parse()
        assert_matches_type(TripListResponse, trip, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTestTrainTravelSDK) -> None:
        async with async_client.trips.with_streaming_response.list(
            bicycles=True,
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trip = await response.parse()
            assert_matches_type(TripListResponse, trip, path=["response"])

        assert cast(Any, response.is_closed) is True
