from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# pathparameter
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}



# optional parameter

@app.get("/products/{product_id}")
def read_product(product_id: int,q: str | None = None):
    return {"product_id": product_id,"q":q}

#query parameter (used for filter and pagination)
@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}