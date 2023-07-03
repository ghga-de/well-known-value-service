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

"""Config Parameter Modeling and Parsing"""
from typing import Any

from ghga_service_commons.api import ApiConfigBase
from hexkit.config import config_from_yaml
from pydantic import BaseSettings, Field


class WellKnownsConfig(BaseSettings):
    """Contains the configured values for the service"""

    well_knowns: dict[str, Any] = Field(
        ...,
        description="A dictionary containing the configured 'well-known values'.",
    )


@config_from_yaml(prefix="wkvs")
class Config(ApiConfigBase, WellKnownsConfig):
    """Config parameters and their defaults."""

    service_name: str = "wkvs"
