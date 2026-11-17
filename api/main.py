from fastapi import FastAPI, Depends

from .routers import applicationsRouter, employersRouter, vacanciesRouter, stats
from .security import require_api_key

app = FastAPI(
    title="Job & Employability Progression API",
    description=(
        "REST API for the Job & Employability Progression Management System. "
        "It reads and writes the same SQLite database as the Django web application."
    ),
    version="1.0.0",

)
@app.get("/health", tags=["System"])
def health():
    """Public check that the service is running (no API key needed)."""
    return {"status": "ok"}


protected = [Depends(require_api_key)]
app.include_router(employersRouter.router, dependencies=protected)
app.include_router(vacanciesRouter.router, dependencies=protected)
app.include_router(applicationsRouter.router, dependencies=protected)
app.include_router(stats.router, dependencies=protected)
