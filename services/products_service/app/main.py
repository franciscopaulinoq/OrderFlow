from fastapi import FastAPI

app = FastAPI(
    title="Products Service",
    description="API for managing product catalog.",
    version="0.0.1",
)

@app.get("/")
async def root():
    return {"message": "Welcome to Product Service!"}