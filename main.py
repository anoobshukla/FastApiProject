from fastapi import FastAPI
import uvicorn 

app = FastAPI(
    title="I4E Python APIs",
    description="I4E Python FastAPI using Swagger and Sqlalchemy",
    version="1.0.0",
)

@app.get("/hello")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
