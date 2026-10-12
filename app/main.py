from fastapi import FastAPI
app = FastAPI(
    title= "Overload",
    description= " Tracks workouts and body weight, and flags stalled lifts and missed sessions.",
)
@app.get("/health")
def health():
    return{"status": "ok"}