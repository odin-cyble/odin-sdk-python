# coding: utf-8

"""
    Odin

    ODIN APIs to search across IP Services, CVEs, Certificates, Exposed Files/Buckets, Domains and more  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_auth': 'bool',
        'server_auth': 'bool'
    }

    attribute_map = {
        'client_auth': 'client_auth',
        'server_auth': 'server_auth'
    }

    def __init__(self, client_auth=None, server_auth=None):  # noqa: E501
        """CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage - a model defined in Swagger"""  # noqa: E501
        self._client_auth = None
        self._server_auth = None
        self.discriminator = None
        if client_auth is not None:
            self.client_auth = client_auth
        if server_auth is not None:
            self.server_auth = server_auth

    @property
    def client_auth(self):
        """Gets the client_auth of this CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage.  # noqa: E501


        :return: The client_auth of this CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage.  # noqa: E501
        :rtype: bool
        """
        return self._client_auth

    @client_auth.setter
    def client_auth(self, client_auth):
        """Sets the client_auth of this CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage.


        :param client_auth: The client_auth of this CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage.  # noqa: E501
        :type: bool
        """

        self._client_auth = client_auth

    @property
    def server_auth(self):
        """Gets the server_auth of this CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage.  # noqa: E501


        :return: The server_auth of this CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage.  # noqa: E501
        :rtype: bool
        """
        return self._server_auth

    @server_auth.setter
    def server_auth(self, server_auth):
        """Sets the server_auth of this CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage.


        :param server_auth: The server_auth of this CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage.  # noqa: E501
        :type: bool
        """

        self._server_auth = server_auth

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CertificateCertificateHashResponseDataCertificateExtensionsExtendedKeyUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
