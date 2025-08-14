

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This line will load environment variables from your .env file
# when you are running the application locally.
load_dotenv()

# This command reads the "DATABASE_URL" from the environment.
# On Railway, it will get the live database URL.
# On your local machine, it will get the URL you just put in your .env file.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# This is a check to make sure the DATABASE_URL was found.
if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()