import httpx

from python_gt_client.client import AuthenticatedClient, Client


def test_client_with_headers_updates_existing_client() -> None:
    client = Client(base_url="https://example.com")
    httpx_client = client.get_httpx_client()
    try:
        updated = client.with_headers({"X-Test": "value"})
        assert updated is not client
        assert updated._headers["X-Test"] == "value"
        assert httpx_client.headers["X-Test"] == "value"
    finally:
        httpx_client.close()


def test_client_with_timeout_updates_existing_client() -> None:
    client = Client(base_url="https://example.com")
    httpx_client = client.get_httpx_client()
    try:
        timeout = httpx.Timeout(5.0)
        updated = client.with_timeout(timeout)
        assert updated is not client
        assert updated._timeout == timeout
        assert httpx_client.timeout == timeout
    finally:
        httpx_client.close()


def test_authenticated_client_sets_auth_header_with_prefix() -> None:
    client = AuthenticatedClient(
        base_url="https://example.com",
        token="token-123",
    )
    httpx_client = client.get_httpx_client()
    try:
        assert httpx_client.headers["Authorization"] == "Bearer token-123"
    finally:
        httpx_client.close()


def test_authenticated_client_sets_auth_header_without_prefix() -> None:
    client = AuthenticatedClient(
        base_url="https://example.com",
        token="token-123",
        prefix="",
    )
    httpx_client = client.get_httpx_client()
    try:
        assert httpx_client.headers["Authorization"] == "token-123"
    finally:
        httpx_client.close()
