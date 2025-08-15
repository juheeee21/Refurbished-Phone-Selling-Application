from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from .schemas import UserLogin

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# For demo purposes, any username/password is valid.
def mock_login(user: UserLogin):
    if not user.username or not user.password:
        raise HTTPException(status_code=400, detail="Username and password required")
    return {"token": f"mocktoken-{user.username}"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    if not token or not token.startswith("mocktoken-"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token.split("mocktoken-")[1]
