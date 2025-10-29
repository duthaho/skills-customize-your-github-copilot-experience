# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a RESTful API using the FastAPI framework by creating a simple task management system. You'll practice creating endpoints, handling HTTP methods, working with JSON data, and implementing basic CRUD operations.

## 📝 Tasks

### 🛠️ Create a Task Management API

#### Description
Build a REST API that manages a collection of tasks. The API should support creating, reading, updating, and deleting tasks. Each task should have an ID, title, description, and completion status. Use FastAPI to implement the endpoints and handle data validation.

#### Requirements
Completed program should:

- Create a FastAPI application with proper imports and setup
- Implement a GET endpoint to retrieve all tasks
- Implement a GET endpoint to retrieve a specific task by ID
- Implement a POST endpoint to create a new task with title and description
- Implement a PUT endpoint to update an existing task
- Implement a DELETE endpoint to remove a task by ID
- Use Pydantic models for request and response data validation
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include proper error handling for invalid task IDs


### 🛠️ Add Task Filtering and Status Management

#### Description
Enhance your API by adding functionality to filter tasks and manage their completion status. This will help you practice working with query parameters and updating specific fields in your data.

#### Requirements
Completed program should:

- Add a boolean `completed` field to the task model (default: False)
- Implement a PATCH endpoint to mark a task as completed or incomplete
- Add query parameters to the GET all tasks endpoint to filter by completion status
- Return only completed tasks when the filter parameter is set to "completed"
- Return only incomplete tasks when the filter parameter is set to "incomplete"
- Test all endpoints using FastAPI's built-in interactive documentation (Swagger UI)
