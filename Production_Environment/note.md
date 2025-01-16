# Project File Descriptions

This document provides an overview of the key files included in this project, explaining their purpose and differences.

---

## **setup.py**

- **Purpose**:
  - This file is used for packaging and distribution of the project.
  - It defines the metadata and dependencies for the project.

- **Key Components**:

  - `name`, `version`, `description`: Metadata for the package.
  - `install_requires`: Lists the dependencies required to run the package.
  - `packages`: Specifies the directories containing Python code to be included.
- **Use Case**:
  - Used when creating a source distribution or installing the package via `pip install .`.

---

## **pyproject.toml**
- **Purpose**: 
  - Defines the build system and configuration for the project.
  - Serves as a modern replacement for `setup.py` in many cases.
- **Key Sections**:
  - `[build-system]`: Specifies build requirements and backend.
  - `[tool.pytest.ini_options]`: Configures pytest settings for the project.
  - `[tool.black]`: Configures Black for code formatting.
  - `[tool.isort]`: Configures isort for import sorting.
- **Use Case**:
  - Used by modern build tools like `pip` and `build`.
  - Can integrate testing, formatting, and other tools in a centralized way.

---

## **MANIFEST.in**
- **Purpose**:
  - Specifies additional files to include or exclude when creating a source distribution.
- **Key Commands**:
  - `include`, `exclude`, `recursive-include`, `recursive-exclude`: Control which files are packaged.
  - `prune`: Removes empty directories from the source distribution.
- **Use Case**:
  - Ensures non-Python files (e.g., `README.md`, `VERSION`) are included in the package.

---

## **mypy.ini**
- **Purpose**:
  - Configures the MyPy static type checker.
- **Key Goals**:
  - Enforce type-checking practices.
  - Ignore incomplete or legacy code where necessary.
- **Use Case**:
  - Ensures type safety and catches potential issues before runtime.


---

## **Tests Directory (e.g., `tests/`)**
- **Purpose**:
  - Contains unit tests to verify the functionality of the project.
- **Use Case**:
  - Used with `pytest` or other testing frameworks to ensure code correctness.

---

## **Differences Between Key Files**

### **setup.py vs pyproject.toml**
| **Aspect**             | **setup.py**                              | **pyproject.toml**                      |
|------------------------|-------------------------------------------|------------------------------------------|
| Purpose               | Packaging and distribution.               | Build system and configuration.          |
| Syntax                | Python code.                              | TOML (human-readable configuration).     |
| Modernity             | Traditional method.                       | Newer, standardized method.              |
| Tool Integration      | Limited to setup and distribution.        | Integrates testing, formatting, and more.|

### **setup.py vs MANIFEST.in**
| **Aspect**             | **setup.py**                              | **MANIFEST.in**                          |
|------------------------|-------------------------------------------|------------------------------------------|
| Purpose               | Defines metadata and dependencies.        | Specifies additional files for packaging.|
| File Inclusion         | Python files by default.                  | Non-Python files can be specified.       |

### **mypy.ini vs pyproject.toml**
| **Aspect**             | **mypy.ini**                              | **pyproject.toml**                       |
|------------------------|-------------------------------------------|------------------------------------------|
| Purpose               | Configures type checking.                 | Centralizes various tool configurations. |
| Tool-Specific         | Dedicated to MyPy.                        | Supports multiple tools.                 |

---

