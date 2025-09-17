from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_DRIVER: str = "ODBC Driver 17 for SQL Server"
    DB_SERVER: str = "MITHUNSINGH"
    DB_DATABASE: str = "TestDB"
    DB_PORT: int = 1433   # 👈 added default SQL Server port
    DB_AUTH: str = "windows"  # fixed for your case

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
