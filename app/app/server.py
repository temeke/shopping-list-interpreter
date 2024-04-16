from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], 
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class Item(BaseModel):
    text: str

def process_with_langchain(text: str) -> str:
    print(text)
    # Oleta, että tämä funktio prosessoi tekstiä Langchainin avulla
    # Tämä esimerkki vain palauttaa alkuperäisen tekstin, korvaa tämä oikealla logiikallasi
    return text

@app.post("/process/")
async def update_shopping_list(item: Item):
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.getenv('TODOIST_API_KEY')
    from todoist_api_python.api import TodoistAPI

    api = TodoistAPI(api_key)

    try:
        projects = api.get_projects()
        print(projects)
        shopping_list_project = next((project for project in projects if project.name == 'shopping-list'), None)
        if shopping_list_project:
            print(f"Found project: {shopping_list_project.name} with ID: {shopping_list_project.id}")
            print(shopping_list_project)
        else:
            print("Shopping list project not found.")
    except Exception as error:
        print(error)
        
    try:
        tasks = api.get_tasks()
        print(shopping_list_project.id)
        project_tasks = [task for task in tasks if task.project_id == shopping_list_project.id]

        print(project_tasks)
    except Exception as error:
        print(error)

    processed_text = process_with_langchain(item.text)
    return processed_text
    todoist_response = add_to_todoist(processed_text)
    return {"Todoist Response": todoist_response}

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=3000, reload=True)