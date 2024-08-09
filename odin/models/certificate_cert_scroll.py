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

class CertificateCertScroll(object):
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
        'certificates': 'list[object]',
        'next_batch': 'str'
    }

    attribute_map = {
        'certificates': 'certificates',
        'next_batch': 'next_batch'
    }

    def __init__(self, certificates=None, next_batch=None):  # noqa: E501
        """CertificateCertScroll - a model defined in Swagger"""  # noqa: E501
        self._certificates = None
        self._next_batch = None
        self.discriminator = None
        if certificates is not None:
            self.certificates = certificates
        if next_batch is not None:
            self.next_batch = next_batch

    @property
    def certificates(self):
        """Gets the certificates of this CertificateCertScroll.  # noqa: E501


        :return: The certificates of this CertificateCertScroll.  # noqa: E501
        :rtype: list[object]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """Sets the certificates of this CertificateCertScroll.


        :param certificates: The certificates of this CertificateCertScroll.  # noqa: E501
        :type: list[object]
        """

        self._certificates = certificates

    @property
    def next_batch(self):
        """Gets the next_batch of this CertificateCertScroll.  # noqa: E501


        :return: The next_batch of this CertificateCertScroll.  # noqa: E501
        :rtype: str
        """
        return self._next_batch

    @next_batch.setter
    def next_batch(self, next_batch):
        """Sets the next_batch of this CertificateCertScroll.


        :param next_batch: The next_batch of this CertificateCertScroll.  # noqa: E501
        :type: str
        """

        self._next_batch = next_batch

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
        if issubclass(CertificateCertScroll, dict):
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
        if not isinstance(other, CertificateCertScroll):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other