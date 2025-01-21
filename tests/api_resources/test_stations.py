# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from test_train_travel_sdk import TestTrainTravelSDK, AsyncTestTrainTravelSDK
from test_train_travel_sdk.types import StationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TestTrainTravelSDK) -> None:
        station = client.stations.list()
        assert_matches_type(StationListResponse, station, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TestTrainTravelSDK) -> None:
        station = client.stations.list(
            coordinates="coordinates",
            country="country",
            limit=1,
            page=1,
            search="Milano Centrale",
        )
        assert_matches_type(StationListResponse, station, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TestTrainTravelSDK) -> None:
        response = client.stations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        station = response.parse()
        assert_matches_type(StationListResponse, station, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TestTrainTravelSDK) -> None:
        with client.stations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            station = response.parse()
            assert_matches_type(StationListResponse, station, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTestTrainTravelSDK) -> None:
        station = await async_client.stations.list()
        assert_matches_type(StationListResponse, station, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTestTrainTravelSDK) -> None:
        station = await async_client.stations.list(
            coordinates="coordinates",
            country="country",
            limit=1,
            page=1,
            search="Milano Centrale",
        )
        assert_matches_type(StationListResponse, station, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTestTrainTravelSDK) -> None:
        response = await async_client.stations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        station = await response.parse()
        assert_matches_type(StationListResponse, station, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTestTrainTravelSDK) -> None:
        async with async_client.stations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            station = await response.parse()
            assert_matches_type(StationListResponse, station, path=["response"])

        assert cast(Any, response.is_closed) is True
