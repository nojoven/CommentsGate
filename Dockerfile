FROM python:3.10.3-bullseye

WORKDIR /CommentsGate
RUN pip install "fastapi[all]"
COPY ./requirements.txt /CommentsGate/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /CommentsGate/requirements.txt


COPY ./app /CommentsGate/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



