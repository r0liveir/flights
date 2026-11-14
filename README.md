# ✈️ fast-flights (fork)

The fast and strongly-typed Google Flights scraper (API) implemented in Python.
Based on Base64-encoded Protobuf string.

This is a fork from AWeirdDev's `flights` project with some additional stuff:
- `operating_airline` field on `SingleFlights`, with IATA airline code and flight number.
- support to multiple origin and destination airports when querying.

Check out the original documentation here:
[**Documentation (v3)**](https://aweirddev.github.io/flights)
```haskell
$ pip install fast-flights
```

## At a glance
```python
from fast_flights import (
    FlightQuery,
    Passengers, 
    create_query, 
    get_flights
)

query = create_query(
    flights=[
        FlightQuery(
            date="YYYY-MM-DD",          # change the date
            from_airport="POA",         # string or list, three-letter name
            to_airport=["CGH", "GRU"],  # string or list, three-letter name
        ),
    ],
    seat="economy",  # business/economy/first/premium-economy
    trip="one-way",  # multi-city/one-way/round-trip
    passengers=Passengers(adults=1),
    language="pt-BR",
)
res = get_flights(query)
```

## Search filters

`FlightQuery` supports filters for each flight leg:

```python
flight = FlightQuery(
    date="YYYY-MM-DD",
    from_airport="MYJ",
    to_airport="TPE",
    max_stops=1,
    airlines=["JL", "ONEWORLD"],
    earliest_departure_hour=7,
    latest_departure_hour=18,
    earliest_arrival_hour=10,
    latest_arrival_hour=23,
    max_duration_minutes=720,
    connecting_airports=["HND", "NRT"],
    min_layover_minutes=60,
    max_layover_minutes=240,
    less_emissions_only=True,
)
```

Filters for the whole search are passed to `create_query`:

```python
query = create_query(
    flights=[flight],
    currency="USD",
    max_price=1500,
    carry_on_bags=1,
    checked_bags=1,
    hide_separate_and_self_transfer=True,
    exclude_basic_economy=True,
)
```

Hours use local airport time on a 0–23 clock. Duration and layover values use
minutes, and `max_price` uses the selected `currency`. Google currently applies
the first leg's airline filter to the whole search.

## Integrations
If you'd like, you can use some sponsored integrations.

### SearchApi <kbd>Sponsored</kbd>
If you want better consistency and richer data, consider using [SearchApi](https://www.searchapi.io/google-flights-api?utm_source=github&utm_medium=sponsorship&utm_campaign=google_flights_api&utm_content=AWeirdDev_flights).

```python
from fast_flights.integrations import SearchApi, SearchApiResult

result: SearchApiResult = get_flights(
    ...,
    integration=SearchApi()
)

# rich data!
result.flights
result.cheaper_alternatives
result.price_insights
result.booking_options
...
```

### RapidProxy <kbd>Sponsored</kbd>
Usually, you'll need a proxy to avoid bot detection from Google. [RapidProxy](https://rapidproxy.io/?ref=flights) provides reliable residential proxy solutions with 90M+ IPs worldwide, smart IP rotation, sticky sessions, and non-expiring traffic. Ideal for web scraping, automation, and large-scale data collection. For more information, see [Setting Up RapidProxy](#setting-up-rapidproxy).

<details>
    <summary>Setting Up RapidProxy</summary>

#### Setting Up RapidProxy
RapidProxy offers two proxy types, both supporting HTTP, HTTPS, and SOCKS5, with "dynamic residential" and "static residential" types.

To get started, you'll need to first log in to the [RapidProxy](https://rapidproxy.io/?ref=flights) dashboard, and choose the proxy product you need.

1. Config: Pick the region, proxy type and connection mode.
2. The dashboard gives you the connection details.
3. Record the required fields.

You'll need:
- `HOST` - Proxy host
- `PORT` - Port
- `USERNAME` - Username for authentication
- `PASSWORD` - Password for authentication

The connection format is `HOST:PORT:USERNAME:PASSWORD`.

Normally, you'll want to store this in a `.env` file or just the environment:

```env
RAPIDPROXY_HOST=HOST
RAPIDPROXY_PORT=PORT
RAPIDPROXY_USERNAME=USERNAME
RAPIDPROXY_PASSWORD=PASSWORD
```

Since `get_flights()` supports `proxy` out of the box, you can just use it:

```python
import os

PROXY_URL = (
   f"http://{os.environ['RAPIDPROXY_USERNAME']}:"
   f"{os.environ['RAPIDPROXY_PASSWORD']}@"
   f"{os.environ['RAPIDPROXY_HOST']}:"
   f"{os.environ['RAPIDPROXY_PORT']}"
)

results = get_flights(..., proxy=PROXY_URL)
```

The rest is the same, and now you have a working proxy.

For more information:

- Website: https://www.rapidproxy.io/
- Getting started: https://docs.rapidproxy.io/proxies/getting-started
- Integration guide: https://docs.rapidproxy.io/proxies/integration-guide
- Support: support@rapidproxy.io

</details>

### Bright Data
Use the [BrightData](https://brightdata.com) integration to protect your IP.

```python
from fast_flights.integrations import BrightData

result = get_flights(
    ..., 
    integration=BrightData(zone="...")
)

# ... same as normal queries
```
## Roadmap
- [x] Use JavaScript data instead of traditional HTML parsing
- [x] Add support for integrations
- [ ] Add support for booking summary URL from Google
- [ ] Dangerously use Google's `GetShoppingResults` internal API. Get ready to get banned.

## Contributing
Contributing is welcomed! A few notes though:
1. please no ai slop. i am not reading all that.
2. im really busy with life; im not a full-time reddit mod.

(this counts for me as well -r0liveir)

***

(c) 2024-2026 AWeirdDev, and all the awesome people

</div>
