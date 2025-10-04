from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry

DB_URL = "postgresql://postgres:password@localhost/TodoApp"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

mapper_registry = registry()
BASE = mapper_registry.generate_base()




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
