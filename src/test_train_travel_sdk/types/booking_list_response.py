# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["BookingListResponse", "Data", "Links"]


class Data(BaseModel):
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


class Links(BaseModel):
    next: Optional[str] = None

    prev: Optional[str] = None

    self: Optional[str] = None


class BookingListResponse(BaseModel):
    data: Optional[List[Data]] = None
    """The wrapper for a collection is an array of objects."""

    links: Optional[Links] = None
