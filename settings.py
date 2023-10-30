from environs import Env
from dataclasses import dataclass

import os


@dataclass
class Settings:
    TOKEN: str          # Token telegram bot
    ADMIN_ID: list      # Administrators list
    GOODS: str          # Name of file database with goods
    PATH_DB_GOODS: str  # Path to the database with goods
    PAGE_SIZE: int      # Standard size of goods page


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        TOKEN=env.str("TOKEN"),
        ADMIN_ID=[int(i) for i in env.list("ADMIN_ID")],
        GOODS=env.str("TABLE_GOODS"),
        PATH_DB_GOODS=os.path.join(os.getcwd(), "database/goods.db"),
        PAGE_SIZE=3
    )


# Class object with ALL settings
settings = get_settings(".env")
