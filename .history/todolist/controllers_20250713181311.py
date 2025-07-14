# レスポンス処理用
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI(
    title='FastAPIで作るtoDoアプリケーション',
    description='FastAPIチュートリアル',
    version='0.9 beta'
)

templates =  Jinja2Templates(directory="template")

def index(request: Request):
    return {'Hello': 'World'}
