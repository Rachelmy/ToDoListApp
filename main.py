from fastapi import FastAPI, HTTPException

app = FastAPI()


# Root endpoint to verify the app is running
@app.get("/")
def root():
    return {"status": "running", "message": "FastAPI is alive"}