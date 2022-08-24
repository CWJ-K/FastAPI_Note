<!-- omit in toc -->
# Table of Contents
- [Dynamic Parameters](#dynamic-parameters)
- [Limiting Allowed Values](#limiting-allowed-values)

## Dynamic Parameters

```python

    @app.get('/users/{test}/{id}/')
    async def get_user(test: str, id: int):
        return {'type': test,'id': id}

```

## Limiting Allowed Values