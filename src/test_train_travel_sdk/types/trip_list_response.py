# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TripListResponse", "Data", "Links"]


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the trip"""

    arrival_time: Optional[datetime] = None
    """The date and time when the trip arrives"""

    bicycles_allowed: Optional[bool] = None
    """Indicates whether bicycles are allowed on the trip"""

    departure_time: Optional[datetime] = None
    """The date and time when the trip departs"""

    destination: Optional[str] = None
    """The destination station of the trip"""

    dogs_allowed: Optional[bool] = None
    """Indicates whether dogs are allowed on the trip"""

    operator: Optional[str] = None
    """The name of the operator of the trip"""

    origin: Optional[str] = None
    """The starting station of the trip"""

    price: Optional[float] = None
    """The cost of the trip"""


class Links(BaseModel):
    next: Optional[str] = None

    prev: Optional[str] = None

    self: Optional[str] = None


class TripListResponse(BaseModel):
    data: Optional[List[Data]] = None
    """The wrapper for a collection is an array of objects."""

    links: Optional[Links] = None
