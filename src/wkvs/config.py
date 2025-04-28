# Copyright 2021 - 2025 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
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

from ghga_service_commons.api import ApiConfigBase
from hexkit.config import config_from_yaml
from hexkit.log import LoggingConfig
from pydantic import Field
from pydantic_settings import BaseSettings


class WellKnownConfig(BaseSettings):
    """Contains the configured values for the service"""

    crypt4gh_public_key: str = Field(..., description="The GHGA crypt4gh public key.")
    dcs_api_url: str = Field(
        ..., description="URL to the root of the DRS-compatible DCS API."
    )
    ucs_api_url: str = Field(
        ...,
        description="URL to the root of the upload controller API.",
    )
    wps_api_url: str = Field(..., description="URL to the root of the WPS API.")
    storage_aliases: dict = Field(
        ...,
        description="Mapping of storage alias to endpoint URL for all available S3 object storages",
    )
    alias_decodes: dict = Field(
        ...,
        description="Mapping of storage alias to its human-readable format",
        examples=[{"HD01": "Heidelberg", "TUE01": "Tübingen"}],
    )


SERVICE_NAME: str = "wkvs"


@config_from_yaml(prefix=SERVICE_NAME)
class Config(ApiConfigBase, WellKnownConfig, LoggingConfig):
    """Config parameters and their defaults."""

    service_name: str = SERVICE_NAME
