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


class AdvancedScheduleMonthlyOccurrence(Model):
    """The properties of the create advanced schedule monthly occurrence.

    :param occurrence: Occurrence of the week within the month. Must be
     between 1 and 5
    :type occurrence: int
    :param day: Day of the occurrence. Must be one of monday, tuesday,
     wednesday, thursday, friday, saturday, sunday. Possible values include:
     'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
     'Sunday'
    :type day: str or ~azure.mgmt.automation.models.ScheduleDay
    """

    _attribute_map = {
        'occurrence': {'key': 'occurrence', 'type': 'int'},
        'day': {'key': 'day', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdvancedScheduleMonthlyOccurrence, self).__init__(**kwargs)
        self.occurrence = kwargs.get('occurrence', None)
        self.day = kwargs.get('day', None)
