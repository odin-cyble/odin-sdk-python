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

class SchemaContact(object):
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
        'address': 'str',
        'city': 'str',
        'company': 'str',
        'country': 'str',
        'country_code': 'str',
        'email': 'str',
        'email_domain': 'str',
        'fax': 'str',
        'name': 'str',
        'phone': 'str',
        'state': 'str',
        'zip': 'str'
    }

    attribute_map = {
        'address': 'address',
        'city': 'city',
        'company': 'company',
        'country': 'country',
        'country_code': 'country_code',
        'email': 'email',
        'email_domain': 'email_domain',
        'fax': 'fax',
        'name': 'name',
        'phone': 'phone',
        'state': 'state',
        'zip': 'zip'
    }

    def __init__(self, address=None, city=None, company=None, country=None, country_code=None, email=None, email_domain=None, fax=None, name=None, phone=None, state=None, zip=None):  # noqa: E501
        """SchemaContact - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._city = None
        self._company = None
        self._country = None
        self._country_code = None
        self._email = None
        self._email_domain = None
        self._fax = None
        self._name = None
        self._phone = None
        self._state = None
        self._zip = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if company is not None:
            self.company = company
        if country is not None:
            self.country = country
        if country_code is not None:
            self.country_code = country_code
        if email is not None:
            self.email = email
        if email_domain is not None:
            self.email_domain = email_domain
        if fax is not None:
            self.fax = fax
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip

    @property
    def address(self):
        """Gets the address of this SchemaContact.  # noqa: E501


        :return: The address of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SchemaContact.


        :param address: The address of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this SchemaContact.  # noqa: E501


        :return: The city of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SchemaContact.


        :param city: The city of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def company(self):
        """Gets the company of this SchemaContact.  # noqa: E501


        :return: The company of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this SchemaContact.


        :param company: The company of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def country(self):
        """Gets the country of this SchemaContact.  # noqa: E501


        :return: The country of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SchemaContact.


        :param country: The country of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def country_code(self):
        """Gets the country_code of this SchemaContact.  # noqa: E501


        :return: The country_code of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this SchemaContact.


        :param country_code: The country_code of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def email(self):
        """Gets the email of this SchemaContact.  # noqa: E501


        :return: The email of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SchemaContact.


        :param email: The email of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_domain(self):
        """Gets the email_domain of this SchemaContact.  # noqa: E501


        :return: The email_domain of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._email_domain

    @email_domain.setter
    def email_domain(self, email_domain):
        """Sets the email_domain of this SchemaContact.


        :param email_domain: The email_domain of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._email_domain = email_domain

    @property
    def fax(self):
        """Gets the fax of this SchemaContact.  # noqa: E501


        :return: The fax of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this SchemaContact.


        :param fax: The fax of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def name(self):
        """Gets the name of this SchemaContact.  # noqa: E501


        :return: The name of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SchemaContact.


        :param name: The name of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this SchemaContact.  # noqa: E501


        :return: The phone of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SchemaContact.


        :param phone: The phone of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def state(self):
        """Gets the state of this SchemaContact.  # noqa: E501


        :return: The state of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SchemaContact.


        :param state: The state of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this SchemaContact.  # noqa: E501


        :return: The zip of this SchemaContact.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this SchemaContact.


        :param zip: The zip of this SchemaContact.  # noqa: E501
        :type: str
        """

        self._zip = zip

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
        if issubclass(SchemaContact, dict):
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
        if not isinstance(other, SchemaContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
