# Lists

Types:

```python
from vibedropper.types import List, Pagination, ListRetrieveResponse, ListListResponse
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
- <code title="get /campaigns">client.campaigns.<a href="./src/vibedropper/resources/campaigns.py">list</a>(\*\*<a href="src/vibedropper/types/campaign_list_params.py">params</a>) -> <a href="./src/vibedropper/types/campaign_list_response.py">CampaignListResponse</a></code>

# Forms

Types:

```python
from vibedropper.types import (
    Form,
    FormRetrieveResponse,
    FormUpdateResponse,
    FormListResponse,
    FormDeleteResponse,
    FormListSubmissionsResponse,
)
```

Methods:

- <code title="get /forms/{formId}">client.forms.<a href="./src/vibedropper/resources/forms.py">retrieve</a>(form_id) -> <a href="./src/vibedropper/types/form_retrieve_response.py">FormRetrieveResponse</a></code>
- <code title="put /forms/{formId}">client.forms.<a href="./src/vibedropper/resources/forms.py">update</a>(form_id, \*\*<a href="src/vibedropper/types/form_update_params.py">params</a>) -> <a href="./src/vibedropper/types/form_update_response.py">FormUpdateResponse</a></code>
- <code title="get /forms">client.forms.<a href="./src/vibedropper/resources/forms.py">list</a>(\*\*<a href="src/vibedropper/types/form_list_params.py">params</a>) -> <a href="./src/vibedropper/types/form_list_response.py">FormListResponse</a></code>
- <code title="delete /forms/{formId}">client.forms.<a href="./src/vibedropper/resources/forms.py">delete</a>(form_id) -> <a href="./src/vibedropper/types/form_delete_response.py">FormDeleteResponse</a></code>
- <code title="get /forms/{formId}/submissions">client.forms.<a href="./src/vibedropper/resources/forms.py">list_submissions</a>(form_id, \*\*<a href="src/vibedropper/types/form_list_submissions_params.py">params</a>) -> <a href="./src/vibedropper/types/form_list_submissions_response.py">FormListSubmissionsResponse</a></code>

# KnowledgeBases

Types:

```python
from vibedropper.types import (
    KnowledgeBase,
    KnowledgeBaseRetrieveResponse,
    KnowledgeBaseUpdateResponse,
    KnowledgeBaseListResponse,
)
```

Methods:

- <code title="get /knowledge-bases/{kbId}">client.knowledge_bases.<a href="./src/vibedropper/resources/knowledge_bases/knowledge_bases.py">retrieve</a>(kb_id) -> <a href="./src/vibedropper/types/knowledge_base_retrieve_response.py">KnowledgeBaseRetrieveResponse</a></code>
- <code title="patch /knowledge-bases/{kbId}">client.knowledge_bases.<a href="./src/vibedropper/resources/knowledge_bases/knowledge_bases.py">update</a>(kb_id, \*\*<a href="src/vibedropper/types/knowledge_base_update_params.py">params</a>) -> <a href="./src/vibedropper/types/knowledge_base_update_response.py">KnowledgeBaseUpdateResponse</a></code>
- <code title="get /knowledge-bases">client.knowledge_bases.<a href="./src/vibedropper/resources/knowledge_bases/knowledge_bases.py">list</a>() -> <a href="./src/vibedropper/types/knowledge_base_list_response.py">KnowledgeBaseListResponse</a></code>
- <code title="delete /knowledge-bases/{kbId}">client.knowledge_bases.<a href="./src/vibedropper/resources/knowledge_bases/knowledge_bases.py">delete</a>(kb_id) -> None</code>

## Articles

Types:

```python
from vibedropper.types.knowledge_bases import (
    KnowledgeBaseArticle,
    ArticleCreateResponse,
    ArticleListResponse,
)
```

Methods:

- <code title="post /knowledge-bases/{kbId}/articles">client.knowledge_bases.articles.<a href="./src/vibedropper/resources/knowledge_bases/articles.py">create</a>(kb_id, \*\*<a href="src/vibedropper/types/knowledge_bases/article_create_params.py">params</a>) -> <a href="./src/vibedropper/types/knowledge_bases/article_create_response.py">ArticleCreateResponse</a></code>
- <code title="get /knowledge-bases/{kbId}/articles">client.knowledge_bases.articles.<a href="./src/vibedropper/resources/knowledge_bases/articles.py">list</a>(kb_id, \*\*<a href="src/vibedropper/types/knowledge_bases/article_list_params.py">params</a>) -> <a href="./src/vibedropper/types/knowledge_bases/article_list_response.py">ArticleListResponse</a></code>

# Pages

Types:

```python
from vibedropper.types import (
    Page,
    PageRetrieveResponse,
    PageUpdateResponse,
    PageListResponse,
    PageDeleteResponse,
)
```

Methods:

- <code title="get /pages/{pageId}">client.pages.<a href="./src/vibedropper/resources/pages.py">retrieve</a>(page_id) -> <a href="./src/vibedropper/types/page_retrieve_response.py">PageRetrieveResponse</a></code>
- <code title="put /pages/{pageId}">client.pages.<a href="./src/vibedropper/resources/pages.py">update</a>(page_id, \*\*<a href="src/vibedropper/types/page_update_params.py">params</a>) -> <a href="./src/vibedropper/types/page_update_response.py">PageUpdateResponse</a></code>
- <code title="get /pages">client.pages.<a href="./src/vibedropper/resources/pages.py">list</a>(\*\*<a href="src/vibedropper/types/page_list_params.py">params</a>) -> <a href="./src/vibedropper/types/page_list_response.py">PageListResponse</a></code>
- <code title="delete /pages/{pageId}">client.pages.<a href="./src/vibedropper/resources/pages.py">delete</a>(page_id) -> <a href="./src/vibedropper/types/page_delete_response.py">PageDeleteResponse</a></code>
