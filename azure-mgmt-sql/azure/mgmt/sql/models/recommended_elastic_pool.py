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

from .resource import Resource


class RecommendedElasticPool(Resource):
    """Represents an Azure SQL Recommended Elastic Pool.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Resource name
    :vartype name: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :ivar database_edition: The edition of the Azure SQL Recommended Elastic
     Pool. The ElasticPoolEditions enumeration contains all the valid
     editions. Possible values include: 'Basic', 'Standard', 'Premium'
    :vartype database_edition: str or :class:`ElasticPoolEditions
     <azure.mgmt.sql.models.ElasticPoolEditions>`
    :param dtu: The DTU for the SQL Azure Recommended Elastic Pool.
    :type dtu: float
    :param database_dtu_min: The minimum DTU for the database.
    :type database_dtu_min: float
    :param database_dtu_max: The maximum DTU for the database.
    :type database_dtu_max: float
    :param storage_mb: Gets storage size in megabytes.
    :type storage_mb: float
    :ivar observation_period_start: The observation period start (ISO8601
     format).
    :vartype observation_period_start: datetime
    :ivar observation_period_end: The observation period start (ISO8601
     format).
    :vartype observation_period_end: datetime
    :ivar max_observed_dtu: Gets maximum observed DTU.
    :vartype max_observed_dtu: float
    :ivar max_observed_storage_mb: Gets maximum observed storage in megabytes.
    :vartype max_observed_storage_mb: float
    :ivar databases: The list of Azure SQL Databases in this pool. Expanded
     property
    :vartype databases: list of :class:`Database
     <azure.mgmt.sql.models.Database>`
    :ivar metrics: The list of Azure SQL Databases housed in the server.
     Expanded property
    :vartype metrics: list of :class:`RecommendedElasticPoolMetric
     <azure.mgmt.sql.models.RecommendedElasticPoolMetric>`
    """ 

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'database_edition': {'readonly': True},
        'observation_period_start': {'readonly': True},
        'observation_period_end': {'readonly': True},
        'max_observed_dtu': {'readonly': True},
        'max_observed_storage_mb': {'readonly': True},
        'databases': {'readonly': True},
        'metrics': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'database_edition': {'key': 'properties.databaseEdition', 'type': 'str'},
        'dtu': {'key': 'properties.dtu', 'type': 'float'},
        'database_dtu_min': {'key': 'properties.databaseDtuMin', 'type': 'float'},
        'database_dtu_max': {'key': 'properties.databaseDtuMax', 'type': 'float'},
        'storage_mb': {'key': 'properties.storageMB', 'type': 'float'},
        'observation_period_start': {'key': 'properties.observationPeriodStart', 'type': 'iso-8601'},
        'observation_period_end': {'key': 'properties.observationPeriodEnd', 'type': 'iso-8601'},
        'max_observed_dtu': {'key': 'properties.maxObservedDtu', 'type': 'float'},
        'max_observed_storage_mb': {'key': 'properties.maxObservedStorageMB', 'type': 'float'},
        'databases': {'key': 'properties.databases', 'type': '[Database]'},
        'metrics': {'key': 'properties.metrics', 'type': '[RecommendedElasticPoolMetric]'},
    }

    def __init__(self, location, tags=None, dtu=None, database_dtu_min=None, database_dtu_max=None, storage_mb=None):
        super(RecommendedElasticPool, self).__init__(location=location, tags=tags)
        self.database_edition = None
        self.dtu = dtu
        self.database_dtu_min = database_dtu_min
        self.database_dtu_max = database_dtu_max
        self.storage_mb = storage_mb
        self.observation_period_start = None
        self.observation_period_end = None
        self.max_observed_dtu = None
        self.max_observed_storage_mb = None
        self.databases = None
        self.metrics = None