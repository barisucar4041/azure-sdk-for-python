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


class IoTSecuritySolutionAnalyticsModel(Model):
    """Security Analytics of a security solution.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar metrics: Security Analytics of a security solution
    :vartype metrics: ~azure.mgmt.security.models.IoTSeverityMetrics
    :ivar unhealthy_devices: number of unhealthy devices
    :vartype unhealthy_devices: int
    :param devices_metrics: The list of devices metrics by the aggregated
     date.
    :type devices_metrics:
     list[~azure.mgmt.security.models.IoTSecuritySolutionAnalyticsModelDevicesMetricsItem]
    :param top_alerted_devices: The list of devices with the most attacked.
    :type top_alerted_devices:
     list[~azure.mgmt.security.models.IoTSecurityDeviceAlerts]
    :param most_prevalent_devices: The list of most prevalent devices.
    :type most_prevalent_devices:
     list[~azure.mgmt.security.models.IoTSecurityDeviceAlerts]
    """

    _validation = {
        'metrics': {'readonly': True},
        'unhealthy_devices': {'readonly': True},
    }

    _attribute_map = {
        'metrics': {'key': 'metrics', 'type': 'IoTSeverityMetrics'},
        'unhealthy_devices': {'key': 'unhealthyDevices', 'type': 'int'},
        'devices_metrics': {'key': 'devicesMetrics', 'type': '[IoTSecuritySolutionAnalyticsModelDevicesMetricsItem]'},
        'top_alerted_devices': {'key': 'topAlertedDevices', 'type': '[IoTSecurityDeviceAlerts]'},
        'most_prevalent_devices': {'key': 'mostPrevalentDevices', 'type': '[IoTSecurityDeviceAlerts]'},
    }

    def __init__(self, *, devices_metrics=None, top_alerted_devices=None, most_prevalent_devices=None, **kwargs) -> None:
        super(IoTSecuritySolutionAnalyticsModel, self).__init__(**kwargs)
        self.metrics = None
        self.unhealthy_devices = None
        self.devices_metrics = devices_metrics
        self.top_alerted_devices = top_alerted_devices
        self.most_prevalent_devices = most_prevalent_devices
