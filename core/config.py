from  pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_ignore_empty=True
    )

    TEST_X_API_KEY: str
    PROD_X_API_KEY: str
    ATLAS_URI:str
    DB_NAME:str


settings = Settings()