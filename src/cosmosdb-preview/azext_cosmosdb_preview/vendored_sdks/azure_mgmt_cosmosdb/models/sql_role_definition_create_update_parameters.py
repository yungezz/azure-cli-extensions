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


class SqlRoleDefinitionCreateUpdateParameters(Model):
    """Parameters to create and update an Azure Cosmos DB SQL Role Definition.

    :param role_name: A user-friendly name for the Role Definition. Must be
     unique for the database account.
    :type role_name: str
    :param type: Indicates whether the Role Definition was built-in or user
     created. Possible values include: 'BuiltInRole', 'CustomRole'
    :type type: str or ~azure.mgmt.cosmosdb.models.RoleDefinitionType
    :param assignable_scopes: A set of fully qualified Scopes at or below
     which Role Assignments may be created using this Role Definition. This
     will allow application of this Role Definition on the entire database
     account or any underlying Database / Collection. Must have at least one
     element. Scopes higher than Database account are not enforceable as
     assignable Scopes. Note that resources referenced in assignable Scopes
     need not exist.
    :type assignable_scopes: list[str]
    :param permissions: The set of operations allowed through this Role
     Definition.
    :type permissions: list[~azure.mgmt.cosmosdb.models.Permission]
    """

    _attribute_map = {
        'role_name': {'key': 'properties.roleName', 'type': 'str'},
        'type': {'key': 'properties.type', 'type': 'RoleDefinitionType'},
        'assignable_scopes': {'key': 'properties.assignableScopes', 'type': '[str]'},
        'permissions': {'key': 'properties.permissions', 'type': '[Permission]'},
    }

    def __init__(self, **kwargs):
        super(SqlRoleDefinitionCreateUpdateParameters, self).__init__(**kwargs)
        self.role_name = kwargs.get('role_name', None)
        self.type = kwargs.get('type', None)
        self.assignable_scopes = kwargs.get('assignable_scopes', None)
        self.permissions = kwargs.get('permissions', None)