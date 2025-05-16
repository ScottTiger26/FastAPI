# from pydantic_settings import BaseSettings, SettingsConfigDict
#
#
# class Settings(BaseSettings):
#     DATABASE_URL: str
#
#     model_config = SettingsConfigDict(
#         env_file="./.env",
#         extra="ignore"
#     )
#
#
# Config = Settings()

# *******************************************************
# config.py

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# --- 1) load your .env file into os.environ
#     this must happen *before* BaseSettings instantiates
env_path = os.path.join(os.path.dirname(__file__), "./.env")
load_dotenv(env_path)

class Settings(BaseSettings):
    DATABASE_URL: str  # now guaranteed to come from os.environ

    model_config = SettingsConfigDict(
        # you can still keep this here for future overrides,
        # but python-dotenv already loaded your vars
        env_file="./.env",
        extra="ignore",
    )

# instantiate now picks up DATABASE_URL from os.environ
Config = Settings()

if __name__ == "__main__":
    print("Loaded DATABASE_URL:", Config.DATABASE_URL)
