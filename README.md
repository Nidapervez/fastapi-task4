uv init fastdca_p1

cd fastdca_p1

uv venv

.venv\Scripts\activate

uv add "fastapi[standard]"

uv run python main.py

uv pip install pydantic


1. What is FastAPI?
FastAPI is a modern, high-performance web framework used to build APIs with Python. It is designed to be fast, intuitive, and developer-friendly. FastAPI leverages Python's type hints to automatically validate input data and generate interactive documentation.

2. Path Parameters
Path parameters are variables included directly in the URL path. They are used to identify specific resources. For example, if an API needs to fetch details of a specific user, the user ID can be passed in the URL itself.

Example usage:
/users/123 — Here, 123 is a path parameter representing the user's unique ID.

FastAPI automatically captures this value and makes it available in the function handling the request.

3. Query Parameters
Query parameters are key-value pairs provided in the URL after a question mark (?). They are commonly used for filtering, sorting, and pagination.

Example usage:
/products?category=books&limit=10 — Here, category and limit are query parameters.

Unlike path parameters, query parameters are optional by default, allowing for flexible API calls.

4. Request Body
The request body is used when sending structured data (usually in JSON format) to the server — for example, while creating a new user or submitting a form. FastAPI uses Python classes (models) to define the expected data and automatically performs validation based on those definitions.

5. Response Models
Response models define the structure of the data returned by the API. This ensures consistency, security, and clarity. For instance, even if the internal data includes sensitive information (like passwords), the response model can exclude those fields from being returned to the client.

6. Status Codes
FastAPI allows developers to define HTTP status codes for each response, indicating the result of an operation:

200 OK – Request succeeded.

201 Created – A new resource was created.

400 Bad Request – Invalid input provided.

404 Not Found – Resource not found.

Proper use of status codes helps in building clear and user-friendly APIs.

7. Dependency Injection
FastAPI supports dependency injection, a technique that allows reusable logic (like authentication, database access, or configuration) to be shared across multiple parts of an application. This promotes cleaner, more modular code.

8. Middleware
Middleware is a function that runs before or after every request. It can be used for tasks such as logging, adding security headers, tracking performance, or handling authentication. Middleware helps enforce application-wide behavior.

9. Interactive Documentation
FastAPI automatically generates interactive API documentation using Swagger UI and ReDoc. This feature allows developers and users to explore, test, and understand the API directly through a web interface without needing additional tools.
