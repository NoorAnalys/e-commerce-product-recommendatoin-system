from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Read variables from a .env file if it exists, and ignore unknown keys
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Basic project info
    PROJECT_NAME: str = "ecommerce-backend"
    API_V1_STR: str = "/api/v1"

    # MySQL connection string for SQLAlchemy using PyMySQL driver:
    # mysql+pymysql://USER:PASSWORD@HOST:PORT/DB_NAME
    DATABASE_URL: str = "mysql+pymysql://root:rootpassword@127.0.0.1:3306/ecommerce_db"

    # JWT settings
    SECRET_KEY: str = "CHANGE_ME_SUPER_SECRET"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Frontend origins allowed to call this API in browser
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]


settings = Settings()
