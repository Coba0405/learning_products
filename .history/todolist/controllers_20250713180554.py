# レスポンス処理用
from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI(
    title='FastAPIで作るtoDoアプリケーション',
    description='FastAPIチュートリアル',
    version='0.9 beta'
)

def index(request: Request):
    return {'Hello': 'World'}
