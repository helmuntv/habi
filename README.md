# habi

## Technologies

> ### Python

# Getting started

## Installation

Please check the official Python installation guide for server requirements before you start. [Official Documentation](https://docs.python.org/3.9/installing/index.html)

> Please Refer to [Github and ssh keys help page](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) before start.

Clone the repository with SSH

    git@github.com:helmuntv/habi.git

Or clone the repository with HTTPS

    https://github.com/helmuntv/habi.git


Switch to the repo folder

    cd habi

Create the venv folder

    python3 -m venv env

Install all the dependencies using pip

    pip install -r requirements.txt

Activate the environment with the dependencies

    source env/bin/activate

Start the local development server

    python3 main.py

You can now access the server at http://localhost:8000


## Successful Request

```
status 200 OK
[
    {
        "id": 10,
        "address": "calle 95 # 78 - 49",
        "city": "bogota",
        "name": "pre_venta",
        "price": 120000000,
        "description": "hermoso acabado, listo para estrenar"
    },
    {
        "id": 67,
        "address": "calle 95 # 78 - 123",
        "city": "bogota",
        "name": "pre_venta",
        "price": 120000000,
        "description": "hermoso acabado, listo para estrenar"
    }
]
```

# Testing API

The api can now be accessed at

    http://localhost:8000/properties?year=2020&city=bogota&status=pre_venta

Request Query Params

| **Required** | **Key**      | **Value**        |
| ------------ | ------------ | ---------------- |
| No           | year         |  int             |
| No           | city         |  str             |
| No           | status       |  str             |


## How the project will be approached:

1. Check requirements
2. Check database structure and tables
3. Create query to return the results to the user
4. Create API in python with local server and database connection
5. Create endpoint with GET method in which the results of the query are displayed
6. Create filters and add them to the query
7. Add environment variables
8. Table creation script for likes service
9. Create project structure and create repository 

---

