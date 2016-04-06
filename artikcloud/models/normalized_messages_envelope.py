# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class NormalizedMessagesEnvelope(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NormalizedMessagesEnvelope - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sdids': 'str',
            'sdid': 'str',
            'uid': 'str',
            'start_date': 'int',
            'end_date': 'int',
            'order': 'str',
            'next': 'str',
            'count': 'int',
            'size': 'int',
            'data': 'list[NormalizedMessage]'
        }

        self.attribute_map = {
            'sdids': 'sdids',
            'sdid': 'sdid',
            'uid': 'uid',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'order': 'order',
            'next': 'next',
            'count': 'count',
            'size': 'size',
            'data': 'data'
        }

        self._sdids = None
        self._sdid = None
        self._uid = None
        self._start_date = None
        self._end_date = None
        self._order = None
        self._next = None
        self._count = None
        self._size = None
        self._data = None

    @property
    def sdids(self):
        """
        Gets the sdids of this NormalizedMessagesEnvelope.


        :return: The sdids of this NormalizedMessagesEnvelope.
        :rtype: str
        """
        return self._sdids

    @sdids.setter
    def sdids(self, sdids):
        """
        Sets the sdids of this NormalizedMessagesEnvelope.


        :param sdids: The sdids of this NormalizedMessagesEnvelope.
        :type: str
        """
        self._sdids = sdids

    @property
    def sdid(self):
        """
        Gets the sdid of this NormalizedMessagesEnvelope.


        :return: The sdid of this NormalizedMessagesEnvelope.
        :rtype: str
        """
        return self._sdid

    @sdid.setter
    def sdid(self, sdid):
        """
        Sets the sdid of this NormalizedMessagesEnvelope.


        :param sdid: The sdid of this NormalizedMessagesEnvelope.
        :type: str
        """
        self._sdid = sdid

    @property
    def uid(self):
        """
        Gets the uid of this NormalizedMessagesEnvelope.


        :return: The uid of this NormalizedMessagesEnvelope.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this NormalizedMessagesEnvelope.


        :param uid: The uid of this NormalizedMessagesEnvelope.
        :type: str
        """
        self._uid = uid

    @property
    def start_date(self):
        """
        Gets the start_date of this NormalizedMessagesEnvelope.


        :return: The start_date of this NormalizedMessagesEnvelope.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this NormalizedMessagesEnvelope.


        :param start_date: The start_date of this NormalizedMessagesEnvelope.
        :type: int
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this NormalizedMessagesEnvelope.


        :return: The end_date of this NormalizedMessagesEnvelope.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this NormalizedMessagesEnvelope.


        :param end_date: The end_date of this NormalizedMessagesEnvelope.
        :type: int
        """
        self._end_date = end_date

    @property
    def order(self):
        """
        Gets the order of this NormalizedMessagesEnvelope.


        :return: The order of this NormalizedMessagesEnvelope.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this NormalizedMessagesEnvelope.


        :param order: The order of this NormalizedMessagesEnvelope.
        :type: str
        """
        self._order = order

    @property
    def next(self):
        """
        Gets the next of this NormalizedMessagesEnvelope.


        :return: The next of this NormalizedMessagesEnvelope.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this NormalizedMessagesEnvelope.


        :param next: The next of this NormalizedMessagesEnvelope.
        :type: str
        """
        self._next = next

    @property
    def count(self):
        """
        Gets the count of this NormalizedMessagesEnvelope.


        :return: The count of this NormalizedMessagesEnvelope.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this NormalizedMessagesEnvelope.


        :param count: The count of this NormalizedMessagesEnvelope.
        :type: int
        """
        self._count = count

    @property
    def size(self):
        """
        Gets the size of this NormalizedMessagesEnvelope.


        :return: The size of this NormalizedMessagesEnvelope.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this NormalizedMessagesEnvelope.


        :param size: The size of this NormalizedMessagesEnvelope.
        :type: int
        """
        self._size = size

    @property
    def data(self):
        """
        Gets the data of this NormalizedMessagesEnvelope.


        :return: The data of this NormalizedMessagesEnvelope.
        :rtype: list[NormalizedMessage]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this NormalizedMessagesEnvelope.


        :param data: The data of this NormalizedMessagesEnvelope.
        :type: list[NormalizedMessage]
        """
        self._data = data

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
