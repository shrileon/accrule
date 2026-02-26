from fastapi import FastAPI
import uvicorn

from app.routers import auth, accounts, users, categories, transactions


# Команда для старта приложения
# uvicorn app.main:app

app = FastAPI(title="Accrule", description="Accrule – finance app", version="0.0.1")

# Routers

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(transactions.router)


@app.get("/")
def root():
    '''
    Description: First test function
    '''
    return {"message": "work"}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)