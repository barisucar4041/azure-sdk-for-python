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


class FeatureInfoObject(Model):
    """The base class Features-related response objects inherit from.

    :param id: A six-digit ID used for Features.
    :type id: int
    :param name: The name of the Feature.
    :type name: str
    :param is_active: Indicates if the feature is enabled.
    :type is_active: bool
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'is_active': {'key': 'isActive', 'type': 'bool'},
    }

    def __init__(self, *, id: int=None, name: str=None, is_active: bool=None, **kwargs) -> None:
        super(FeatureInfoObject, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.is_active = is_active