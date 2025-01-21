# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["BookingPaymentParams", "Source", "SourceCard", "SourceBankAccount"]


class BookingPaymentParams(TypedDict, total=False):
    amount: float
    """Amount intended to be collected by this payment.

    A positive decimal figure describing the amount to be collected.
    """

    currency: Literal["bam", "bgn", "chf", "eur", "gbp", "nok", "sek", "try"]
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase.
    """

    source: Source
    """The payment source to take the payment from.

    This can be a card or a bank account. Some of these properties will be hidden on
    read to protect PII leaking.
    """


class SourceCard(TypedDict, total=False):
    address_country: Required[str]

    cvc: Required[int]
    """Card security code, 3 or 4 digits usually found on the back of the card."""

    exp_month: Required[int]
    """Two-digit number representing the card's expiration month."""

    exp_year: Required[int]
    """Four-digit number representing the card's expiration year."""

    name: Required[str]
    """Cardholder's full name as it appears on the card."""

    number: Required[str]
    """The card number, as a string without any separators.

    On read all but the last four digits will be masked for security.
    """

    address_city: str

    address_line1: str

    address_line2: str

    address_post_code: str

    object: Literal["card"]


class SourceBankAccount(TypedDict, total=False):
    account_type: Required[Literal["individual", "company"]]
    """The type of entity that holds the account.

    This can be either `individual` or `company`.
    """

    bank_name: Required[str]
    """The name of the bank associated with the routing number."""

    country: Required[str]
    """Two-letter country code (ISO 3166-1 alpha-2)."""

    name: Required[str]

    number: Required[str]
    """The account number for the bank account, in string form.

    Must be a current account.
    """

    object: Literal["bank_account"]

    sort_code: str
    """The sort code for the bank account, in string form. Must be a six-digit number."""


Source: TypeAlias = Union[SourceCard, SourceBankAccount]
