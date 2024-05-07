from main_service.routes import auth

from fastapi import FastAPI


app = FastAPI()

app.include_router(auth.auth)






