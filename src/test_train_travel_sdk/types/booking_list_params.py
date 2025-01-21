# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BookingListParams"]


class BookingListParams(TypedDict, total=False):
    limit: int
    """The number of items to return per page"""

    page: int
    """The page number to return"""
