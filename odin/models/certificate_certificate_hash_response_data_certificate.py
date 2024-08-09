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

class CertificateCertificateHashResponseDataCertificate(object):
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
        'extensions': 'CertificateCertificateHashResponseDataCertificateExtensions',
        'fingerprint_md5': 'str',
        'fingerprint_sha1': 'str',
        'fingerprint_sha256': 'str',
        'issuer': 'CertificateCertificateHashResponseDataCertificateIssuer',
        'redacted': 'bool',
        'serial_number': 'str',
        'signature': 'CertificateCertificateHashResponseDataCertificateSignature',
        'subject': 'CertificateCertificateHashResponseDataCertificateSubject',
        'subject_alt_name': 'CertificateCertificateHashResponseDataCertificateSubjectAltName',
        'subject_key_info': 'CertificateCertificateHashResponseDataCertificateSubjectKeyInfo',
        'tbs_fingerprint': 'str',
        'validation_level': 'str',
        'validity': 'CertificateCertificateHashResponseDataCertificateValidity',
        'version': 'int'
    }

    attribute_map = {
        'extensions': 'extensions',
        'fingerprint_md5': 'fingerprint_md5',
        'fingerprint_sha1': 'fingerprint_sha1',
        'fingerprint_sha256': 'fingerprint_sha256',
        'issuer': 'issuer',
        'redacted': 'redacted',
        'serial_number': 'serial_number',
        'signature': 'signature',
        'subject': 'subject',
        'subject_alt_name': 'subject_alt_name',
        'subject_key_info': 'subject_key_info',
        'tbs_fingerprint': 'tbs_fingerprint',
        'validation_level': 'validation_level',
        'validity': 'validity',
        'version': 'version'
    }

    def __init__(self, extensions=None, fingerprint_md5=None, fingerprint_sha1=None, fingerprint_sha256=None, issuer=None, redacted=None, serial_number=None, signature=None, subject=None, subject_alt_name=None, subject_key_info=None, tbs_fingerprint=None, validation_level=None, validity=None, version=None):  # noqa: E501
        """CertificateCertificateHashResponseDataCertificate - a model defined in Swagger"""  # noqa: E501
        self._extensions = None
        self._fingerprint_md5 = None
        self._fingerprint_sha1 = None
        self._fingerprint_sha256 = None
        self._issuer = None
        self._redacted = None
        self._serial_number = None
        self._signature = None
        self._subject = None
        self._subject_alt_name = None
        self._subject_key_info = None
        self._tbs_fingerprint = None
        self._validation_level = None
        self._validity = None
        self._version = None
        self.discriminator = None
        if extensions is not None:
            self.extensions = extensions
        if fingerprint_md5 is not None:
            self.fingerprint_md5 = fingerprint_md5
        if fingerprint_sha1 is not None:
            self.fingerprint_sha1 = fingerprint_sha1
        if fingerprint_sha256 is not None:
            self.fingerprint_sha256 = fingerprint_sha256
        if issuer is not None:
            self.issuer = issuer
        if redacted is not None:
            self.redacted = redacted
        if serial_number is not None:
            self.serial_number = serial_number
        if signature is not None:
            self.signature = signature
        if subject is not None:
            self.subject = subject
        if subject_alt_name is not None:
            self.subject_alt_name = subject_alt_name
        if subject_key_info is not None:
            self.subject_key_info = subject_key_info
        if tbs_fingerprint is not None:
            self.tbs_fingerprint = tbs_fingerprint
        if validation_level is not None:
            self.validation_level = validation_level
        if validity is not None:
            self.validity = validity
        if version is not None:
            self.version = version

    @property
    def extensions(self):
        """Gets the extensions of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The extensions of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: CertificateCertificateHashResponseDataCertificateExtensions
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this CertificateCertificateHashResponseDataCertificate.


        :param extensions: The extensions of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: CertificateCertificateHashResponseDataCertificateExtensions
        """

        self._extensions = extensions

    @property
    def fingerprint_md5(self):
        """Gets the fingerprint_md5 of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The fingerprint_md5 of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint_md5

    @fingerprint_md5.setter
    def fingerprint_md5(self, fingerprint_md5):
        """Sets the fingerprint_md5 of this CertificateCertificateHashResponseDataCertificate.


        :param fingerprint_md5: The fingerprint_md5 of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: str
        """

        self._fingerprint_md5 = fingerprint_md5

    @property
    def fingerprint_sha1(self):
        """Gets the fingerprint_sha1 of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The fingerprint_sha1 of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint_sha1

    @fingerprint_sha1.setter
    def fingerprint_sha1(self, fingerprint_sha1):
        """Sets the fingerprint_sha1 of this CertificateCertificateHashResponseDataCertificate.


        :param fingerprint_sha1: The fingerprint_sha1 of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: str
        """

        self._fingerprint_sha1 = fingerprint_sha1

    @property
    def fingerprint_sha256(self):
        """Gets the fingerprint_sha256 of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The fingerprint_sha256 of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint_sha256

    @fingerprint_sha256.setter
    def fingerprint_sha256(self, fingerprint_sha256):
        """Sets the fingerprint_sha256 of this CertificateCertificateHashResponseDataCertificate.


        :param fingerprint_sha256: The fingerprint_sha256 of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: str
        """

        self._fingerprint_sha256 = fingerprint_sha256

    @property
    def issuer(self):
        """Gets the issuer of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The issuer of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: CertificateCertificateHashResponseDataCertificateIssuer
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CertificateCertificateHashResponseDataCertificate.


        :param issuer: The issuer of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: CertificateCertificateHashResponseDataCertificateIssuer
        """

        self._issuer = issuer

    @property
    def redacted(self):
        """Gets the redacted of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The redacted of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this CertificateCertificateHashResponseDataCertificate.


        :param redacted: The redacted of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: bool
        """

        self._redacted = redacted

    @property
    def serial_number(self):
        """Gets the serial_number of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The serial_number of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this CertificateCertificateHashResponseDataCertificate.


        :param serial_number: The serial_number of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def signature(self):
        """Gets the signature of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The signature of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: CertificateCertificateHashResponseDataCertificateSignature
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this CertificateCertificateHashResponseDataCertificate.


        :param signature: The signature of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: CertificateCertificateHashResponseDataCertificateSignature
        """

        self._signature = signature

    @property
    def subject(self):
        """Gets the subject of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The subject of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: CertificateCertificateHashResponseDataCertificateSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CertificateCertificateHashResponseDataCertificate.


        :param subject: The subject of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: CertificateCertificateHashResponseDataCertificateSubject
        """

        self._subject = subject

    @property
    def subject_alt_name(self):
        """Gets the subject_alt_name of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The subject_alt_name of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: CertificateCertificateHashResponseDataCertificateSubjectAltName
        """
        return self._subject_alt_name

    @subject_alt_name.setter
    def subject_alt_name(self, subject_alt_name):
        """Sets the subject_alt_name of this CertificateCertificateHashResponseDataCertificate.


        :param subject_alt_name: The subject_alt_name of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: CertificateCertificateHashResponseDataCertificateSubjectAltName
        """

        self._subject_alt_name = subject_alt_name

    @property
    def subject_key_info(self):
        """Gets the subject_key_info of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The subject_key_info of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: CertificateCertificateHashResponseDataCertificateSubjectKeyInfo
        """
        return self._subject_key_info

    @subject_key_info.setter
    def subject_key_info(self, subject_key_info):
        """Sets the subject_key_info of this CertificateCertificateHashResponseDataCertificate.


        :param subject_key_info: The subject_key_info of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: CertificateCertificateHashResponseDataCertificateSubjectKeyInfo
        """

        self._subject_key_info = subject_key_info

    @property
    def tbs_fingerprint(self):
        """Gets the tbs_fingerprint of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The tbs_fingerprint of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: str
        """
        return self._tbs_fingerprint

    @tbs_fingerprint.setter
    def tbs_fingerprint(self, tbs_fingerprint):
        """Sets the tbs_fingerprint of this CertificateCertificateHashResponseDataCertificate.


        :param tbs_fingerprint: The tbs_fingerprint of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: str
        """

        self._tbs_fingerprint = tbs_fingerprint

    @property
    def validation_level(self):
        """Gets the validation_level of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The validation_level of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: str
        """
        return self._validation_level

    @validation_level.setter
    def validation_level(self, validation_level):
        """Sets the validation_level of this CertificateCertificateHashResponseDataCertificate.


        :param validation_level: The validation_level of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: str
        """

        self._validation_level = validation_level

    @property
    def validity(self):
        """Gets the validity of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The validity of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: CertificateCertificateHashResponseDataCertificateValidity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this CertificateCertificateHashResponseDataCertificate.


        :param validity: The validity of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: CertificateCertificateHashResponseDataCertificateValidity
        """

        self._validity = validity

    @property
    def version(self):
        """Gets the version of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501


        :return: The version of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CertificateCertificateHashResponseDataCertificate.


        :param version: The version of this CertificateCertificateHashResponseDataCertificate.  # noqa: E501
        :type: int
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
        if issubclass(CertificateCertificateHashResponseDataCertificate, dict):
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
        if not isinstance(other, CertificateCertificateHashResponseDataCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
