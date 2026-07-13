from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI(openapi_url = None)

@app.head("/")
async def status(): return Response()