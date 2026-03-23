# mieza-api-python

Python client for the [Mieza](https://mieza.ai) GTO API, auto-generated from the OpenAPI specification.

## Installation

```bash
pip install mieza-gto-sdk
```

## Usage

```python
from python_gt_client import Client, AuthenticatedClient

# Unauthenticated client
client = Client(base_url="https://gto.mieza.ai")

# Authenticated client
client = AuthenticatedClient(
    base_url="https://gto.mieza.ai",
    token="your-api-key",
)
```

### Making requests

```python
from python_gt_client.api.default import get_api_gt_games

response = get_api_gt_games.sync(client=client)
```

## Development

The client is generated from the GTO service's OpenAPI spec:

```bash
./generate.sh
```

## Running tests

```bash
pytest tests/
```

## License

MIT
