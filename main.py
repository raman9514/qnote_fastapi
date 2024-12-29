from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.notes import note
# from pymongo import MongoClient

app = FastAPI()
app.include_router(note)

app.mount("/static", StaticFiles(directory="static"), name="static")


# conn: MongoClient = MongoClient(
#     'mongodb+srv://raman9514:admin@cluster0.5lkypkz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


# @app.get("/", response_class=HTMLResponse)
# async def root(request: Request):
#     doc = conn.notesdb.notes.find({})
#     notes = list()
#     notes.append({
#         'title': 'THis is first note',
#         'description': 'buy me some vegii'
#     })
#     for note in doc:
#         notes.append({
#             'title': note['title'],
#             'description': note['description']
#         })
#     return templates.TemplateResponse(
#         request=request, name="index.html", context={"notes": notes}
#     )
