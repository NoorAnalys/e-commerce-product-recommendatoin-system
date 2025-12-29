from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.security import create_access_token
from app.schemas.token import Token
from app.services.user_service import authenticate_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
    ) -> Token:
    # OAuth2PasswordRequestForm uses field name "username"
    # We treat it as "email" for our system
    user = authenticate_user(db, email=form_data.username, password=form_data.password)

    access_token = create_access_token(subject=user.id)
    return Token(access_token=access_token)
