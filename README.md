# ORKG Template Python Prototype

This repository contains a minimal Python script, based on the ORKG Python package documentation in order to load an ORKG template, populate it with dummy values, and store it in the ORKG Sandbox. 

## Current Progress

- Successful authentication against the ORKG Sandbox
- Connectivity verified via `orkg.ping()`
- Template inspection via `get_template_specifications(template_id)`
- Template materialization via `materialize_template(template_id)`
- Auto-generated Python functions created for templates (e.g. NLP4RE ID Card, Empirical Research Practice)
- Create and save template instances in ORKG Sandbox 

## Environment Setup

1. Create and activate the virtual environment (Windows)

```
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Create a .env file and add your ORKG credentials

```
ORKG_EMAIL=your_email
ORKG_PASSWORD=your_password
```

4. Run the prototype script

```
python main.py
```