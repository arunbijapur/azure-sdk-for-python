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


class SasDefinitionAttributes(Model):
    """The SAS definition management attributes.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param enabled: the enabled state of the object.
    :type enabled: bool
    :ivar created: Creation time in UTC.
    :vartype created: datetime
    :ivar updated: Last updated time in UTC.
    :vartype updated: datetime
    :ivar recovery_level: Reflects the deletion recovery level currently in
     effect for SAS definitions in the current vault. If it contains
     'Purgeable' the SAS definition can be permanently deleted by a privileged
     user; otherwise, only the system can purge the SAS definition, at the end
     of the retention interval. Possible values include: 'Purgeable',
     'Recoverable+Purgeable', 'Recoverable',
     'Recoverable+ProtectedSubscription'
    :vartype recovery_level: str or
     ~azure.keyvault.models.DeletionRecoveryLevel
    """

    _validation = {
        'created': {'readonly': True},
        'updated': {'readonly': True},
        'recovery_level': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'created': {'key': 'created', 'type': 'unix-time'},
        'updated': {'key': 'updated', 'type': 'unix-time'},
        'recovery_level': {'key': 'recoveryLevel', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SasDefinitionAttributes, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.created = None
        self.updated = None
        self.recovery_level = None
