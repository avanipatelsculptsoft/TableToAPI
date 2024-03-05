# TableToAPI
A python project which will create API CRUD routes based on database tables 

# How to generate Model and create routes using FastAPI

1. Command to generate models in directory using sqlacodegen
    sqlacodegen --outfile models.py postgresql+pg8000://postgres:password@localhost:5433/codegendb
        It’ll always override the outfile which you have mentioned in the above command.
2. Create a router file based on that model insider routers folder in your app directory.
    So it’ll be like routers/customers.py
    routers/Contacts.py
3. We need to create routers file manually
4. In main python file we will create FastAPI and include all tables crud routers one by one
    app.include_router(customer.router)
    app.include_router(contact.router)


# How to run the existing code:

1. Create venv
2. Install all packages listed in requirements.txt file by following command
    pip freeze > requirements.txt
3. To run the app 
4. uvicorn main:app --reload


# OpenAPI.yml

Update openapi.yml based on your newly added models and check in swagger editor
