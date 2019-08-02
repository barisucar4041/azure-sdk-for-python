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


class DashboardParts(Model):
    """A dashboard part.

    All required parameters must be populated in order to send to Azure.

    :param position: Required. The dashboard's part position.
    :type position: ~microsoft.portal.models.DashboardPartsPosition
    :param metadata: The dashboard part's metadata.
    :type metadata: dict[str, object]
    """

    _validation = {
        'position': {'required': True},
    }

    _attribute_map = {
        'position': {'key': 'position', 'type': 'DashboardPartsPosition'},
        'metadata': {'key': 'metadata', 'type': '{object}'},
    }

    def __init__(self, *, position, metadata=None, **kwargs) -> None:
        super(DashboardParts, self).__init__(**kwargs)
        self.position = position
        self.metadata = metadata