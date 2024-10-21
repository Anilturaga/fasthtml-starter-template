# FastHTML Starter Template

This is a simple starter template for creating a webapps using FastAPI.

## Features
- username based authentication and protected routes
- DaisyUI and TailwindCSS for styling
- Lucide icons


## Installation
1. Clone the repository
2. Create a virtual environment
```bash
python -m venv .venv
```
3. Install the dependencies
```bash
pip install -r requirements.txt
```
4. Run the app
```bash
uvicorn main:app --reload
```

## Change theme
DaisyUI provides a lot of themes. Change to appropriate theme by modifying the tailwind.config attribute and the input of fast_app in `main.py`.


## Folder Structure
```
├── README.md
├── auth
│   └── loginHandler.py
├── backend
│   └── index.py
├── main.py
├── pages
│   ├── components
│   │   ├── header.py
│   │   └── loginDialogIndex.py
│   └── index.py
├── pyproject.toml
├── requirements.txt
└── utils.py
```

## Resources
- The FastHTML documentation at https://docs.fastht.ml/ provides comprehensive information on using the framework.
- For LLM assisted development, add the file at https://docs.fastht.ml/llms-ctx.txt as context.
- When converting DaisyUI or HTML code to FastHTML Python code, the converter tool at https://h2x.answer.ai/ can be helpful.

> Note: This is a simple starter template and is not production ready. Use it as a starting point for your projects.
