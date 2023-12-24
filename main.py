from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from vonage import Sms, Client
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import pyotp
app = FastAPI()

origins = ["*"]  # Allow all origins for simplicity

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class SMSRequest(BaseModel):
    to: str
    text: Optional[str] = ""

def generate_otp():
    # Generate a 6-digit OTP using pyotp
    totp = pyotp.TOTP(pyotp.random_base32())
    return totp.now()


@app.post("/send-sms")
async def send_sms(sms_request: SMSRequest):
    otp = generate_otp()
    # Replace with your actual Vonage API key and secret
    # api_key = "your_api_key"
    # api_secret = "your_api_secret"

    # client = Client(key=api_key, secret=api_secret)
    # sms = Sms(client)

    # try:
    #     # Send SMS
    #     response = sms.send_message({
    #         "from": "Vonage APIs",
    #         "to": sms_request.to,
    #         "text": sms_request.text,
    #     })

    #     # Check if the message was sent successfully
    #     if response["messages"][0]["status"] == "0":
    #         return {"status": "Message sent successfully"}
    #     else:
    #         error_text = response["messages"][0]["error-text"]
    #         raise HTTPException(status_code=500, detail=f"Failed to send SMS: {error_text}")
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Failed to send SMS: {str(e)}")
    return {"status": "Message sent successfully",'otp':otp}
@app.get('/')
def hello(req):
    return 'hello'