from fastapi import FastAPI



# Команда для старта приложения
# uvicorn app.main:app

app = FastAPI()

@app.get("/")
def root():
    return {"message": "work"}