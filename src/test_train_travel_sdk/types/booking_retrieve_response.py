# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .booking import Booking
from .._models import BaseModel

__all__ = ["BookingRetrieveResponse", "BookingRetrieveResponseLinks"]


class BookingRetrieveResponseLinks(BaseModel):
    self: Optional[str] = None


class BookingRetrieveResponse(Booking):
    links: Optional[BookingRetrieveResponseLinks] = None
