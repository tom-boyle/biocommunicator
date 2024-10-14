
# Contributing Guide

We appreciate contributions to Biocommunicator! Follow these steps to contribute:

1. **Fork the repository**: Click the "Fork" button in the top-right corner.
2. **Clone your fork**:

    ```bash
    git clone https://github.com/yourusername/biocommunicator.git
    cd biocommunicator
    ```

3. **Create a new branch for your feature or bug fix**:

    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Make your changes** and ensure all tests pass:

    ```bash
    python -m unittest discover -s tests
    ```

5. **Push your changes** to your fork:

    ```bash
    git push origin feature/your-feature-name
    ```

6. **Submit a pull request** to the `develop` branch. A project maintainer will review it.
