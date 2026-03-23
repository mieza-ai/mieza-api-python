from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_gt_plays_id_history_limit import GetApiGtPlaysIdHistoryLimit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, "GetApiGtPlaysIdHistoryLimit"] = UNSET,
    node_id: Union[Unset, UUID] = UNSET,
    actor: Union[Unset, str] = UNSET,
    include_decisions: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_limit: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.to_dict()
    if not isinstance(json_limit, Unset):
        params.update(json_limit)

    json_node_id: Union[Unset, str] = UNSET
    if not isinstance(node_id, Unset):
        json_node_id = str(node_id)
    params["node_id"] = json_node_id

    params["actor"] = actor

    params["include_decisions"] = include_decisions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/gt/plays/:id/history",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, "GetApiGtPlaysIdHistoryLimit"] = UNSET,
    node_id: Union[Unset, UUID] = UNSET,
    actor: Union[Unset, str] = UNSET,
    include_decisions: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        limit (Union[Unset, GetApiGtPlaysIdHistoryLimit]):
        node_id (Union[Unset, UUID]):
        actor (Union[Unset, str]):
        include_decisions (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        limit=limit,
        node_id=node_id,
        actor=actor,
        include_decisions=include_decisions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, "GetApiGtPlaysIdHistoryLimit"] = UNSET,
    node_id: Union[Unset, UUID] = UNSET,
    actor: Union[Unset, str] = UNSET,
    include_decisions: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        limit (Union[Unset, GetApiGtPlaysIdHistoryLimit]):
        node_id (Union[Unset, UUID]):
        actor (Union[Unset, str]):
        include_decisions (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        limit=limit,
        node_id=node_id,
        actor=actor,
        include_decisions=include_decisions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
