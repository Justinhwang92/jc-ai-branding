from fastapi import FastAPI, HTTPException
from ai_branding import generate_branding_snippet, generate_keywords

app = FastAPI()

MAX_INPUT_LENGTH = 32


@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet}


@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    keywords = generate_keywords(prompt)
    return {"keywords": keywords}


@app.get("/generate_snippet_and_keywords")
async def generate_snippet_and_keywords_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}


def validate_input_length(prompt: str):
    if len(prompt) > MAX_INPUT_LENGTH:
        # https://fastapi.tiangolo.com/tutorial/handling-errors/
        raise HTTPException(
            status_code=400, detail=f"Input length is too long. Must be {MAX_INPUT_LENGTH} characters or less.")

# python3 -m uvicorn ai_branding_api:app --reload
# http://127.0.0.1:8000/generate_snippet_and_keywords?prompt=
