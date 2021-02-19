### SMARTIA TECH API DOCUMENTATION

- Introduction
- Authentication
- Response format
- Pagination
- Error Message
- Rate Limit
- Versioning
- Searching & Filtering


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


#### Pagination
To return a paginated response, you have two different query parameters (page, limit)

- page: This denotes the page you want to fetch.
    It's REQUIRED for pagination and it must be an INTEGER, e.g 5
- limit: This denotes the number of data you want to fetch per requests. It defaults to 20 as it's not required and
it must also be an integer. The value ranges from 1 - 50

Example:
```buildoutcfg
GET: https://smartia-tech.com/api/v1/gateway/?page=2&limit=30
```


#### Error Messages
We use standard HTTP response codes to indicate the success or failure of an API request.
Status codes within 200 - 300 specifies a successful request

Codes within 500 means something went wrong on our side while status codes within 400 - 499 means the error occured 
mostly from the information you provided

Below are the http status code we currently use
```buildoutcfg
200 - OK
201 - Created successfully
204 - Deleted successfully

400 - Bad Request (check the payload data you sent)
401 - UnAuthorized (API key is not valid or not present)
403 - Forbidden (The API key doesn't have permission to carry out the information)
429 - Too Many Requests (Rate limit error) - see RATE LIMIT
500 - Server Error (We screwed up something)
```

#### Rate Limit
All APIs are throttled and you can only make 30 requests per minutes. Any other requests
after the first 30 requests within a minute will return a 429 status code

#### Versioning
We also support versioning, and the current version is `v1`


#### Searching & Filtering
To search for any information in an endpoint, pass the value in a query parameter as shown below
```buildoutcfg
endpoint/?search='Posse Label'
```

Below are the fields your search value will look into
- posse endpoint - Since it contains only label and id property, you can only search a label
- gateway endpoint - searches from [gateway label, posse label, location, serial_number]. i.e you can search from any of the fields in the array
- gateway-status - searches from [status label, gateway label, hostname, os_name]
- gateway-tag - searches from [tag label, gateway label, hardware_name]


Also, you can filter `unit_type` and/or `status` from gateway-tags
```buildoutcfg
/gateway-tags/?unit_type=bool&status=active
```
