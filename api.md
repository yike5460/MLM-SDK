# Instances

Types:

```python
from mlm.types import (
    InstanceDetails,
    InstanceSummary,
    InstanceCreateResponse,
    InstanceUpdateResponse,
    InstanceListResponse,
)
```

Methods:

- <code title="post /instances">client.instances.<a href="./src/mlm/resources/instances.py">create</a>(\*\*<a href="src/mlm/types/instance_create_params.py">params</a>) -> <a href="./src/mlm/types/instance_create_response.py">InstanceCreateResponse</a></code>
- <code title="get /instances/{instanceName}">client.instances.<a href="./src/mlm/resources/instances.py">retrieve</a>(instance_name) -> <a href="./src/mlm/types/instance_details.py">InstanceDetails</a></code>
- <code title="put /instances/{instanceName}">client.instances.<a href="./src/mlm/resources/instances.py">update</a>(instance_name, \*\*<a href="src/mlm/types/instance_update_params.py">params</a>) -> <a href="./src/mlm/types/instance_update_response.py">InstanceUpdateResponse</a></code>
- <code title="get /instances">client.instances.<a href="./src/mlm/resources/instances.py">list</a>() -> <a href="./src/mlm/types/instance_list_response.py">InstanceListResponse</a></code>
- <code title="delete /instances/{instanceName}">client.instances.<a href="./src/mlm/resources/instances.py">delete</a>(instance_name) -> None</code>

# Models

Types:

```python
from mlm.types import (
    ModelDetails,
    ModelSummary,
    ModelCreateResponse,
    ModelUpdateResponse,
    ModelListResponse,
    ModelDeleteResponse,
)
```

Methods:

- <code title="post /models">client.models.<a href="./src/mlm/resources/models.py">create</a>(\*\*<a href="src/mlm/types/model_create_params.py">params</a>) -> <a href="./src/mlm/types/model_create_response.py">ModelCreateResponse</a></code>
- <code title="get /models/{modelName}">client.models.<a href="./src/mlm/resources/models.py">retrieve</a>(model_name) -> <a href="./src/mlm/types/model_details.py">ModelDetails</a></code>
- <code title="put /models/{modelName}">client.models.<a href="./src/mlm/resources/models.py">update</a>(model_name, \*\*<a href="src/mlm/types/model_update_params.py">params</a>) -> <a href="./src/mlm/types/model_update_response.py">ModelUpdateResponse</a></code>
- <code title="get /models">client.models.<a href="./src/mlm/resources/models.py">list</a>() -> <a href="./src/mlm/types/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /models/{modelName}">client.models.<a href="./src/mlm/resources/models.py">delete</a>(model_name) -> <a href="./src/mlm/types/model_delete_response.py">object</a></code>

# Metrics

Types:

```python
from mlm.types import MetricDatapoint, MetricListResponse
```

Methods:

- <code title="get /metrics">client.metrics.<a href="./src/mlm/resources/metrics.py">list</a>(\*\*<a href="src/mlm/types/metric_list_params.py">params</a>) -> <a href="./src/mlm/types/metric_list_response.py">MetricListResponse</a></code>
