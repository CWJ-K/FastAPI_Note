<!-- omit in toc -->
# Table of Contents
- [Dynamic Parameters](#dynamic-parameters)
- [Limiting Allowed Values](#limiting-allowed-values)
- [Advanced validation](#advanced-validation)
  - [Ellipsis (...)](#ellipsis-)
  - [Tables of keyword arguments](#tables-of-keyword-arguments)
- [Query Parameters](#query-parameters)

## Dynamic Parameters

```python

    @app.get('/users/{test}/{id}/')
    async def get_user(test: str, id: int):
        return {'type': test,'id': id}

```

## Limiting Allowed Values
* Use `Enum` to set limited allowed arguments in the app

## Advanced validation
* set some options on each parameter
* Use the function of FastAPI: `Path`
* the result of Path is used as a **default value** for arguments

```python
    @app.get('/users/{id}')
    async def get_user(id: int = Path(..., ge=1)):
        return {'id': id} 

    @app.get('/users/{id}')
    async def get_user(id: str = Path(..., min_length=9, max_length=9)):
        return {'id': id} 

```
### Ellipsis (...)
* do need a default value


### Tables of keyword arguments
|Type|keyword|Meaning|
|:---:|:---:|:---:|
|int|gt|greater than|
|int|ge|greater than or equal to|
|int|lt|less than|
|int|le|less than or equal to|
|string|min_length||
|string|max_length||
|string|regex=r''  (like f-strings)|regular expression|


## Query Parameters
* add dynamic parameters to a URL
  * read endpoints to apply pagination, a filter, a sorting order or selecting fields
* exact same syntax as path parameters, but they do not appear in the path pattern
  * FastAPI automatically consider them to be query parameters

```python
    @app.get('/users')
    async def get_user(page: int = 1, size: int = 10):
        return {'page': page, 'size': size} 
```