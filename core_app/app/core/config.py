from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    project_name: str
    postgres_dsn: str
    jwt_secret_key: str
    jwt_algorithm: str
    access_token_expire_minutes: int
    api_v1_str: str
    file_upload_chunk_size: int
    file_upload_semaphore_count: int
    file_upload_dir: str
    file_url_base: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    
settings = Settings()