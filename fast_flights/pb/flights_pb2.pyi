from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Emissions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_EMISSIONS: _ClassVar[Emissions]
    LESS_EMISSIONS: _ClassVar[Emissions]

class Seat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_SEAT: _ClassVar[Seat]
    ECONOMY: _ClassVar[Seat]
    PREMIUM_ECONOMY: _ClassVar[Seat]
    BUSINESS: _ClassVar[Seat]
    FIRST: _ClassVar[Seat]

class Trip(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_TRIP: _ClassVar[Trip]
    ROUND_TRIP: _ClassVar[Trip]
    ONE_WAY: _ClassVar[Trip]
    MULTI_CITY: _ClassVar[Trip]

class Passenger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_PASSENGER: _ClassVar[Passenger]
    ADULT: _ClassVar[Passenger]
    CHILD: _ClassVar[Passenger]
    INFANT_IN_SEAT: _ClassVar[Passenger]
    INFANT_ON_LAP: _ClassVar[Passenger]
UNKNOWN_EMISSIONS: Emissions
LESS_EMISSIONS: Emissions
UNKNOWN_SEAT: Seat
ECONOMY: Seat
PREMIUM_ECONOMY: Seat
BUSINESS: Seat
FIRST: Seat
UNKNOWN_TRIP: Trip
ROUND_TRIP: Trip
ONE_WAY: Trip
MULTI_CITY: Trip
UNKNOWN_PASSENGER: Passenger
ADULT: Passenger
CHILD: Passenger
INFANT_IN_SEAT: Passenger
INFANT_ON_LAP: Passenger

class Airport(_message.Message):
    __slots__ = ("airport",)
    AIRPORT_FIELD_NUMBER: _ClassVar[int]
    airport: str
    def __init__(self, airport: _Optional[str] = ...) -> None: ...

class FlightData(_message.Message):
    __slots__ = ("date", "from_airport", "to_airport", "max_stops", "airlines", "earliest_departure_hour", "latest_departure_hour", "earliest_arrival_hour", "latest_arrival_hour", "max_duration_minutes", "connecting_airports", "min_layover_minutes", "max_layover_minutes", "emissions")
    DATE_FIELD_NUMBER: _ClassVar[int]
    FROM_AIRPORT_FIELD_NUMBER: _ClassVar[int]
    TO_AIRPORT_FIELD_NUMBER: _ClassVar[int]
    MAX_STOPS_FIELD_NUMBER: _ClassVar[int]
    AIRLINES_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_DEPARTURE_HOUR_FIELD_NUMBER: _ClassVar[int]
    LATEST_DEPARTURE_HOUR_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_ARRIVAL_HOUR_FIELD_NUMBER: _ClassVar[int]
    LATEST_ARRIVAL_HOUR_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    CONNECTING_AIRPORTS_FIELD_NUMBER: _ClassVar[int]
    MIN_LAYOVER_MINUTES_FIELD_NUMBER: _ClassVar[int]
    MAX_LAYOVER_MINUTES_FIELD_NUMBER: _ClassVar[int]
    EMISSIONS_FIELD_NUMBER: _ClassVar[int]
    date: str
    from_airport: _containers.RepeatedCompositeFieldContainer[Airport]
    to_airport: _containers.RepeatedCompositeFieldContainer[Airport]
    max_stops: int
    airlines: _containers.RepeatedScalarFieldContainer[str]
    earliest_departure_hour: int
    latest_departure_hour: int
    earliest_arrival_hour: int
    latest_arrival_hour: int
    max_duration_minutes: int
    connecting_airports: _containers.RepeatedScalarFieldContainer[str]
    min_layover_minutes: int
    max_layover_minutes: int
    emissions: _containers.RepeatedScalarFieldContainer[Emissions]
    def __init__(self, date: _Optional[str] = ..., from_airport: _Optional[_Iterable[_Union[Airport, _Mapping]]] = ..., to_airport: _Optional[_Iterable[_Union[Airport, _Mapping]]] = ..., max_stops: _Optional[int] = ..., airlines: _Optional[_Iterable[str]] = ..., earliest_departure_hour: _Optional[int] = ..., latest_departure_hour: _Optional[int] = ..., earliest_arrival_hour: _Optional[int] = ..., latest_arrival_hour: _Optional[int] = ..., max_duration_minutes: _Optional[int] = ..., connecting_airports: _Optional[_Iterable[str]] = ..., min_layover_minutes: _Optional[int] = ..., max_layover_minutes: _Optional[int] = ..., emissions: _Optional[_Iterable[_Union[Emissions, str]]] = ...) -> None: ...

class Baggage(_message.Message):
    __slots__ = ("carry_on_bags", "checked_bags")
    CARRY_ON_BAGS_FIELD_NUMBER: _ClassVar[int]
    CHECKED_BAGS_FIELD_NUMBER: _ClassVar[int]
    carry_on_bags: int
    checked_bags: int
    def __init__(self, carry_on_bags: _Optional[int] = ..., checked_bags: _Optional[int] = ...) -> None: ...

class Info(_message.Message):
    __slots__ = ("data", "seat", "passengers", "max_price", "baggage", "hide_separate_and_self_transfer", "trip", "exclude_basic_economy")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SEAT_FIELD_NUMBER: _ClassVar[int]
    PASSENGERS_FIELD_NUMBER: _ClassVar[int]
    MAX_PRICE_FIELD_NUMBER: _ClassVar[int]
    BAGGAGE_FIELD_NUMBER: _ClassVar[int]
    HIDE_SEPARATE_AND_SELF_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    TRIP_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_BASIC_ECONOMY_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[FlightData]
    seat: Seat
    passengers: _containers.RepeatedScalarFieldContainer[Passenger]
    max_price: int
    baggage: Baggage
    hide_separate_and_self_transfer: bool
    trip: Trip
    exclude_basic_economy: bool
    def __init__(self, data: _Optional[_Iterable[_Union[FlightData, _Mapping]]] = ..., seat: _Optional[_Union[Seat, str]] = ..., passengers: _Optional[_Iterable[_Union[Passenger, str]]] = ..., max_price: _Optional[int] = ..., baggage: _Optional[_Union[Baggage, _Mapping]] = ..., hide_separate_and_self_transfer: _Optional[bool] = ..., trip: _Optional[_Union[Trip, str]] = ..., exclude_basic_economy: _Optional[bool] = ...) -> None: ...

class Price(_message.Message):
    __slots__ = ("price", "currency")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    price: int
    currency: str
    def __init__(self, price: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class ItinerarySummary(_message.Message):
    __slots__ = ("flights", "price")
    FLIGHTS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    flights: str
    price: Price
    def __init__(self, flights: _Optional[str] = ..., price: _Optional[_Union[Price, _Mapping]] = ...) -> None: ...
