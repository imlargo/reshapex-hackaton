from fastapi import FastAPI

app = FastAPI(title="SICK Application Engineer")


@app.get("/api/health")
async def health() -> dict:
    return {"ok": True}
