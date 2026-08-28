FROM public.ecr.aws/docker/library/python:3.9

COPY . /opt/program
WORKDIR /opt/program



RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
