# レスポンス処理用
from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI(
    title='FastAPIで作るtoDoアプリケーション'、
    description='FastAPIty'
)
