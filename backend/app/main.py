# from fastapi import FastAPI
# from .auth import register_user, login_user
# from .ondc import get_products, search_products


# app = FastAPI()

# @app.post("/register")
# def register(email: str, password: str):
#     return register_user(email, password)

# @app.post("/login")
# def login(email: str, password: str):
#     return login_user(email, password)


# # List products by category
# @app.get("/products/{category}")
# def list_products(category: str):
#     try:
#         return get_products(category)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Search products
# @app.get("/search")
# def search(query: str):
#     try:
#         return search_products(query)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .auth import register_user, login_user
from .ondc import get_products, search_products  # if present in your project

app = FastAPI(title="AISO Backend", version="1.0")

# Allow CORS for local dev (Flutter web)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
async def register(payload: dict):
    """
    Accepts JSON: { "email": "...", "password": "..." }
    """
    email = payload.get("email")
    password = payload.get("password")
    if not email or not password:
        raise HTTPException(status_code=400, detail="email and password required")
    try:
        return register_user(email, password)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/login")
async def login(payload: dict):
    """
    Accepts JSON: { "email": "...", "password": "..." }
    """
    email = payload.get("email")
    password = payload.get("password")
    if not email or not password:
        raise HTTPException(status_code=400, detail="email and password required")
    try:
        return login_user(email, password)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional ONDC endpoints (if you have ondc.py)
@app.get("/products/{category}")
def list_products(category: str):
    try:
        return get_products(category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/search")
def search(query: str):
    try:
        return search_products(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
