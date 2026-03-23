from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_gt_games_limit import GetApiGtGamesLimit
from ...models.get_api_gt_games_sort import GetApiGtGamesSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, "GetApiGtGamesLimit"] = UNSET,
    search: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetApiGtGamesSort] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_limit: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.to_dict()
    if not isinstance(json_limit, Unset):
        params.update(json_limit)

    params["search"] = search

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/gt/games",
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
    limit: Union[Unset, "GetApiGtGamesLimit"] = UNSET,
    search: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetApiGtGamesSort] = UNSET,
) -> Response[Any]:
    """
    Args:
        limit (Union[Unset, GetApiGtGamesLimit]):
        search (Union[Unset, str]):
        sort (Union[Unset, GetApiGtGamesSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        limit=limit,
        search=search,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, "GetApiGtGamesLimit"] = UNSET,
    search: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetApiGtGamesSort] = UNSET,
) -> Response[Any]:
    """
    Args:
        limit (Union[Unset, GetApiGtGamesLimit]):
        search (Union[Unset, str]):
        sort (Union[Unset, GetApiGtGamesSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        limit=limit,
        search=search,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
