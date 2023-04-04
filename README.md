# Smartphone_shop


## Database

#### Schema SmartPhone

| Field | Type | Description |
|-------|------|-------------|
| id | integer | Primary key |
| price | float | Phone price |
| img_url | string | Phone image url |
| color | string | Phone color |
| name | string | Phone name |
| memory | float | Phone memory |
| model | string | Phone model |
| add_date | date (autamtic) | create date |
| up_date | date (autamtic) | update date |


#### Schema Cart

| Field | Type | Description |
| ------|------|-------------|
| phone_id | integer | Phone id in SmartPhone |
| phone_name | string | Phone name in SmartPhone |
| user | integer | One to Many `User` |




## Endpoints

| Method | Endpoint | Function |
|--------|----------|----------|
| POST | add_phone/ | add_phone |
| POST | get_model/ | model_phones |
| POST | search_name/ | search_name |
| POST | upd_phone/ | upd_phone |
| POST | sign_in/ | sign_in |
| POST | sign_up/ | sign_up |
| GET | add_product/<int:pk> | add_product |

### Functions

#### `add_phone`
> Input data
>> - {
        'price':price,
        'img_url':img_url,
        'color':color,
        'ram':ram,
        'memory':memory,
        'name':name,
       'model':model
        }

> Output data 
>> - {'result':'ok'}


#### `model_phones`
>Input data
>> - {'model': model_name}

>Output data
>> - Get all smartphones include model 


#### `search_name`
>Input data
>> - {'name': search_name}

>Output data
>> - Get all smartphones same search_name



