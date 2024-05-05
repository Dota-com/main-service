from fastapi import FastAPI


app = FastAPI()


@app.post("/auth/register")
def register() -> int:
    if token:
        return "ok"
    return "}{yi"


