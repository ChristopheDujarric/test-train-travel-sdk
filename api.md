# Stations

Types:

```python
from test_train_travel_sdk.types import StationListResponse
```

Methods:

- <code title="get /stations">client.stations.<a href="./src/test_train_travel_sdk/resources/stations.py">list</a>(\*\*<a href="src/test_train_travel_sdk/types/station_list_params.py">params</a>) -> <a href="./src/test_train_travel_sdk/types/station_list_response.py">StationListResponse</a></code>

# Trips

Types:

```python
from test_train_travel_sdk.types import TripListResponse
```

Methods:

- <code title="get /trips">client.trips.<a href="./src/test_train_travel_sdk/resources/trips.py">list</a>(\*\*<a href="src/test_train_travel_sdk/types/trip_list_params.py">params</a>) -> <a href="./src/test_train_travel_sdk/types/trip_list_response.py">TripListResponse</a></code>

# Bookings

Types:

```python
from test_train_travel_sdk.types import (
    Booking,
    BookingCreateResponse,
    BookingRetrieveResponse,
    BookingListResponse,
    BookingPaymentResponse,
)
```

Methods:

- <code title="post /bookings">client.bookings.<a href="./src/test_train_travel_sdk/resources/bookings/bookings.py">create</a>(\*\*<a href="src/test_train_travel_sdk/types/booking_create_params.py">params</a>) -> <a href="./src/test_train_travel_sdk/types/booking_create_response.py">BookingCreateResponse</a></code>
- <code title="get /bookings/{bookingId}">client.bookings.<a href="./src/test_train_travel_sdk/resources/bookings/bookings.py">retrieve</a>(booking_id) -> <a href="./src/test_train_travel_sdk/types/booking_retrieve_response.py">BookingRetrieveResponse</a></code>
- <code title="get /bookings">client.bookings.<a href="./src/test_train_travel_sdk/resources/bookings/bookings.py">list</a>(\*\*<a href="src/test_train_travel_sdk/types/booking_list_params.py">params</a>) -> <a href="./src/test_train_travel_sdk/types/booking_list_response.py">BookingListResponse</a></code>
- <code title="delete /bookings/{bookingId}">client.bookings.<a href="./src/test_train_travel_sdk/resources/bookings/bookings.py">delete</a>(booking_id) -> None</code>
- <code title="post /bookings/{bookingId}/payment">client.bookings.<a href="./src/test_train_travel_sdk/resources/bookings/bookings.py">payment</a>(booking_id, \*\*<a href="src/test_train_travel_sdk/types/booking_payment_params.py">params</a>) -> <a href="./src/test_train_travel_sdk/types/booking_payment_response.py">BookingPaymentResponse</a></code>

## Payments

Types:

```python
from test_train_travel_sdk.types.bookings import BookingPayment
```
