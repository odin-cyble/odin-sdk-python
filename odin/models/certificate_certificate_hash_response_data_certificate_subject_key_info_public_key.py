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

class CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey(object):
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
        'b': 'str',
        'curve': 'str',
        'gx': 'str',
        'gy': 'str',
        'length': 'int',
        'p': 'str',
        'x': 'str',
        'y': 'str'
    }

    attribute_map = {
        'b': 'b',
        'curve': 'curve',
        'gx': 'gx',
        'gy': 'gy',
        'length': 'length',
        'p': 'p',
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, b=None, curve=None, gx=None, gy=None, length=None, p=None, x=None, y=None):  # noqa: E501
        """CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey - a model defined in Swagger"""  # noqa: E501
        self._b = None
        self._curve = None
        self._gx = None
        self._gy = None
        self._length = None
        self._p = None
        self._x = None
        self._y = None
        self.discriminator = None
        if b is not None:
            self.b = b
        if curve is not None:
            self.curve = curve
        if gx is not None:
            self.gx = gx
        if gy is not None:
            self.gy = gy
        if length is not None:
            self.length = length
        if p is not None:
            self.p = p
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def b(self):
        """Gets the b of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501


        :return: The b of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.


        :param b: The b of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :type: str
        """

        self._b = b

    @property
    def curve(self):
        """Gets the curve of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501


        :return: The curve of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._curve

    @curve.setter
    def curve(self, curve):
        """Sets the curve of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.


        :param curve: The curve of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :type: str
        """

        self._curve = curve

    @property
    def gx(self):
        """Gets the gx of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501


        :return: The gx of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._gx

    @gx.setter
    def gx(self, gx):
        """Sets the gx of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.


        :param gx: The gx of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :type: str
        """

        self._gx = gx

    @property
    def gy(self):
        """Gets the gy of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501


        :return: The gy of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._gy

    @gy.setter
    def gy(self, gy):
        """Sets the gy of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.


        :param gy: The gy of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :type: str
        """

        self._gy = gy

    @property
    def length(self):
        """Gets the length of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501


        :return: The length of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.


        :param length: The length of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def p(self):
        """Gets the p of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501


        :return: The p of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._p

    @p.setter
    def p(self, p):
        """Sets the p of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.


        :param p: The p of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :type: str
        """

        self._p = p

    @property
    def x(self):
        """Gets the x of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501


        :return: The x of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.


        :param x: The x of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :type: str
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501


        :return: The y of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.


        :param y: The y of this CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey.  # noqa: E501
        :type: str
        """

        self._y = y

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
        if issubclass(CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey, dict):
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
        if not isinstance(other, CertificateCertificateHashResponseDataCertificateSubjectKeyInfoPublicKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
