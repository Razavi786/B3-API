from flask import Flask,request
from pvb3 import b3
import httpx
import time
import asyncio
import random

app = Flask("B3 API")

def format_proxy(proxy):
	ip,port,user,pas = map(str.strip,proxy.split(":"))
	return user+':'+pas+'@'+ip+':'+port

proxies = [
	"p.webshare.io:80:tmwykaqz-1:aba398innfss"
	"p.webshare.io:80:tmwykaqz-2:aba398innfss",
	"p.webshare.io:80:tmwykaqz-3:aba398innfss",
	"p.webshare.io:80:tmwykaqz-4:aba398innfss",
	"p.webshare.io:80:tmwykaqz-5:aba398innfss",
	"p.webshare.io:80:tmwykaqz-6:aba398innfss"
	"p.webshare.io:80:tmwykaqz-7:aba398innfss",
	"p.webshare.io:80:tmwykaqz-8:aba398innfss",
	"p.webshare.io:80:tmwykaqz-9:aba398innfss",
	"p.webshare.io:80:tmwykaqz-10:aba398innfss"
	]

@app.route("/api/b3",methods=["GET","POST"])
async def b3api():
	cc = request.args.get("cc")
	if not cc:
		return {"error":"Please Provide A Valid CC"}
	api = "https://www.bebebrands.com"
	proxy = format_proxy(random.choice(proxies))
	client = httpx.AsyncClient(timeout=30,proxy="http://"+proxy)
	start = time.time()
	response = await b3(api,cc,client)
	return {"cc":cc,"response":response,"taken":f"{(time.time()-start):.2f} seconds"}

@app.route("/",methods=["GET","POST"])
async def index():
	return "Alive"

if __name__ == "__main__":
	asyncio.run(app.run())
