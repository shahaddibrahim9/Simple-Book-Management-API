from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, crud
from app.database import engine, Base, get_db
from app.auth import authenticate_user

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Management API",
    version="1.0.0",
    description="Manage a collection of books with CRUD operations."
)

@app.post("/api/books", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), user: str = Depends(authenticate_user)):
    return crud.create_book(db, book)

@app.get("/api/books", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit)

@app.get("/api/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/api/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, updates: schemas.BookUpdate, db: Session = Depends(get_db), user: str = Depends(authenticate_user)):
    book = crud.update_book(db, book_id, updates)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete("/api/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db), user: str = Depends(authenticate_user)):
    if crud.delete_book(db, book_id):
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
