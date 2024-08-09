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

class ServiceIPHostname(object):
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
        'last_updated_at': 'str',
        'name': 'str'
    }

    attribute_map = {
        'last_updated_at': 'last_updated_at',
        'name': 'name'
    }

    def __init__(self, last_updated_at=None, name=None):  # noqa: E501
        """ServiceIPHostname - a model defined in Swagger"""  # noqa: E501
        self._last_updated_at = None
        self._name = None
        self.discriminator = None
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if name is not None:
            self.name = name

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this ServiceIPHostname.  # noqa: E501


        :return: The last_updated_at of this ServiceIPHostname.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this ServiceIPHostname.


        :param last_updated_at: The last_updated_at of this ServiceIPHostname.  # noqa: E501
        :type: str
        """

        self._last_updated_at = last_updated_at

    @property
    def name(self):
        """Gets the name of this ServiceIPHostname.  # noqa: E501


        :return: The name of this ServiceIPHostname.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceIPHostname.


        :param name: The name of this ServiceIPHostname.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(ServiceIPHostname, dict):
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
        if not isinstance(other, ServiceIPHostname):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other