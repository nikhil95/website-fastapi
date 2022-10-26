import win32api
from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List

#for sencond endpoint
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
from fastapi import FastAPI, Request,Form

from fastapi import FastAPI, status, HTTPException
from database import engine
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import Base,Contact,Subscription,Demo
from schema import DemoRequest
from schema import ContactRequest
from schema import SubscriptionRequest
# Create the database
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(bind=engine)
session=Session()
Base.metadata.create_all(engine)


class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME = "testnikhil67@gmail.com",
    MAIL_PASSWORD = "dkyghxnnxddqnhrq",
    MAIL_FROM = "testnikhil67@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False,

    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

app = FastAPI()

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

html = """
<p>Your Response has been submitted</p>
"""




@app.post("/contact")
async def contact_us(obj:ContactRequest):
    contact=Contact(name=obj.name,email=obj.email,message=obj.message)
    session.add(contact)
    session.commit()
    message = MessageSchema(
        subject="Rezlytix Contact Request",
        recipients=["nikhil.ranjan@rezlytix.com"],  # List of recipients, as many as you can pass 
        body=html,
        subtype="html"
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "successfully inserted and email has been sent"})
    

        

@app.post("/contact_form",response_class=HTMLResponse)
async def contact_us_insert(request: Request,name: str = Form(), email: str = Form(),message: str = Form()):
    contact=Contact(name=name,email=email,message=message)
    session.add(contact)
    session.commit()
    message = MessageSchema(
        subject="Rezlytix Contact Request",
        recipients=["nikhil.ranjan@rezlytix.com"],  # List of recipients, as many as you can pass 
        body=html,
        subtype="html"
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    #return JSONResponse(status_code=200, content={"message": "successfully inserted and email has been sent"})
    win32api.MessageBox(0, 'Response Submited and email has been sent!', 'Running a Python Script via Javascript', 0x00001000)
    return templates.TemplateResponse("contact-us.html", {"request": request})

@app.get("/contact")
async def fetch_contact_us():
    contact=session.query(Contact).all()
    return contact

@app.post("/subscription")
async def subscription(obj:SubscriptionRequest):
    subscription=Subscription(email=obj.email,active=True)
    session.add(subscription)
    session.commit()
    return "inserted"

@app.post("/subscription_form",response_class=HTMLResponse)
async def subscription_insert(request: Request,email: str = Form()):
    contact=Subscription(email=email,active=True)
    session.add(contact)
    session.commit()
    win32api.MessageBox(0, 'Response Submited!', 'Running a Python Script via html-form', 0x00001000)
    return templates.TemplateResponse("contact-us.html", {"request": request})

@app.get("/subscription")
async def fetch_subscription():
    subscription=session.query(Subscription).all()
    return subscription

@app.post("/Demo")
async def demo(obj:DemoRequest):
    demo=Demo(name=obj.name,company_name=obj.company_name,email=obj.email,position=obj.position,phone_no=obj.phone_no,services=obj.services)
    session.add(demo)
    session.commit()
    return "inserted"

@app.post("/Demo_form",response_class=HTMLResponse)
async def demo(request: Request,name: str = Form(),company_name:str = Form(), email: str = Form(),position: str = Form(),phone_no: int = Form(),services: list = Form()):
    services=str(services)
    demo=Demo(name=name,company_name=company_name,email=email,position=position,phone_no=phone_no,services=services)
    session.add(demo)
    session.commit()
    win32api.MessageBox(0, 'Response Submited!', 'Running a Python Script via html-form', 0x00001000)
    return templates.TemplateResponse("demo.html", {"request": request})

@app.get("/Demo")
async def fetch_demo():
    demo=session.query(Demo).all()
    return demo
"""
@app.post("/test")
async def display(name:str,email:str,message:str):
    return name+"--"+email+"---"+message

@app.post("/test1")
async def display():

    import cgi
    form = cgi.FieldStorage()
    name =  form.getvalue('name')
    return name


@app.get('/test')
def test():
    
    
    win32api.MessageBox(0, 'You have just run a python script on the button press!', 'Running a Python Script via Javascript', 0x00001000)
    return "success"
"""
