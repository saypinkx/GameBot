from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from server.routers.user import user_router
from server.routers.form import form_router

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()
app.include_router(user_router)
app.include_router(form_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8180", "http://185.221.152.242:8180"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7000)


app.mount("/server/static", StaticFiles(directory="./server/static"), name='static')

templates = Jinja2Templates(directory="./server/templates")




@app.get("/form", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse(
        request=request, name="FormCreate.html")

