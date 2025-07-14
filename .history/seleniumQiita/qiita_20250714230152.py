# seleniumの必要なライブラリをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By

# tkinter（メッセージボックス表示）の必要なライブラリをインポート
import tkinter
from tkinter import messagebox

# Chrome Webドライバーのインスタンスを生成
driver = webdriver.Chrome()

#WebドライバーでQiitaログインページを起動
driver.get('https://qiita.com/login')

# NAMW属性が"identity"であるHTML要素を取得し、ログインID文字列をキーボード送信
driver.find