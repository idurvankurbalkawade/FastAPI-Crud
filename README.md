# FastAPI-Crud

Crud Operations in FastAPI using PostgreSQL as Database

### To build docker image from dockerfile, run following command
docker build -t fastapi .

### To run docker container, run following command
docker run --name myapp --link psql -p 8000:8000 fastapi

### For database, used postgresql official docker image from docker hub, use following commands 
docker pull postgres
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres