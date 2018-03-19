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

from .metric_alert_criteria import MetricAlertCriteria


class MetricAlertSingleResourceMultipleMetricCriteria(MetricAlertCriteria):
    """Specifies the metric alert criteria for a single resource that has multiple
    metric criteria.

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param all_of: The list of metric criteria for this 'all of' operation.
    :type all_of: list[~azure.mgmt.monitor.models.MetricCriteria]
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'all_of': {'key': 'allOf', 'type': '[MetricCriteria]'},
    }

    def __init__(self, *, all_of=None, **kwargs) -> None:
        super(MetricAlertSingleResourceMultipleMetricCriteria, self).__init__(, **kwargs)
        self.all_of = all_of
        self.odatatype = 'Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria'