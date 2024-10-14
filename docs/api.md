
# API Documentation

Biocommunicator exposes several endpoints to interact with the system.

## Endpoints

### `POST /api/data`
- **Description**: Submit data for analysis by the AI models.
- **Request**:
    - `data`: The input data in JSON format.
- **Response**:
    - `result`: The analyzed output from the AI model in JSON format.

### `GET /api/status`
- **Description**: Retrieve the current status of the AI model and system.
- **Response**:
    - `status`: The system's current operational status in JSON format.
