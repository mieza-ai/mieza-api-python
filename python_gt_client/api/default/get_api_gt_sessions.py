from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_gt_sessions_limit import GetApiGtSessionsLimit
from ...models.get_api_gt_sessions_sort import GetApiGtSessionsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, "GetApiGtSessionsLimit"] = UNSET,
    player_id: Union[Unset, UUID] = UNSET,
    game_id: Union[Unset, UUID] = UNSET,
    active_only: Union[Unset, bool] = UNSET,
    sort: Union[Unset, GetApiGtSessionsSort] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_limit: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.to_dict()
    if not isinstance(json_limit, Unset):
        params.update(json_limit)

    json_player_id: Union[Unset, str] = UNSET
    if not isinstance(player_id, Unset):
        json_player_id = str(player_id)
    params["player_id"] = json_player_id

    json_game_id: Union[Unset, str] = UNSET
    if not isinstance(game_id, Unset):
        json_game_id = str(game_id)
    params["game_id"] = json_game_id

    params["active_only"] = active_only

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/gt/sessions",
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
    limit: Union[Unset, "GetApiGtSessionsLimit"] = UNSET,
    player_id: Union[Unset, UUID] = UNSET,
    game_id: Union[Unset, UUID] = UNSET,
    active_only: Union[Unset, bool] = UNSET,
    sort: Union[Unset, GetApiGtSessionsSort] = UNSET,
) -> Response[Any]:
    """
    Args:
        limit (Union[Unset, GetApiGtSessionsLimit]):
        player_id (Union[Unset, UUID]):
        game_id (Union[Unset, UUID]):
        active_only (Union[Unset, bool]):
        sort (Union[Unset, GetApiGtSessionsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        limit=limit,
        player_id=player_id,
        game_id=game_id,
        active_only=active_only,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, "GetApiGtSessionsLimit"] = UNSET,
    player_id: Union[Unset, UUID] = UNSET,
    game_id: Union[Unset, UUID] = UNSET,
    active_only: Union[Unset, bool] = UNSET,
    sort: Union[Unset, GetApiGtSessionsSort] = UNSET,
) -> Response[Any]:
    """
    Args:
        limit (Union[Unset, GetApiGtSessionsLimit]):
        player_id (Union[Unset, UUID]):
        game_id (Union[Unset, UUID]):
        active_only (Union[Unset, bool]):
        sort (Union[Unset, GetApiGtSessionsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        limit=limit,
        player_id=player_id,
        game_id=game_id,
        active_only=active_only,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
