## 🧮 DSL for Matrix Operations

A web-based compiler and interpreter for a Domain-Specific Language (DSL) designed specifically for matrix operations. This full-stack project allows users to write DSL commands in a browser-based editor and get instant results. Built using **React** for the frontend and **Python** for the backend.

---

### 📁 Project Structure

```
PBL/
├── backend/
│   ├── compiler/
│   │   ├── ast.py           # Abstract Syntax Tree definitions
│   │   ├── executor.py      # Evaluation and execution of IR
│   │   ├── ir.py            # Intermediate representation
│   │   ├── lexer.py         # Tokenizer
│   │   ├── parser.py        # Parser for the DSL
│   │   ├── semantic.py      # Semantic analyzer
│   │   └── __init__.py
│   ├── app.py               # Flask API for DSL execution
│   └── requirements.txt     # Backend dependencies
├── frontend/
│   ├── public/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── README.md
```

---

### 💡 Features

* Custom matrix-focused DSL with intuitive syntax
* Tokenization, parsing, semantic analysis, and execution handled in Python
* Frontend interface with code editor and real-time output
* API integration between React frontend and Python backend
* Error handling and syntax validation

---

### 📜 DSL Syntax Examples

```dsl
# Matrix declarations
matrix A = [[1, 2], [3, 4]]
matrix B = [[5, 6], [7, 8]]

# Matrix operations
matrix C = A + B
matrix D = A * B
matrix E = transpose(A)
matrix F = inverse(A)
scalar d = determinant(A)

# Element access
scalar x = A[0][1]
```

---

### 🚀 Getting Started

#### 🔧 Backend Setup (Python + Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

By default, the Flask server runs at `http://localhost:5000`.

---

#### 💻 Frontend Setup (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on `http://localhost:5173`.

---

### 🔌 API Endpoint

#### POST `/evaluate`

* Accepts DSL code and returns evaluation results.

**Request:**

```json
{
  "code": "matrix A = [[1, 2], [3, 4]]"
}
```

**Response:**

```json
{
  "result": {
    "A": [[1, 2], [3, 4]]
  }
}
```

---

### ⚙️ Internals

| Component     | Description                                   |
| ------------- | --------------------------------------------- |
| `lexer.py`    | Converts source code into tokens              |
| `parser.py`   | Parses tokens into an AST                     |
| `semantic.py` | Checks for semantic errors (e.g., type match) |
| `ir.py`       | Generates an intermediate representation      |
| `executor.py` | Evaluates the IR and returns results          |
| `app.py`      | Flask API interface                           |

---

<!-- ### 🌐 Live Demo

If hosted, link here. Otherwise, instructions in the usage section help users run locally.

--- -->


### 🤝 Contributing

We @prachisah1 ,@gunjanbhanwal and @Richarani-tarase
have contributed to this project and will plane to add more features in future.

---
