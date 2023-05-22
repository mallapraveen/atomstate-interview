from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import uvicorn

from qa import qa

origins = [
    "*",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QAHuggingFace(BaseModel):
    question: str
    context: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/qa")
async def root(qa_hf: QAHuggingFace):
    question = qa_hf.question
    context = qa_hf.context
    result = qa(question, context)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
