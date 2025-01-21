# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TripListParams"]


class TripListParams(TypedDict, total=False):
    bicycles: Required[bool]
    """Only return trips where bicycles are known to be allowed"""

    date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date and time of the trip in ISO 8601 format in origin station's timezone."""

    destination: Required[str]
    """The ID of the destination station"""

    origin: Required[str]
    """The ID of the origin station"""

    dogs: bool
    """Only return trips where dogs are known to be allowed"""

    limit: int
    """The number of items to return per page"""

    page: int
    """The page number to return"""
