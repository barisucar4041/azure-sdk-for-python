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


class ReplicatorQueueStatus(Model):
    """Provides various statistics of the queue used in the service fabric
    replicator.
    Contains information about the service fabric replicator like the
    replication/copy queue utilization, last acknowledgement received
    timestamp, etc.
    Depending on the role of the replicator, the properties in this type imply
    different meanings.

    :param queue_utilization_percentage: Represents the utilization of the
     queue. A value of 0 indicates that the queue is empty and a value of 100
     indicates the queue is full.
    :type queue_utilization_percentage: int
    :param queue_memory_size: Represents the virtual memory consumed by the
     queue in bytes.
    :type queue_memory_size: str
    :param first_sequence_number: On a primary replicator, this is
     semantically the sequence number of the operation for which all the
     secondary replicas have sent an acknowledgement.
     On a secondary replicator, this is the smallest sequence number of the
     operation that is present in the queue.
    :type first_sequence_number: str
    :param completed_sequence_number: On a primary replicator, this is
     semantically the highest sequence number of the operation for which all
     the secondary replicas have sent an acknowledgement.
     On a secondary replicator, this is semantically the highest sequence
     number that has been applied to the persistent state.
    :type completed_sequence_number: str
    :param committed_sequence_number: On a primary replicator, this is
     semantically the highest sequence number of the operation for which a
     write quorum of the secondary replicas have sent an acknowledgement.
     On a secondary replicator, this is semantically the highest sequence
     number of the in-order operation received from the primary.
    :type committed_sequence_number: str
    :param last_sequence_number: Represents the latest sequence number of the
     operation that is available in the queue.
    :type last_sequence_number: str
    """

    _attribute_map = {
        'queue_utilization_percentage': {'key': 'QueueUtilizationPercentage', 'type': 'int'},
        'queue_memory_size': {'key': 'QueueMemorySize', 'type': 'str'},
        'first_sequence_number': {'key': 'FirstSequenceNumber', 'type': 'str'},
        'completed_sequence_number': {'key': 'CompletedSequenceNumber', 'type': 'str'},
        'committed_sequence_number': {'key': 'CommittedSequenceNumber', 'type': 'str'},
        'last_sequence_number': {'key': 'LastSequenceNumber', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ReplicatorQueueStatus, self).__init__(**kwargs)
        self.queue_utilization_percentage = kwargs.get('queue_utilization_percentage', None)
        self.queue_memory_size = kwargs.get('queue_memory_size', None)
        self.first_sequence_number = kwargs.get('first_sequence_number', None)
        self.completed_sequence_number = kwargs.get('completed_sequence_number', None)
        self.committed_sequence_number = kwargs.get('committed_sequence_number', None)
        self.last_sequence_number = kwargs.get('last_sequence_number', None)