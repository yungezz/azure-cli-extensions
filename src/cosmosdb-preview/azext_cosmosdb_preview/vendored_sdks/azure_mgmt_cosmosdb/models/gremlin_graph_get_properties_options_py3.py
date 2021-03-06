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

from .options_resource_py3 import OptionsResource


class GremlinGraphGetPropertiesOptions(OptionsResource):
    """GremlinGraphGetPropertiesOptions.

    :param throughput: Value of the Cosmos DB resource throughput or
     autoscaleSettings. Use the ThroughputSetting resource when retrieving
     offer details.
    :type throughput: int
    :param autoscale_settings: Specifies the Autoscale settings.
    :type autoscale_settings: ~azure.mgmt.cosmosdb.models.AutoscaleSettings
    """

    _attribute_map = {
        'throughput': {'key': 'throughput', 'type': 'int'},
        'autoscale_settings': {'key': 'autoscaleSettings', 'type': 'AutoscaleSettings'},
    }

    def __init__(self, *, throughput: int=None, autoscale_settings=None, **kwargs) -> None:
        super(GremlinGraphGetPropertiesOptions, self).__init__(throughput=throughput, autoscale_settings=autoscale_settings, **kwargs)
