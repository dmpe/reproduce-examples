import os,sys
from prometheus_client import start_http_server, Summary, Gauge

import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(1234)
    # Generate some requests.

    g = Gauge('tenant_object_size', 'Size of Tenant in bytes', ['tenant_id'])
    g.labels(tenant_id='1234567890').set(4.2)
    g.labels(tenant_id='237348959').set(5.2)
    g.labels(tenant_id='947').set(6)

    g = Gauge('tenant_object_max', 'Maxiumum provisioned in bytes', ['tenant_id'])
    g.labels(tenant_id='1234567890').set(10)
    g.labels(tenant_id='237348959').set(6)
    g.labels(tenant_id='947').set(5)

    g = Gauge('tenant_object_association', 'Naming association', ['tenant_id', 'tenant_name'])
    g.labels(tenant_id='1234567890', tenant_name='red').set(1)
    g.labels(tenant_id='237348959', tenant_name='blue').set(1)
    g.labels(tenant_id='947', tenant_name='orange').set(1)

    while True:
        process_request(random.random())
