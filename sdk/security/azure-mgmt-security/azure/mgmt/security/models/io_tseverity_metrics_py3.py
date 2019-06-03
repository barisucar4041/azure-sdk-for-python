# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IoTSeverityMetrics(Model):
    """Severity metrics.

    :param high: count of high severity items
    :type high: int
    :param medium: count of medium severity items
    :type medium: int
    :param low: count of low severity items
    :type low: int
    """

    _attribute_map = {
        'high': {'key': 'high', 'type': 'int'},
        'medium': {'key': 'medium', 'type': 'int'},
        'low': {'key': 'low', 'type': 'int'},
    }

    def __init__(self, *, high: int=None, medium: int=None, low: int=None, **kwargs) -> None:
        super(IoTSeverityMetrics, self).__init__(**kwargs)
        self.high = high
        self.medium = medium
        self.low = low
