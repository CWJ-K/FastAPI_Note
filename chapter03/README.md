<!-- omit in toc -->
# Introduction

<br />

<!-- omit in toc -->
# Table of Contents
- [Fundamental Concepts](#fundamental-concepts)
  - [endpoint](#endpoint)
  - [FastAPI](#fastapi)
  - [Uvicorn](#uvicorn)
  - [Payload](#payload)
- [Commands](#commands)
  - [Structure of FastAPI](#structure-of-fastapi)
  - [Call a FastAPI](#call-a-fastapi)
    - [Issue: uvicorn ERROR: [Errno 98] Address already in use](#issue-uvicorn-error-errno-98-address-already-in-use)
  - [FastAPI automatic interactive documentation](#fastapi-automatic-interactive-documentation)
  - [Handle Request Parameters](#handle-request-parameters)
    - [Path Parameters](#path-parameters)
      - [Codes](#codes)

<br />

# Fundamental Concepts
## [endpoint](https://www.twblogs.net/a/5c9e40abbd9eee75238873e4)

## FastAPI
* expose an **ASGI-compatible** application
* rely on OpenAPI specification, [`Swagger`](https://swagger.io/), automatic interactive documentation includes:
  * all defined endpoints
  * documentation about expected inputs and outputs
* build upon Python libraries
  1. Starletee: a low-level ASGI framework
  2. pydantic: a data validation library based on type hints => can define parameters declaratively

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
* python_script is calles as a module, so use dotted path
```bash
    # :variable_name_of_your_ASGI_app_instance
    uvicorn <python_script>:app --port <port> --host <host>

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
<br />

## FastAPI automatic interactive documentation 
```bash
    http://host:port/docs

```

<br />

## Handle Request Parameters
* Four Types of Request Parameters
  1. Path Parameters
  2. Query Parameters
  3. Body Payloads
  4. Headers

### [Path Parameters](Path_Parameters.md)
* the main thing end users will interact with


#### Codes
* `404 Not Found`
  * await a parameter after API path
  * wrong name of paramters 
* `422 Unprocessable Entity`
  * type error. The type of arguments is not valid
* `307 Temporary Redirect`
  * the requested resource has been temporarily moved to another URI
  * [All modern browsers will automatically detect the 307 Temporary Redirect response code and process the redirection action to the new URI automatically](https://blog.airbrake.io/blog/http-errors/307-temporary-redirect)