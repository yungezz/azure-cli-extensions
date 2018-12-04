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


class ManagedClusterAddonProfile(Model):
    """A Kubernetes add-on profile for a managed cluster.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Whether the add-on is enabled or not.
    :type enabled: bool
    :param config: Key-value pairs for configuring an add-on.
    :type config: dict[str, str]
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'config': {'key': 'config', 'type': '{str}'},
    }

    def __init__(self, *, enabled: bool, config=None, **kwargs) -> None:
        super(ManagedClusterAddonProfile, self).__init__(**kwargs)
        self.enabled = enabled
        self.config = config