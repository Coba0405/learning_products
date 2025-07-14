# レスポンス処理用
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import db
from models import User, Task

app = FastAPI(
    title='FastAPIで作るtoDoアプリケーション',
    description='FastAPIチュートリアル',
    version='0.9 beta'
)

templates =  Jinja2Templates(directory="templates")
jinja_env = templates.env

def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

def admin(request: Request):
    user = db.session.query(User).filter(User.username == 'admin').first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all
    
    return templates.TemplateResponse('admin.html', {'request': request, 'usename': 'admin'})
