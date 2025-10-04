from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry

DB_URL = "sqlite:///./sqlite/todos.db"

engine = create_engine(DB_URL,connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

mapper_registry = registry()
BASE = mapper_registry.generate_base()




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
