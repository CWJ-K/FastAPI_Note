<!-- omit in toc -->
# Table of Contents
- [Dynamic Parameters](#dynamic-parameters)
- [Limiting Allowed Values](#limiting-allowed-values)
- [Advanced validation](#advanced-validation)

## Dynamic Parameters

```python

    @app.get('/users/{test}/{id}/')
    async def get_user(test: str, id: int):
        return {'type': test,'id': id}

```

## Limiting Allowed Values
* Use `Enum` to set limited allowed arguments in app

## Advanced validation
* set some options on each parameters
* Use the function of FastAPI: `Path`