from app.db.session import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)
