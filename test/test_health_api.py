# coding: utf-8

"""
    Odin

    ODIN APIs to search across IP Services, CVEs, Certificates, Exposed Files/Buckets, Domains and more  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import odin
from odin.odin.health_api import HealthApi  # noqa: E501
from odin.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_ping_get(self):
        """Test case for v1_ping_get

        Health Check  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
