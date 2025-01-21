# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StationListParams"]


class StationListParams(TypedDict, total=False):
    coordinates: str
    """
    The latitude and longitude of the user's location, to narrow down the search
    results to sites within a proximity of this location.
    """

    country: str
    """Filter stations by country code"""

    limit: int
    """The number of items to return per page"""

    page: int
    """The page number to return"""

    search: str
    """A search term to filter the list of stations by name or address."""
