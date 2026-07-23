from fastapi import FastAPI

app = FastAPI(
    title="FlipIntel API",
    description="Retail intelligence platform for resellers",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "name": "FlipIntel",
        "status": "online",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "healthy": True
    }