from fastapi import APIRouter, Request
from models.note import Note
from config.db import conn
from schemas.note import notesEntity, noteEntity
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from bson import ObjectId

templates = Jinja2Templates(directory="templates")


note = APIRouter()


@note.get('/', response_class=HTMLResponse)
async def GetNotes(request: Request):
    doc = conn.notesdb.notes.find({})
    notes = notesEntity(doc)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"notes": notes}
    )


@note.post('/', response_class=HTMLResponse)
async def AddNote(request: Request):
    form = await request.form()
    inserted = conn.notesdb.notes.insert_one(dict(form))
    doc = conn.notesdb.notes.find({})
    notes = notesEntity(doc)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"notes": notes, 'message': 'Note inserted Successfully'}
    )


@note.get('/delete/{id}', response_class=RedirectResponse)
async def RemoveNode(id, request: Request):

    doc = conn.notesdb.notes.find_one_and_delete({
        '_id': ObjectId(id)
    })
    notes = conn.notesdb.notes.find({})
    return RedirectResponse('/')
