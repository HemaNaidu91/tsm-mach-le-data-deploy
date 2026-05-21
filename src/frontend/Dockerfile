FROM python:3.10-slim

WORKDIR /app

# Prevent Python from writing pyc files + improve logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade pip uv
#RUN uv pip install --no-cache-dir -r requirements.txt
RUN uv pip install --system --no-cache -r requirements.txt

# copy app
COPY . .

# expose streamlit port
EXPOSE 8501

# run streamlit
CMD ["sh", "-c", "streamlit run main.py --server.port=${PORT:-8501} --server.address=0.0.0.0"]
