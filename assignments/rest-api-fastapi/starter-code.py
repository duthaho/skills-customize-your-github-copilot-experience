from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# TODO: Define your Task model using Pydantic BaseModel
# Include fields: id (int), title (str), description (str), completed (bool)


# TODO: Create an in-memory storage for tasks (use a list or dictionary)
tasks = []


# TODO: Implement GET endpoint to retrieve all tasks
# Endpoint: GET /tasks
# Optional query parameter: status (completed/incomplete)


# TODO: Implement GET endpoint to retrieve a task by ID
# Endpoint: GET /tasks/{task_id}


# TODO: Implement POST endpoint to create a new task
# Endpoint: POST /tasks
# Request body should include title and description


# TODO: Implement PUT endpoint to update a task
# Endpoint: PUT /tasks/{task_id}
# Request body should include title and description


# TODO: Implement PATCH endpoint to update task completion status
# Endpoint: PATCH /tasks/{task_id}/complete
# Request body should include completed status (boolean)


# TODO: Implement DELETE endpoint to delete a task
# Endpoint: DELETE /tasks/{task_id}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
