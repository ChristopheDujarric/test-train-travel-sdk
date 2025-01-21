# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["StationListResponse", "Data", "Links"]


class Data(BaseModel):
    id: str
    """Unique identifier for the station."""

    address: str
    """The address of the station."""

    country_code: str
    """The country code of the station."""

    name: str
    """The name of the station"""

    timezone: Optional[str] = None
    """
    The timezone of the station in the
    [IANA Time Zone Database format](https://www.iana.org/time-zones).
    """


class Links(BaseModel):
    next: Optional[str] = None

    prev: Optional[str] = None

    self: Optional[str] = None


class StationListResponse(BaseModel):
    data: Optional[List[Data]] = None
    """The wrapper for a collection is an array of objects."""

    links: Optional[Links] = None
