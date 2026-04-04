FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .  
#this id for the source code

#copy reuirements.txt first becuase its the longest step
CMD ["sh", "-c", "sleep 5 && alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]