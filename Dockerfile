FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py saline_aquifer_co2_storage_capacity_estimator.py ./

EXPOSE 7860

CMD ["python", "app.py"]
