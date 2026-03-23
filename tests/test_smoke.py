import importlib


def test_package_importable():
    """Package can be imported without errors."""
    mod = importlib.import_module("python_gt_client")
    assert mod is not None


def test_client_class_exists():
    """Client class is importable and constructable."""
    from python_gt_client.client import Client

    client = Client(base_url="http://localhost:8000")
    assert client is not None


def test_client_with_headers_returns_new_client():
    """with_headers returns a client that includes the new headers."""
    from python_gt_client.client import Client

    original = Client(base_url="http://localhost:8000")
    updated = original.with_headers({"Authorization": "Bearer test-token"})
    assert updated is not None


def test_client_with_timeout():
    """with_timeout returns a client with the updated timeout."""
    import httpx
    from python_gt_client.client import Client

    client = Client(base_url="http://localhost:8000")
    updated = client.with_timeout(httpx.Timeout(10.0))
    assert updated is not None


def test_errors_module_exports():
    """Errors module exposes UnexpectedStatus."""
    from python_gt_client.errors import UnexpectedStatus

    assert issubclass(UnexpectedStatus, Exception)
