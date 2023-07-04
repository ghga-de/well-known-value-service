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

"""Basic tests for the API"""
import json

import pytest
from fastapi import status

from tests.fixtures.joint import JointFixture, joint_fixture  # noqa: F401


@pytest.mark.asyncio
async def test_happy_retrieval_simple_value(joint_fixture: JointFixture):  # noqa: F811
    """Test that configured values can be retrieved"""
    url = "/values/a_string"
    response = await joint_fixture.rest_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(response.content) == {"a_string": "Some value"}


@pytest.mark.asyncio
async def test_happy_retrieval_complex_value(joint_fixture: JointFixture):  # noqa: F811
    """Test that configured values can be retrieved"""
    url = "/values/ghga_crypt4gh_public_key"
    response = await joint_fixture.rest_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(response.content) == {
        "ghga_crypt4gh_public_key": {
            "version": 1.0,
            "key": "30F32923F923IJF2RO23OIRJ2LK43JL3KJ4L",
        }
    }


@pytest.mark.asyncio
async def test_non_configured_value(joint_fixture: JointFixture):  # noqa: F811
    """Test that we get an HTTP exception when requesting a non-configured value"""
    url = "/values/not_configured"
    response = await joint_fixture.rest_client.get(url)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert (
        json.loads(response.content)["detail"]
        == "The value not_configured is not configured"
    )
