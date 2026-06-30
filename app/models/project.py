from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.database.db import Base


class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    prompt = Column(String, nullable=False)

    script = Column(String)

    audio = Column(String)

    video = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )