from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_gt_plays_limit import GetApiGtPlaysLimit
from ...models.get_api_gt_plays_sort import GetApiGtPlaysSort
from ...models.get_api_gt_plays_sources_item import GetApiGtPlaysSourcesItem
from ...models.get_api_gt_plays_status import GetApiGtPlaysStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, "GetApiGtPlaysLimit"] = UNSET,
    search: Union[Unset, str] = UNSET,
    session_id: Union[Unset, UUID] = UNSET,
    game_id: Union[Unset, UUID] = UNSET,
    status: Union[Unset, GetApiGtPlaysStatus] = UNSET,
    sources: Union[Unset, list[GetApiGtPlaysSourcesItem]] = UNSET,
    sort: Union[Unset, GetApiGtPlaysSort] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_limit: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.to_dict()
    if not isinstance(json_limit, Unset):
        params.update(json_limit)

    params["search"] = search

    json_session_id: Union[Unset, str] = UNSET
    if not isinstance(session_id, Unset):
        json_session_id = str(session_id)
    params["session_id"] = json_session_id

    json_game_id: Union[Unset, str] = UNSET
    if not isinstance(game_id, Unset):
        json_game_id = str(game_id)
    params["game_id"] = json_game_id

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_sources: Union[Unset, list[str]] = UNSET
    if not isinstance(sources, Unset):
        json_sources = []
        for sources_item_data in sources:
            sources_item = sources_item_data.value
            json_sources.append(sources_item)

    params["sources"] = json_sources

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/gt/plays",
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
    limit: Union[Unset, "GetApiGtPlaysLimit"] = UNSET,
    search: Union[Unset, str] = UNSET,
    session_id: Union[Unset, UUID] = UNSET,
    game_id: Union[Unset, UUID] = UNSET,
    status: Union[Unset, GetApiGtPlaysStatus] = UNSET,
    sources: Union[Unset, list[GetApiGtPlaysSourcesItem]] = UNSET,
    sort: Union[Unset, GetApiGtPlaysSort] = UNSET,
) -> Response[Any]:
    """
    Args:
        limit (Union[Unset, GetApiGtPlaysLimit]):
        search (Union[Unset, str]):
        session_id (Union[Unset, UUID]):
        game_id (Union[Unset, UUID]):
        status (Union[Unset, GetApiGtPlaysStatus]):
        sources (Union[Unset, list[GetApiGtPlaysSourcesItem]]):
        sort (Union[Unset, GetApiGtPlaysSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        limit=limit,
        search=search,
        session_id=session_id,
        game_id=game_id,
        status=status,
        sources=sources,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, "GetApiGtPlaysLimit"] = UNSET,
    search: Union[Unset, str] = UNSET,
    session_id: Union[Unset, UUID] = UNSET,
    game_id: Union[Unset, UUID] = UNSET,
    status: Union[Unset, GetApiGtPlaysStatus] = UNSET,
    sources: Union[Unset, list[GetApiGtPlaysSourcesItem]] = UNSET,
    sort: Union[Unset, GetApiGtPlaysSort] = UNSET,
) -> Response[Any]:
    """
    Args:
        limit (Union[Unset, GetApiGtPlaysLimit]):
        search (Union[Unset, str]):
        session_id (Union[Unset, UUID]):
        game_id (Union[Unset, UUID]):
        status (Union[Unset, GetApiGtPlaysStatus]):
        sources (Union[Unset, list[GetApiGtPlaysSourcesItem]]):
        sort (Union[Unset, GetApiGtPlaysSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        limit=limit,
        search=search,
        session_id=session_id,
        game_id=game_id,
        status=status,
        sources=sources,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
