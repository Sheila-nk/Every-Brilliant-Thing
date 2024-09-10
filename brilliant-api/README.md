# API

## Add a brilliant thing
### Request URL

`POST http://127.0.0.1:8000/brilliant_thing/`

### Request body
```json
{
  "entry": "Hot cocoa on a rainy day"
}
```
### Response
```json
{
  "message": "Brilliant Thing #7 added successfully!"
}
```

## Get a brilliant thing
### Request URL

`GET http://127.0.0.1:8000/brilliant_thing/`

### Request body
```json
{
  "entry": "Hot cocoa on a rainy day"
}
```
### Response
```json
{
  "entry": "A hug after a long day",
  "id": 3,
  "date_posted": "2024-09-09T22:14:06.697322"
}
```