from sqlalchemy.orm import DeclarativeBase

from k8s_web_app.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
