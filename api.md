# Lists

Types:

```python
from vibedropper.types import List, ListRetrieveResponse, ListListResponse
```

Methods:

- <code title="get /lists/{listId}">client.lists.<a href="./src/vibedropper/resources/lists/lists.py">retrieve</a>(list_id) -> <a href="./src/vibedropper/types/list_retrieve_response.py">ListRetrieveResponse</a></code>
- <code title="get /lists">client.lists.<a href="./src/vibedropper/resources/lists/lists.py">list</a>(\*\*<a href="src/vibedropper/types/list_list_params.py">params</a>) -> <a href="./src/vibedropper/types/list_list_response.py">ListListResponse</a></code>

## Subscribers

Types:

```python
from vibedropper.types.lists import (
    Subscriber,
    SubscriberListResponse,
    SubscriberAddResponse,
    SubscriberRemoveResponse,
)
```

Methods:

- <code title="get /lists/{listId}/subscribers">client.lists.subscribers.<a href="./src/vibedropper/resources/lists/subscribers.py">list</a>(list_id) -> <a href="./src/vibedropper/types/lists/subscriber_list_response.py">SubscriberListResponse</a></code>
- <code title="post /lists/{listId}/subscribers">client.lists.subscribers.<a href="./src/vibedropper/resources/lists/subscribers.py">add</a>(list_id, \*\*<a href="src/vibedropper/types/lists/subscriber_add_params.py">params</a>) -> <a href="./src/vibedropper/types/lists/subscriber_add_response.py">SubscriberAddResponse</a></code>
- <code title="delete /lists/{listId}/subscribers/{subscriberId}">client.lists.subscribers.<a href="./src/vibedropper/resources/lists/subscribers.py">remove</a>(subscriber_id, \*, list_id) -> <a href="./src/vibedropper/types/lists/subscriber_remove_response.py">SubscriberRemoveResponse</a></code>

# Customers

Types:

```python
from vibedropper.types import (
    Customer,
    CustomerRetrieveResponse,
    CustomerUpdateResponse,
    CustomerListResponse,
)
```

Methods:

- <code title="get /customers/{customerId}">client.customers.<a href="./src/vibedropper/resources/customers.py">retrieve</a>(customer_id) -> <a href="./src/vibedropper/types/customer_retrieve_response.py">CustomerRetrieveResponse</a></code>
- <code title="patch /customers/{customerId}">client.customers.<a href="./src/vibedropper/resources/customers.py">update</a>(customer_id, \*\*<a href="src/vibedropper/types/customer_update_params.py">params</a>) -> <a href="./src/vibedropper/types/customer_update_response.py">CustomerUpdateResponse</a></code>
- <code title="get /customers">client.customers.<a href="./src/vibedropper/resources/customers.py">list</a>(\*\*<a href="src/vibedropper/types/customer_list_params.py">params</a>) -> <a href="./src/vibedropper/types/customer_list_response.py">CustomerListResponse</a></code>

# Campaigns

Types:

```python
from vibedropper.types import Campaign, CampaignRetrieveResponse, CampaignListResponse
```

Methods:

- <code title="get /campaigns/{campaignId}">client.campaigns.<a href="./src/vibedropper/resources/campaigns.py">retrieve</a>(campaign_id) -> <a href="./src/vibedropper/types/campaign_retrieve_response.py">CampaignRetrieveResponse</a></code>
- <code title="get /campaigns">client.campaigns.<a href="./src/vibedropper/resources/campaigns.py">list</a>() -> <a href="./src/vibedropper/types/campaign_list_response.py">CampaignListResponse</a></code>
