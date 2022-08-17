<!-- omit in toc -->
# Introduction

<br />

<!-- omit in toc -->
# Table of Contents

<br />

# Fundamental Concepts
## [endpoint](https://www.twblogs.net/a/5c9e40abbd9eee75238873e4)

## FastAPI
* expose an **ASGI-compatible** application
* automatic interactive documentation includes:
  * all defined endpoints
  * documentation about expected inputs and outputs


## Uvicorn
* a web server compatible with ASGI protocol

## Payload
* the part of transmitted data that is the actual intended message



<br />

# Commands

## Structure of FastAPI
    ```python
    app = FastAPI()
    
    @app.get("/")
    async def function():
        return 'hi'
    ```
* `FastAPI()`: main application object that wire all of the API routes  
* `GET`: endpoint at the root path
  * One decorator per HTTP method 
  * `/`: the first argument to be added to a `GET` endpoint with the path
* `function`: **Path operation function**, which means the function to be operated when switching to the path
* `@`: decorator, synatic sugar, to wrap a function with common logic without compromising readability

## Call a FastAPI
```bash
    # :variable_name_of_your_ASGI_app_instance
    uvicorn python_script:app --port <port> --host <host>

    # use HTTPie to try the endpoint
    http http://<host>:<port>
```


### Issue: uvicorn ERROR: [Errno 98] Address already in use
1. check the port already in use
```bash
    lsof -i :<port>
```
2. kill the process
```bash
    kill -9 <process_id>

```

## FastAPI automatic interactive documentation 
```bash
    http://host:port/docs

```

<br />