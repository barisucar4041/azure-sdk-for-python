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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import MicrosoftSerialConsoleClientConfiguration
from .operations import MicrosoftSerialConsoleClientOperationsMixin
from . import models


class MicrosoftSerialConsoleClient(MicrosoftSerialConsoleClientOperationsMixin, SDKClient):
    """The Azure Serial Console allows you to access the serial console of a Virtual Machine or VM scale set instance

    :ivar config: Configuration for client.
    :vartype config: MicrosoftSerialConsoleClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription ID which uniquely identifies the
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call requiring it.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = MicrosoftSerialConsoleClientConfiguration(credentials, subscription_id, base_url)
        super(MicrosoftSerialConsoleClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-05-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
