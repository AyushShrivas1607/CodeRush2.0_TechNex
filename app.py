import random
import time
from contextlib import asynccontextmanager
import jwt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import FastAPI, HTTPException, Header
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

# --- MODERN LIFESPAN EVENT HANDLER (Replaces deprecated @app.on_event) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("Model successfully loaded into memory for web service.")
    yield
    # Shutdown logic (optional)
    print("Application shutting down...")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="templates"), name="static")

JWT_SECRET = "SPACEOPS_SUPER_SECURE_JWT_SECRET_KEY_9988!"
active_challenges = {}

# --- SMTP CONFIGURATION ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "ayushshrivas168@gmail.com" 
SENDER_PASSWORD = "yvkh vfry muqp obkk"

class EmailRequest(BaseModel):
    email: str

class VerifyRequest(BaseModel):
    email: str
    code: str

def send_email_code(recipient_email: str, code: str):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = "Secure Mission IdP - Your 2SV Verification Code"

        body = f"""
        Hello,

        Your authentication code for the Secure Mission IdP Gateway is:

        {code}

        This code will expire in 5 minutes.
        """
        msg.attach(MIMEText(body, 'plain'))

        print(f"[SMTP] Attempting to connect to Google SMTP server for {recipient_email}...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        server.quit()
        print(f"[SMTP SUCCESS] Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"[SMTP CRITICAL ERROR] Could not send email: {str(e)}")
        raise HTTPException(status_code=500, detail=f"SMTP Error: {str(e)}")

@app.get("/")
def read_root():
    return RedirectResponse(url="/static/index.html")

@app.post("/api/auth/request-passkey")
def request_passkey(data: EmailRequest):
    code = str(random.randint(100000, 999999))
    active_challenges[data.email] = {
        "code": code,
        "expires": time.time() + 300
    }
    
    # Triggers the actual email sending function
    send_email_code(data.email, code)
    
    return {"success": True, "message": f"OOB Code dispatched successfully to {data.email}"}

@app.post("/api/auth/verify-2sv")
def verify_2sv(data: VerifyRequest):
    challenge = active_challenges.get(data.email)
    
    if not challenge or challenge["expires"] < time.time():
        raise HTTPException(status_code=401, detail="2SV challenge expired or not found.")
    
    if challenge["code"] != data.code:
        raise HTTPException(status_code=401, detail="Invalid 2SV verification code.")
    
    del active_challenges[data.email]
    
    token = jwt.encode({"email": data.email, "role": "FlightDirector"}, JWT_SECRET, algorithm="HS256")
    return {"success": True, "token": token, "message": "Authentication successful."}

@app.post("/api/mission/execute")
def execute_mission(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="No authorization token provided.")
    
    token = authorization.split(" ")[1]
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return {"success": True, "message": "Procedure executed successfully under verified session."}
    except jwt.PyJWTError:
        raise HTTPException(status_code=403, detail="Invalid or expired session token.")

@app.get("/api/telemetry/live")
def get_live_telemetry():
    return {
        "timestamp": time.time(),
        "cpu_load": round(random.uniform(15.0, 85.0), 2),
        "memory_usage": round(random.uniform(40.0, 90.0), 2),
        "ai_confidence": round(random.uniform(88.0, 99.9), 2)
    }