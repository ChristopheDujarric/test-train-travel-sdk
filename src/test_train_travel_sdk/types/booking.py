# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Booking"]


class Booking(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the booking"""

    has_bicycle: Optional[bool] = None
    """Indicates whether the passenger has a bicycle."""

    has_dog: Optional[bool] = None
    """Indicates whether the passenger has a dog."""

    passenger_name: Optional[str] = None
    """Name of the passenger"""

    trip_id: Optional[str] = None
    """Identifier of the booked trip"""
