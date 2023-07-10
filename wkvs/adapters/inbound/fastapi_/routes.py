# Copyright 2021 - 2023 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Contains endpoint functions for the API"""
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from wkvs.config import WellKnownsConfig
from wkvs.container import Container

WELLKNOWNS_FILTER: set[str] = WellKnownsConfig.schema()["properties"].keys()

router = APIRouter()


@router.get(
    "/values/{value_name}",
    summary="retrieve a configured value",
    status_code=status.HTTP_200_OK,
)
@inject
async def retrieve_value(
    value_name: str,
    config: WellKnownsConfig = Depends(Provide[Container.config]),
) -> JSONResponse:
    """Retrieves the given value from configuration
    Args:
        value_name: the name of the value to be retrieved

    Raises:
        HTTPException 422 when the specified value is not configured
    """

    try:
        available = config.dict(include=WELLKNOWNS_FILTER)
        response = JSONResponse(content={value_name: available[value_name]})
    except KeyError as err:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"The value {value_name} is not configured",
        ) from err

    return response


@router.get(
    "/values",
    summary="retrieve all configured values",
    status_code=status.HTTP_200_OK,
)
@inject
async def retrieve_all_values(
    config: WellKnownsConfig = Depends(Provide[Container.config]),
) -> dict[str, str]:
    """Retrieves all values from the WellKnownsConfig class"""

    return config.dict(include=WELLKNOWNS_FILTER)
