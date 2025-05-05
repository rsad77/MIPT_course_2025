from sqlalchemy.orm import Session
from app import models, schemas, auth



def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_book(db: Session, book: schemas.BookCreate):
    db_genre = db.query(models.Genre).filter(models.Genre.id == book.genre_id).first()
    if not db_genre:
        raise ValueError("Genre not found")

    db_book = models.Book(
        title=book.title,
        author=book.author,
        year=book.year,
        genre_id=book.genre_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()