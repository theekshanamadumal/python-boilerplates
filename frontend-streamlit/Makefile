# Define variables
APP_NAME = app.py  # Change this to your Streamlit app file
PORT = 8501  # Default Streamlit port
ENV_NAME = streamlit-fe  # Default Streamlit port

# Create a virtual environment using venv and install dependencies
setup-venv:
	python -m venv $(ENV_NAME)
	. $(ENV_NAME)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Create a virtual environment using conda and install dependencies
setup-conda:
	conda create --name $(ENV_NAME)python=3.12 -y
	conda activate $(ENV_NAME) && pip install --upgrade pip && pip install -r requirements.txt

# Run the Streamlit app
run:
	streamlit run $(APP_NAME) --server.port $(PORT)
#	streamlit run $(APP_NAME) --server.port $(PORT)

# Format Python code
format:
	black $(APP_NAME)

# Lint the code using flake8
lint:
	flake8 $(APP_NAME)

# Clean up generated files
clean:
	rm -rf __pycache__
	rm -rf .streamlit

# Deactivate virtual environment
stop:
	deactivate