# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .bookings.booking_payment import BookingPayment

__all__ = ["BookingPaymentResponse", "BookingPaymentResponseLinks"]


class BookingPaymentResponseLinks(BaseModel):
    booking: Optional[str] = None


class BookingPaymentResponse(BookingPayment):
    links: Optional[BookingPaymentResponseLinks] = None
