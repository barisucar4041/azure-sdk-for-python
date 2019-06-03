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


class IoTSecuritySolutionAnalyticsModelDevicesMetricsItem(Model):
    """IoTSecuritySolutionAnalyticsModelDevicesMetricsItem.

    :param date_property: the date of the metrics
    :type date_property: datetime
    :param devices_metrics: devices alerts count by severity.
    :type devices_metrics: ~azure.mgmt.security.models.IoTSeverityMetrics
    """

    _attribute_map = {
        'date_property': {'key': 'date', 'type': 'iso-8601'},
        'devices_metrics': {'key': 'devicesMetrics', 'type': 'IoTSeverityMetrics'},
    }

    def __init__(self, **kwargs):
        super(IoTSecuritySolutionAnalyticsModelDevicesMetricsItem, self).__init__(**kwargs)
        self.date_property = kwargs.get('date_property', None)
        self.devices_metrics = kwargs.get('devices_metrics', None)
