
# Getting Started

## Prerequisites
- **Python 3.9+**
- **pip** (for managing Python packages)
- **Git** (for version control)

## Installation Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/biocommunicator.git
    cd biocommunicator
    ```

2. **Set up a virtual environment (optional)**:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:

    ```bash
    python src/main.py
    ```

## Running Tests

To run all tests and ensure the code works as expected:

```bash
python -m unittest discover -s tests
```

Refer to the [Contributing Guidelines](contributing.md) if you would like to contribute to the project.
