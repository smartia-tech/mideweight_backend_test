### API DOCUMENTATION


### SWAGGER DOCUMENTATION

Swagger documention is Available at http://localhost:8000/api/docs/ 


#### Pagination
To return a paginated response, use these query params(page, limit)

- page: This denotes the page you want to fetch.
    It's REQUIRED for pagination and it must be an INTEGER, e.g 5

Example:
```buildoutcfg
GET: http://localhost:8000/api/v1/gateway/?page=2
```


