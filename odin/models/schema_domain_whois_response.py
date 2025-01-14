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

class SchemaDomainWhoisResponse(object):
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
        'administrative_contact': 'SchemaContact',
        'audited_fields': 'SchemaAudit',
        'billing_contact': 'SchemaContact',
        'created_date': 'str',
        'domain_name': 'str',
        'domain_status': 'list[str]',
        'expires_date': 'str',
        'name_servers': 'list[str]',
        'raw_data': 'str',
        'registrant_contact': 'SchemaContact',
        'registrar': 'SchemaRegistrar',
        'technical_contact': 'SchemaContact',
        'tld': 'str',
        'updated_date': 'str'
    }

    attribute_map = {
        'administrative_contact': 'administrative_contact',
        'audited_fields': 'audited_fields',
        'billing_contact': 'billing_contact',
        'created_date': 'created_date',
        'domain_name': 'domain_name',
        'domain_status': 'domain_status',
        'expires_date': 'expires_date',
        'name_servers': 'name_servers',
        'raw_data': 'raw_data',
        'registrant_contact': 'registrant_contact',
        'registrar': 'registrar',
        'technical_contact': 'technical_contact',
        'tld': 'tld',
        'updated_date': 'updated_date'
    }

    def __init__(self, administrative_contact=None, audited_fields=None, billing_contact=None, created_date=None, domain_name=None, domain_status=None, expires_date=None, name_servers=None, raw_data=None, registrant_contact=None, registrar=None, technical_contact=None, tld=None, updated_date=None):  # noqa: E501
        """SchemaDomainWhoisResponse - a model defined in Swagger"""  # noqa: E501
        self._administrative_contact = None
        self._audited_fields = None
        self._billing_contact = None
        self._created_date = None
        self._domain_name = None
        self._domain_status = None
        self._expires_date = None
        self._name_servers = None
        self._raw_data = None
        self._registrant_contact = None
        self._registrar = None
        self._technical_contact = None
        self._tld = None
        self._updated_date = None
        self.discriminator = None
        if administrative_contact is not None:
            self.administrative_contact = administrative_contact
        if audited_fields is not None:
            self.audited_fields = audited_fields
        if billing_contact is not None:
            self.billing_contact = billing_contact
        if created_date is not None:
            self.created_date = created_date
        if domain_name is not None:
            self.domain_name = domain_name
        if domain_status is not None:
            self.domain_status = domain_status
        if expires_date is not None:
            self.expires_date = expires_date
        if name_servers is not None:
            self.name_servers = name_servers
        if raw_data is not None:
            self.raw_data = raw_data
        if registrant_contact is not None:
            self.registrant_contact = registrant_contact
        if registrar is not None:
            self.registrar = registrar
        if technical_contact is not None:
            self.technical_contact = technical_contact
        if tld is not None:
            self.tld = tld
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def administrative_contact(self):
        """Gets the administrative_contact of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The administrative_contact of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: SchemaContact
        """
        return self._administrative_contact

    @administrative_contact.setter
    def administrative_contact(self, administrative_contact):
        """Sets the administrative_contact of this SchemaDomainWhoisResponse.


        :param administrative_contact: The administrative_contact of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: SchemaContact
        """

        self._administrative_contact = administrative_contact

    @property
    def audited_fields(self):
        """Gets the audited_fields of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The audited_fields of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: SchemaAudit
        """
        return self._audited_fields

    @audited_fields.setter
    def audited_fields(self, audited_fields):
        """Sets the audited_fields of this SchemaDomainWhoisResponse.


        :param audited_fields: The audited_fields of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: SchemaAudit
        """

        self._audited_fields = audited_fields

    @property
    def billing_contact(self):
        """Gets the billing_contact of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The billing_contact of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: SchemaContact
        """
        return self._billing_contact

    @billing_contact.setter
    def billing_contact(self, billing_contact):
        """Sets the billing_contact of this SchemaDomainWhoisResponse.


        :param billing_contact: The billing_contact of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: SchemaContact
        """

        self._billing_contact = billing_contact

    @property
    def created_date(self):
        """Gets the created_date of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The created_date of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this SchemaDomainWhoisResponse.


        :param created_date: The created_date of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def domain_name(self):
        """Gets the domain_name of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The domain_name of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this SchemaDomainWhoisResponse.


        :param domain_name: The domain_name of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def domain_status(self):
        """Gets the domain_status of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The domain_status of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        """Sets the domain_status of this SchemaDomainWhoisResponse.


        :param domain_status: The domain_status of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: list[str]
        """

        self._domain_status = domain_status

    @property
    def expires_date(self):
        """Gets the expires_date of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The expires_date of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: str
        """
        return self._expires_date

    @expires_date.setter
    def expires_date(self, expires_date):
        """Sets the expires_date of this SchemaDomainWhoisResponse.


        :param expires_date: The expires_date of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: str
        """

        self._expires_date = expires_date

    @property
    def name_servers(self):
        """Gets the name_servers of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The name_servers of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._name_servers

    @name_servers.setter
    def name_servers(self, name_servers):
        """Sets the name_servers of this SchemaDomainWhoisResponse.


        :param name_servers: The name_servers of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: list[str]
        """

        self._name_servers = name_servers

    @property
    def raw_data(self):
        """Gets the raw_data of this SchemaDomainWhoisResponse.  # noqa: E501

        IngestedAt            time.Time  `json:\"ingested_at\"`  # noqa: E501

        :return: The raw_data of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: str
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this SchemaDomainWhoisResponse.

        IngestedAt            time.Time  `json:\"ingested_at\"`  # noqa: E501

        :param raw_data: The raw_data of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: str
        """

        self._raw_data = raw_data

    @property
    def registrant_contact(self):
        """Gets the registrant_contact of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The registrant_contact of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: SchemaContact
        """
        return self._registrant_contact

    @registrant_contact.setter
    def registrant_contact(self, registrant_contact):
        """Sets the registrant_contact of this SchemaDomainWhoisResponse.


        :param registrant_contact: The registrant_contact of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: SchemaContact
        """

        self._registrant_contact = registrant_contact

    @property
    def registrar(self):
        """Gets the registrar of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The registrar of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: SchemaRegistrar
        """
        return self._registrar

    @registrar.setter
    def registrar(self, registrar):
        """Sets the registrar of this SchemaDomainWhoisResponse.


        :param registrar: The registrar of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: SchemaRegistrar
        """

        self._registrar = registrar

    @property
    def technical_contact(self):
        """Gets the technical_contact of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The technical_contact of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: SchemaContact
        """
        return self._technical_contact

    @technical_contact.setter
    def technical_contact(self, technical_contact):
        """Sets the technical_contact of this SchemaDomainWhoisResponse.


        :param technical_contact: The technical_contact of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: SchemaContact
        """

        self._technical_contact = technical_contact

    @property
    def tld(self):
        """Gets the tld of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The tld of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: str
        """
        return self._tld

    @tld.setter
    def tld(self, tld):
        """Sets the tld of this SchemaDomainWhoisResponse.


        :param tld: The tld of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: str
        """

        self._tld = tld

    @property
    def updated_date(self):
        """Gets the updated_date of this SchemaDomainWhoisResponse.  # noqa: E501


        :return: The updated_date of this SchemaDomainWhoisResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this SchemaDomainWhoisResponse.


        :param updated_date: The updated_date of this SchemaDomainWhoisResponse.  # noqa: E501
        :type: str
        """

        self._updated_date = updated_date

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
        if issubclass(SchemaDomainWhoisResponse, dict):
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
        if not isinstance(other, SchemaDomainWhoisResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
