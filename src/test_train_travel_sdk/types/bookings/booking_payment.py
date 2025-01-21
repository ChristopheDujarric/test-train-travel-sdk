# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["BookingPayment", "Source", "SourceCard", "SourceBankAccount"]


class SourceCard(BaseModel):
    address_country: str

    exp_month: int
    """Two-digit number representing the card's expiration month."""

    exp_year: int
    """Four-digit number representing the card's expiration year."""

    name: str
    """Cardholder's full name as it appears on the card."""

    number: str
    """The card number, as a string without any separators.

    On read all but the last four digits will be masked for security.
    """

    address_city: Optional[str] = None

    address_post_code: Optional[str] = None

    object: Optional[Literal["card"]] = None


class SourceBankAccount(BaseModel):
    account_type: Literal["individual", "company"]
    """The type of entity that holds the account.

    This can be either `individual` or `company`.
    """

    bank_name: str
    """The name of the bank associated with the routing number."""

    country: str
    """Two-letter country code (ISO 3166-1 alpha-2)."""

    name: str

    number: str
    """The account number for the bank account, in string form.

    Must be a current account.
    """

    object: Optional[Literal["bank_account"]] = None

    sort_code: Optional[str] = None
    """The sort code for the bank account, in string form. Must be a six-digit number."""


Source: TypeAlias = Union[SourceCard, SourceBankAccount]


class BookingPayment(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the payment.

    This will be a unique identifier for the payment, and is used to reference the
    payment in other objects.
    """

    amount: Optional[float] = None
    """Amount intended to be collected by this payment.

    A positive decimal figure describing the amount to be collected.
    """

    currency: Optional[Literal["bam", "bgn", "chf", "eur", "gbp", "nok", "sek", "try"]] = None
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase.
    """

    source: Optional[Source] = None
    """The payment source to take the payment from.

    This can be a card or a bank account. Some of these properties will be hidden on
    read to protect PII leaking.
    """

    status: Optional[Literal["pending", "succeeded", "failed"]] = None
    """The status of the payment, one of `pending`, `succeeded`, or `failed`."""
