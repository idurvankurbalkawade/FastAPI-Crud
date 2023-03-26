FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN python -m pip install --upgrade pip


COPY . .

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]