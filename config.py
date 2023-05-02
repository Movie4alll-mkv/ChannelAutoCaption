import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5442493323:AAHPw8TNe0hh2zCAQKm_2O2o6KdmQ3Okgf8")
    API_ID = int(os.environ.get("API_ID", 6534707))
    API_HASH = os.environ.get("API_HASH", "4bcc61d959a9f403b2f20149cbbe627a")
    DB_URL = os.environ.get("DATABASE_URL", "postgres://dgdxlptb:uP0wjJhot4kqWrwXg8ENLEFAuEd2yk4d@mouse.db.elephantsql.com/dgdxlptb")
