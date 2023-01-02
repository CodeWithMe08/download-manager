from pydantic import BaseSettings

class Settings(BaseSettings):
    SOURCE: str
    SFX_DEST: str
    MUSIC_DEST: str
    VIDEO_DEST: str
    DOCUMENTS_DEST: str
    IMAGE_DEST: str
    class Config:
        env_file = ".env"
        
settings = Settings()
