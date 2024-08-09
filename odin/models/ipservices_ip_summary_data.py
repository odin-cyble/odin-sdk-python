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

class IpservicesIPSummaryData(object):
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
        'asn': 'IPASN',
        'asn_updated_at': 'str',
        'banner': 'list[str]',
        'domains': 'list[IPDomain]',
        'hostnames': 'list[IPHostname]',
        'ip': 'str',
        'is_ipv4': 'bool',
        'is_ipv6': 'bool',
        'is_vuln': 'bool',
        'last_updated_at': 'str',
        'location': 'IPLocation',
        'location_updated_at': 'str',
        'scan_id': 'int',
        'services': 'list[IPService]',
        'services_hash': 'str',
        'tags': 'list[IPTag]',
        'whois': 'IPWhois',
        'whois_updated_at': 'str'
    }

    attribute_map = {
        'asn': 'asn',
        'asn_updated_at': 'asn_updated_at',
        'banner': 'banner',
        'domains': 'domains',
        'hostnames': 'hostnames',
        'ip': 'ip',
        'is_ipv4': 'is_ipv4',
        'is_ipv6': 'is_ipv6',
        'is_vuln': 'is_vuln',
        'last_updated_at': 'last_updated_at',
        'location': 'location',
        'location_updated_at': 'location_updated_at',
        'scan_id': 'scan_id',
        'services': 'services',
        'services_hash': 'services_hash',
        'tags': 'tags',
        'whois': 'whois',
        'whois_updated_at': 'whois_updated_at'
    }

    def __init__(self, asn=None, asn_updated_at=None, banner=None, domains=None, hostnames=None, ip=None, is_ipv4=None, is_ipv6=None, is_vuln=None, last_updated_at=None, location=None, location_updated_at=None, scan_id=None, services=None, services_hash=None, tags=None, whois=None, whois_updated_at=None):  # noqa: E501
        """IpservicesIPSummaryData - a model defined in Swagger"""  # noqa: E501
        self._asn = None
        self._asn_updated_at = None
        self._banner = None
        self._domains = None
        self._hostnames = None
        self._ip = None
        self._is_ipv4 = None
        self._is_ipv6 = None
        self._is_vuln = None
        self._last_updated_at = None
        self._location = None
        self._location_updated_at = None
        self._scan_id = None
        self._services = None
        self._services_hash = None
        self._tags = None
        self._whois = None
        self._whois_updated_at = None
        self.discriminator = None
        if asn is not None:
            self.asn = asn
        if asn_updated_at is not None:
            self.asn_updated_at = asn_updated_at
        if banner is not None:
            self.banner = banner
        if domains is not None:
            self.domains = domains
        if hostnames is not None:
            self.hostnames = hostnames
        if ip is not None:
            self.ip = ip
        if is_ipv4 is not None:
            self.is_ipv4 = is_ipv4
        if is_ipv6 is not None:
            self.is_ipv6 = is_ipv6
        if is_vuln is not None:
            self.is_vuln = is_vuln
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if location is not None:
            self.location = location
        if location_updated_at is not None:
            self.location_updated_at = location_updated_at
        if scan_id is not None:
            self.scan_id = scan_id
        if services is not None:
            self.services = services
        if services_hash is not None:
            self.services_hash = services_hash
        if tags is not None:
            self.tags = tags
        if whois is not None:
            self.whois = whois
        if whois_updated_at is not None:
            self.whois_updated_at = whois_updated_at

    @property
    def asn(self):
        """Gets the asn of this IpservicesIPSummaryData.  # noqa: E501


        :return: The asn of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: IPASN
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this IpservicesIPSummaryData.


        :param asn: The asn of this IpservicesIPSummaryData.  # noqa: E501
        :type: IPASN
        """

        self._asn = asn

    @property
    def asn_updated_at(self):
        """Gets the asn_updated_at of this IpservicesIPSummaryData.  # noqa: E501


        :return: The asn_updated_at of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: str
        """
        return self._asn_updated_at

    @asn_updated_at.setter
    def asn_updated_at(self, asn_updated_at):
        """Sets the asn_updated_at of this IpservicesIPSummaryData.


        :param asn_updated_at: The asn_updated_at of this IpservicesIPSummaryData.  # noqa: E501
        :type: str
        """

        self._asn_updated_at = asn_updated_at

    @property
    def banner(self):
        """Gets the banner of this IpservicesIPSummaryData.  # noqa: E501


        :return: The banner of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: list[str]
        """
        return self._banner

    @banner.setter
    def banner(self, banner):
        """Sets the banner of this IpservicesIPSummaryData.


        :param banner: The banner of this IpservicesIPSummaryData.  # noqa: E501
        :type: list[str]
        """

        self._banner = banner

    @property
    def domains(self):
        """Gets the domains of this IpservicesIPSummaryData.  # noqa: E501


        :return: The domains of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: list[IPDomain]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this IpservicesIPSummaryData.


        :param domains: The domains of this IpservicesIPSummaryData.  # noqa: E501
        :type: list[IPDomain]
        """

        self._domains = domains

    @property
    def hostnames(self):
        """Gets the hostnames of this IpservicesIPSummaryData.  # noqa: E501


        :return: The hostnames of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: list[IPHostname]
        """
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        """Sets the hostnames of this IpservicesIPSummaryData.


        :param hostnames: The hostnames of this IpservicesIPSummaryData.  # noqa: E501
        :type: list[IPHostname]
        """

        self._hostnames = hostnames

    @property
    def ip(self):
        """Gets the ip of this IpservicesIPSummaryData.  # noqa: E501


        :return: The ip of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this IpservicesIPSummaryData.


        :param ip: The ip of this IpservicesIPSummaryData.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def is_ipv4(self):
        """Gets the is_ipv4 of this IpservicesIPSummaryData.  # noqa: E501


        :return: The is_ipv4 of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: bool
        """
        return self._is_ipv4

    @is_ipv4.setter
    def is_ipv4(self, is_ipv4):
        """Sets the is_ipv4 of this IpservicesIPSummaryData.


        :param is_ipv4: The is_ipv4 of this IpservicesIPSummaryData.  # noqa: E501
        :type: bool
        """

        self._is_ipv4 = is_ipv4

    @property
    def is_ipv6(self):
        """Gets the is_ipv6 of this IpservicesIPSummaryData.  # noqa: E501


        :return: The is_ipv6 of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: bool
        """
        return self._is_ipv6

    @is_ipv6.setter
    def is_ipv6(self, is_ipv6):
        """Sets the is_ipv6 of this IpservicesIPSummaryData.


        :param is_ipv6: The is_ipv6 of this IpservicesIPSummaryData.  # noqa: E501
        :type: bool
        """

        self._is_ipv6 = is_ipv6

    @property
    def is_vuln(self):
        """Gets the is_vuln of this IpservicesIPSummaryData.  # noqa: E501


        :return: The is_vuln of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: bool
        """
        return self._is_vuln

    @is_vuln.setter
    def is_vuln(self, is_vuln):
        """Sets the is_vuln of this IpservicesIPSummaryData.


        :param is_vuln: The is_vuln of this IpservicesIPSummaryData.  # noqa: E501
        :type: bool
        """

        self._is_vuln = is_vuln

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this IpservicesIPSummaryData.  # noqa: E501


        :return: The last_updated_at of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this IpservicesIPSummaryData.


        :param last_updated_at: The last_updated_at of this IpservicesIPSummaryData.  # noqa: E501
        :type: str
        """

        self._last_updated_at = last_updated_at

    @property
    def location(self):
        """Gets the location of this IpservicesIPSummaryData.  # noqa: E501


        :return: The location of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: IPLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this IpservicesIPSummaryData.


        :param location: The location of this IpservicesIPSummaryData.  # noqa: E501
        :type: IPLocation
        """

        self._location = location

    @property
    def location_updated_at(self):
        """Gets the location_updated_at of this IpservicesIPSummaryData.  # noqa: E501


        :return: The location_updated_at of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: str
        """
        return self._location_updated_at

    @location_updated_at.setter
    def location_updated_at(self, location_updated_at):
        """Sets the location_updated_at of this IpservicesIPSummaryData.


        :param location_updated_at: The location_updated_at of this IpservicesIPSummaryData.  # noqa: E501
        :type: str
        """

        self._location_updated_at = location_updated_at

    @property
    def scan_id(self):
        """Gets the scan_id of this IpservicesIPSummaryData.  # noqa: E501


        :return: The scan_id of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: int
        """
        return self._scan_id

    @scan_id.setter
    def scan_id(self, scan_id):
        """Sets the scan_id of this IpservicesIPSummaryData.


        :param scan_id: The scan_id of this IpservicesIPSummaryData.  # noqa: E501
        :type: int
        """

        self._scan_id = scan_id

    @property
    def services(self):
        """Gets the services of this IpservicesIPSummaryData.  # noqa: E501


        :return: The services of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: list[IPService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this IpservicesIPSummaryData.


        :param services: The services of this IpservicesIPSummaryData.  # noqa: E501
        :type: list[IPService]
        """

        self._services = services

    @property
    def services_hash(self):
        """Gets the services_hash of this IpservicesIPSummaryData.  # noqa: E501


        :return: The services_hash of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: str
        """
        return self._services_hash

    @services_hash.setter
    def services_hash(self, services_hash):
        """Sets the services_hash of this IpservicesIPSummaryData.


        :param services_hash: The services_hash of this IpservicesIPSummaryData.  # noqa: E501
        :type: str
        """

        self._services_hash = services_hash

    @property
    def tags(self):
        """Gets the tags of this IpservicesIPSummaryData.  # noqa: E501


        :return: The tags of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: list[IPTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this IpservicesIPSummaryData.


        :param tags: The tags of this IpservicesIPSummaryData.  # noqa: E501
        :type: list[IPTag]
        """

        self._tags = tags

    @property
    def whois(self):
        """Gets the whois of this IpservicesIPSummaryData.  # noqa: E501


        :return: The whois of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: IPWhois
        """
        return self._whois

    @whois.setter
    def whois(self, whois):
        """Sets the whois of this IpservicesIPSummaryData.


        :param whois: The whois of this IpservicesIPSummaryData.  # noqa: E501
        :type: IPWhois
        """

        self._whois = whois

    @property
    def whois_updated_at(self):
        """Gets the whois_updated_at of this IpservicesIPSummaryData.  # noqa: E501


        :return: The whois_updated_at of this IpservicesIPSummaryData.  # noqa: E501
        :rtype: str
        """
        return self._whois_updated_at

    @whois_updated_at.setter
    def whois_updated_at(self, whois_updated_at):
        """Sets the whois_updated_at of this IpservicesIPSummaryData.


        :param whois_updated_at: The whois_updated_at of this IpservicesIPSummaryData.  # noqa: E501
        :type: str
        """

        self._whois_updated_at = whois_updated_at

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
        if issubclass(IpservicesIPSummaryData, dict):
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
        if not isinstance(other, IpservicesIPSummaryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
