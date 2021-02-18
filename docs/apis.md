### SMARTIA TECH API DOCUMENTATION

- Introduction
- Authentication
- Response format
- Pagination
- Error Message
- Rate Limit
- Versioning


#### Introduction
Smartia Tech API is structured around REST. It returns JSON responses and uses standard HTTP response codes and verbs.


#### Authentication
Every endpoint expects API keys to be passed in the Authorization header. All API requests without authentication will fail

```buildoutcfg
-H "Authorization: Bearer your_api_key"
```

`Note: For this challenge, the API key is: slbnkmdysqpxyzwacwpztjfikptx`


#### Response Format
The format of all the responses is as follows

```buildoutcfg
{
    "count": 56,
    "next": "https://smartia-tech.com/api/v1/gateway/?page=3",
    "previous": "https://smartia-tech.com/api/v1/gateway/?page=1",
    "results": []
}
```

Definition
- count: This represents the total number of values available for the api.
- next: This is used for pagination to get the next page response data
- previous: This is also used for pagination to get the previous response data.
- results: This is where the actual data you requested for would live in. It would always be an array of object.


By default, we return the ID of every nested objects rather than the data. For example, let's say we have a response as follows:
```buildoutcfg
{
    "count": 56,
    "next": "https://smartia-tech.com/api/v1/gateway/?page=3",
    "previous": "https://smartia-tech.com/api/v1/gateway/?page=1",
    "results": [
        {
            "id": "sdh67430-4387sjh4736-4398",
            "name": "Gate way name"
        }
    ]
}
```

If this api has nested objects like tags, status, by default we will only return the ID, i.e

```buildoutcfg
    "results": [
        {
            "id": "sdh67430-4387sjh4736-4398",
            "name": "Gate way name",
            "tags": ["sdhjs-jhsd673-43n-", "sd-34j823-whew0"...],
            "status": ["apwep-32kjsd8-349", "043jsd82-32s-483", ...]
        }
    ]
    
```

If you want the actual nested data itself other than the IDs, i.e more verbose, you can always append a query parameter of "response = verbose"
e.g
```buildoutcfg
GET: https://smartia-tech.com/api/v1/gateway/?response=verbose

RESPONSE:
"results": [
        {
            "id": "sdh67430-4387sjh4736-4398",
            "name": "Gate way name",
            "tags": [
                {
                    "label": "Tage Label",
                    "unit_name": "John doe",
                    ...
                }
            ],
            "status": [
                {
                    "hostname": "Smartia-tech.com",
                    "unit_name": "John doe",
                    ...
                }
            ],
        }
    ]
```
