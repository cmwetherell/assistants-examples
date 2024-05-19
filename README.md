# Assitant Examples

## Introduction

Welcome to the my repository exploring the use of AI Assistants! This repository contains several examples to help get you started. To get started with development, you need to set up a Poetry environment. Follow the steps below to clone the repository and set up the environment.

## Prerequisites

- Python 3.11
- [Poetry](https://python-poetry.org/) installed on your system

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/cmwetherell/assistant-examples.git
cd assistant-examples
```

### 2. Install Poetry

If you haven't already installed Poetry, you can do so by following the instructions on the [Poetry installation page](https://python-poetry.org/docs/#installation). For most systems, you can use the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Ensure that Poetry's bin directory is added to your PATH. You can add the following line to your shell configuration file (`.bashrc`, `.zshrc`, etc.):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

After editing your shell configuration file, reload it:

```bash
source ~/.bashrc  # or source ~/.zshrc for Zsh users
```

### 3. Install Dependencies

With Poetry installed, navigate to the project directory (if not already there) and install the project dependencies:

```bash
poetry install
```

This command will create a virtual environment and install all the dependencies specified in the `pyproject.toml` file.

### 4. Activate the Virtual Environment

To activate the virtual environment created by Poetry, use the following command:

```bash
poetry shell
```

Now you are ready to start working on the project!

### 5. Running the Project

To run the project, use the following command (modify according to your project's entry point):

```bash
python ./assistants_examples/article.py
```

## Additional Commands

Here are some additional Poetry commands you might find useful:

- **Add a new dependency**:
  ```bash
  poetry add <package-name>
  ```

- **Remove a dependency**:
  ```bash
  poetry remove <package-name>
  ```

- **Update dependencies**:
  ```bash
  poetry update
  ```

- **Run a script defined in pyproject.toml**:
  ```bash
  poetry run <script-name>
  ```

## Conclusion

You have successfully set up the Poetry environment for this project. If you encounter any issues or have any questions, please refer to the [Poetry documentation](https://python-poetry.org/docs/) or open an issue in this repository.

Happy coding!

---

Feel free to modify the instructions to fit the specific details and requirements of your project.