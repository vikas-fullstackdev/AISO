# from fastapi import HTTPException
from .database import cursor, conn

def register_user(email: str, password: str):
    # check existing
    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
    if cursor.fetchone():
        raise HTTPException(status_code=400, detail="User already exists")

    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        return {"status": "success", "message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def login_user(email: str, password: str):
    cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    stored_password = row[0]
    if password != stored_password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    return {"status": "success", "message": "Login successful"}
