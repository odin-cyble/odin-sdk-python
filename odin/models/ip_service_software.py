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

class IPServiceSoftware(object):
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
        'edition': 'object',
        'language': 'object',
        'part': 'object',
        'product': 'object',
        'update': 'object',
        'uri': 'str',
        'vendor': 'object',
        'version': 'object'
    }

    attribute_map = {
        'edition': 'edition',
        'language': 'language',
        'part': 'part',
        'product': 'product',
        'update': 'update',
        'uri': 'uri',
        'vendor': 'vendor',
        'version': 'version'
    }

    def __init__(self, edition=None, language=None, part=None, product=None, update=None, uri=None, vendor=None, version=None):  # noqa: E501
        """IPServiceSoftware - a model defined in Swagger"""  # noqa: E501
        self._edition = None
        self._language = None
        self._part = None
        self._product = None
        self._update = None
        self._uri = None
        self._vendor = None
        self._version = None
        self.discriminator = None
        if edition is not None:
            self.edition = edition
        if language is not None:
            self.language = language
        if part is not None:
            self.part = part
        if product is not None:
            self.product = product
        if update is not None:
            self.update = update
        if uri is not None:
            self.uri = uri
        if vendor is not None:
            self.vendor = vendor
        if version is not None:
            self.version = version

    @property
    def edition(self):
        """Gets the edition of this IPServiceSoftware.  # noqa: E501


        :return: The edition of this IPServiceSoftware.  # noqa: E501
        :rtype: object
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this IPServiceSoftware.


        :param edition: The edition of this IPServiceSoftware.  # noqa: E501
        :type: object
        """

        self._edition = edition

    @property
    def language(self):
        """Gets the language of this IPServiceSoftware.  # noqa: E501


        :return: The language of this IPServiceSoftware.  # noqa: E501
        :rtype: object
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this IPServiceSoftware.


        :param language: The language of this IPServiceSoftware.  # noqa: E501
        :type: object
        """

        self._language = language

    @property
    def part(self):
        """Gets the part of this IPServiceSoftware.  # noqa: E501


        :return: The part of this IPServiceSoftware.  # noqa: E501
        :rtype: object
        """
        return self._part

    @part.setter
    def part(self, part):
        """Sets the part of this IPServiceSoftware.


        :param part: The part of this IPServiceSoftware.  # noqa: E501
        :type: object
        """

        self._part = part

    @property
    def product(self):
        """Gets the product of this IPServiceSoftware.  # noqa: E501


        :return: The product of this IPServiceSoftware.  # noqa: E501
        :rtype: object
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this IPServiceSoftware.


        :param product: The product of this IPServiceSoftware.  # noqa: E501
        :type: object
        """

        self._product = product

    @property
    def update(self):
        """Gets the update of this IPServiceSoftware.  # noqa: E501


        :return: The update of this IPServiceSoftware.  # noqa: E501
        :rtype: object
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this IPServiceSoftware.


        :param update: The update of this IPServiceSoftware.  # noqa: E501
        :type: object
        """

        self._update = update

    @property
    def uri(self):
        """Gets the uri of this IPServiceSoftware.  # noqa: E501


        :return: The uri of this IPServiceSoftware.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this IPServiceSoftware.


        :param uri: The uri of this IPServiceSoftware.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def vendor(self):
        """Gets the vendor of this IPServiceSoftware.  # noqa: E501


        :return: The vendor of this IPServiceSoftware.  # noqa: E501
        :rtype: object
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this IPServiceSoftware.


        :param vendor: The vendor of this IPServiceSoftware.  # noqa: E501
        :type: object
        """

        self._vendor = vendor

    @property
    def version(self):
        """Gets the version of this IPServiceSoftware.  # noqa: E501


        :return: The version of this IPServiceSoftware.  # noqa: E501
        :rtype: object
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IPServiceSoftware.


        :param version: The version of this IPServiceSoftware.  # noqa: E501
        :type: object
        """

        self._version = version

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
        if issubclass(IPServiceSoftware, dict):
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
        if not isinstance(other, IPServiceSoftware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
