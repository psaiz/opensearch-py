# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

from ..plugins.alerting import AlertingClient as AlertingClient
from .utils import NamespacedClient as NamespacedClient
from typing import Any

class PluginsClient(NamespacedClient):
    alerting: Any
    def __init__(self, client) -> None: ...
