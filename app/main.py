from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.api import nlp_api
from app.nlp import nlp_service

app = FastAPI(title="ParsePoint NLP API", 
              description="An NLP API for tokenization and POS tagging",
              version="0.1.0")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Include routers
app.include_router(nlp_api.router, prefix="/api", tags=["NLP API"])

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Render the main UI page
    """
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
