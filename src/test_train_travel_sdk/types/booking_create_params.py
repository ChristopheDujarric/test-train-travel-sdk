# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BookingCreateParams"]


class BookingCreateParams(TypedDict, total=False):
    has_bicycle: bool
    """Indicates whether the passenger has a bicycle."""

    has_dog: bool
    """Indicates whether the passenger has a dog."""

    passenger_name: str
    """Name of the passenger"""

    trip_id: str
    """Identifier of the booked trip"""
