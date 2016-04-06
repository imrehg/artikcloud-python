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


class DevicesEnvelope(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DevicesEnvelope - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total': 'int',
            'count': 'int',
            'offset': 'int',
            'data': 'DeviceArray'
        }

        self.attribute_map = {
            'total': 'total',
            'count': 'count',
            'offset': 'offset',
            'data': 'data'
        }

        self._total = None
        self._count = None
        self._offset = None
        self._data = None

    @property
    def total(self):
        """
        Gets the total of this DevicesEnvelope.


        :return: The total of this DevicesEnvelope.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this DevicesEnvelope.


        :param total: The total of this DevicesEnvelope.
        :type: int
        """
        self._total = total

    @property
    def count(self):
        """
        Gets the count of this DevicesEnvelope.


        :return: The count of this DevicesEnvelope.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this DevicesEnvelope.


        :param count: The count of this DevicesEnvelope.
        :type: int
        """
        self._count = count

    @property
    def offset(self):
        """
        Gets the offset of this DevicesEnvelope.


        :return: The offset of this DevicesEnvelope.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this DevicesEnvelope.


        :param offset: The offset of this DevicesEnvelope.
        :type: int
        """
        self._offset = offset

    @property
    def data(self):
        """
        Gets the data of this DevicesEnvelope.


        :return: The data of this DevicesEnvelope.
        :rtype: DeviceArray
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this DevicesEnvelope.


        :param data: The data of this DevicesEnvelope.
        :type: DeviceArray
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
