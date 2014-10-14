from config import Config

# NOTE load database credentials from local env
# NOTE this uses a homebuilt pip module that I use
Config.load_from_list([
    "POSTGRES_HOST",
    "POSTGRES_PORT",
    "POSTGRES_USER",
    "POSTGRES_PASS",
    "POSTGRES_DB",
    ])

