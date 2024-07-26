from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Update with your actual SQL Server database connection string
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://sa:lincolnrassel40@DESKTOP-SVRQCC2/FastAPI?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
