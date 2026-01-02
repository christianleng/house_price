from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database.core import get_db
from app.auth.security import verify_token, UserRole
from app.auth.schemas import TokenData
from app.entities.user import User

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


def get_current_token_data(
    token: Annotated[str, Depends(oauth2_bearer)],
) -> TokenData:
    try:
        payload = verify_token(token)
        return TokenData(
            user_id=payload["user_id"],
            email=payload.get("email"),
            role=UserRole(payload["role"]),
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user(
    token_data: Annotated[TokenData, Depends(get_current_token_data)],
    db: Annotated[Session, Depends(get_db)],
) -> User:
    if not token_data.is_user():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access restricted to users only",
        )

    user = db.query(User).filter(User.id == token_data.get_uuid()).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
        )

    return user


CurrentUser = Annotated[User, Depends(get_current_token_data)]
CurrentTokenData = Annotated[TokenData, Depends(get_current_user)]
