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


class TrackingEventsDefinition(Model):
    """TrackingEventsDefinition.

    All required parameters must be populated in order to send to Azure.

    :param source_type: Required.
    :type source_type: str
    :param track_events_options: Possible values include: 'None',
     'DisableSourceInfoEnrich'
    :type track_events_options: str or
     ~azure.mgmt.logic.models.TrackEventsOperationOptions
    :param events: Required.
    :type events: list[~azure.mgmt.logic.models.TrackingEvent]
    """

    _validation = {
        'source_type': {'required': True},
        'events': {'required': True},
    }

    _attribute_map = {
        'source_type': {'key': 'sourceType', 'type': 'str'},
        'track_events_options': {'key': 'trackEventsOptions', 'type': 'str'},
        'events': {'key': 'events', 'type': '[TrackingEvent]'},
    }

    def __init__(self, **kwargs):
        super(TrackingEventsDefinition, self).__init__(**kwargs)
        self.source_type = kwargs.get('source_type', None)
        self.track_events_options = kwargs.get('track_events_options', None)
        self.events = kwargs.get('events', None)
