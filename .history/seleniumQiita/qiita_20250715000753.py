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

# NAME属性が"identity"であるHTML要素を取得し、ログインID文字列をキーボード送信(elementに「name="identity"」と書いてある部分)
driver.find_element(By.NAME,"identity").send_keys("vacky0405@gmail.com")
# NAME属性が"password"であるHTML要素を取得し、パスワード文字列をキーボード送信
driver.find_element(By.NAME,"password").send_keys("@84XputXyjT9SqZ")
# CLASS属性が"sessions_button--wide"であるHTML要素をクリック
driver.find_element(By.CLASS_NAME, "sessions_button--wide").click()
# CLASS属性が複数ある要素は「.」で取得できる
# 例）< ... class="btn btn_login btn_default" ...のような場合、
#                "btn.btn_login.btn_default"でfind_elemetする

# マイページへ移動
driver.get('https://qiita.com/vacky0405')

try:
    wait = WebDriverWait
# Contributions数を取得（CLASS属性が"style-1snuvpu"のHTML要素を取得してテキストを取得）
cobCnt = driver.find_element(By.CLASS_NAME, "style-1snuvpu").text

# Contributions数のメッセージボックス表示
root = tkinter.Tk()
root.withdraw()
messagebox.showinfo("selenium sample", "現在、" + cobCnt + "Contributionsです。本日も張り切ってアウトプットしていこう！")

# Webドライバーのセッションを終了
driver.quit()
