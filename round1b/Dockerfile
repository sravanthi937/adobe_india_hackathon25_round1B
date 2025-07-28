FROM python:3.9-slim

WORKDIR /app

COPY . .

# Force upgrade pip and skip hash checks
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org pymupdf sentence-transformers scikit-learn --disable-pip-version-check

CMD ["python", "selector_b.py"]
