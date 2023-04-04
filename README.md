# Smartphone_shop


## Endpoints

| Method | Endpoint |
|--------|----------|
| POST | add_phone/ |
| POST | get_model/ |
| POST | search_name/ |
| POST | upd_phone/ |
| POST | sign_in/ |
| POST | sign_up/ |
| GET | add_product/<int:pk> |


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

