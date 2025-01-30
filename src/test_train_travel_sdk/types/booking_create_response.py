# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .booking import Booking
from .._models import BaseModel

__all__ = ["BookingCreateResponse", "BookingCreateResponseLinks"]


class BookingCreateResponseLinks(BaseModel):
    self: Optional[str] = None


class BookingCreateResponse(Booking):
    links: Optional[BookingCreateResponseLinks] = None
