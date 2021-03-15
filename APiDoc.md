### Api Doc ###

'''This is just a simple api to expose the models of the data_sources app provided.'''
```This api was created with FE devs in mind mostly, it provides error handling
   as well as the abilty to filter on any field, allowing them to create forms
   without having to do most of the heavy lifting```

```
### Gateways
```Keywords:
      label
      posse
      location
      oauth2_client_id
      serial_number
      type_name
   ```

### Gateway Tags
``` In the spec it was said that unit types should be maintained,
    thus I added checking to ensure that an invalid type never
    gets added to the database. 
    
    Keywords(Same for all methods):
    gateway
    data_flow
    hardware_name
    unit_name
    unit_type
    status
```

### Gateway Status

```Keywords:
    gateway
    hostname
    data_flow
    os_name
    os_version
    firmware_version
    maio_edge_version
    created_at```



