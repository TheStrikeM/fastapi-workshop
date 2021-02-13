from pydantic import BaseSettings


class Settings(BaseSettings):
    server_ip: str = "127.0.0.1"
    server_port: int = 8000
    server_reload: bool = True
    database_url: str = "postgresql://postgres:123456@localhost/test"


settings = Settings()
