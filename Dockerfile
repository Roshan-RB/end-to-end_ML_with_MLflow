# Use a modern Python version
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install OS dependencies (needed for numpy, pandas, sklearn)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full project
COPY . .

# Streamlit uses port 8501
EXPOSE 8501

# Streamlit run command
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
