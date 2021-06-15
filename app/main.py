from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import app.services as _services
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"))

templates = Jinja2Templates(directory="app/templates/")


@app.get("/meme")
def get_meme():
    image_path = _services.select_random_image("app/static/images/memes")
    return FileResponse(image_path)


@app.get("/meme_list")
def get_meme_list():
    memes = _services.get_image_filenames("app/static/images/memes")
    return {"memes": memes}


@app.post("/meme_upload")
def post_meme(file: UploadFile = File(...)):
    file_name = _services.upload_image("app/static/images/new_memes", file)
    if file_name is None:
        return HTTPException(status_code=409, detail="incorrect file type")
    return FileResponse(file_name)


@app.get("/", tags=["root"])
def get_root(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
