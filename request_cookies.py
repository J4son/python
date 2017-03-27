# coding=utf-8
import requests

requests.cookies.RequestsCookieJar()
with requests.Session() as req:
    req.get('http://192.168.1.1', auth=('admin','Espace01'))

print(req.cookies)
if req.cookies:
    print("yes we hack!")
else:
    print("pas de cookies!")
