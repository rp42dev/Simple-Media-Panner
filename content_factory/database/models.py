# Database Models (Stub)

# Example: SQLAlchemy models for persistent storage
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ContentItem(Base):
	__tablename__ = 'content_items'
	id = Column(Integer, primary_key=True)
	topic = Column(String(255))
	category = Column(String(100))
	tone = Column(String(100))
	content = Column(Text)
	visuals = Column(Text)
	seo = Column(Text)         # JSON string
	analytics = Column(Text)  # JSON string
	video = Column(Text)      # JSON string
	carousel = Column(Text)   # JSON string
	formatted_content = Column(Text)   # JSON string or text
	research_points = Column(Text)     # JSON string
	strategy = Column(Text)            # JSON string
	topics = Column(Text)              # JSON string
	visual_prompts = Column(Text)      # JSON string
	writer_output = Column(Text)       # JSON string or text

# SQLAlchemy engine and session setup
DATABASE_URL = "sqlite:///./content.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# Migration Plan (Stub)
# 1. Use Alembic for migrations
# 2. Run `alembic init` and configure
# 3. Add migration scripts for new models
