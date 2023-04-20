FROM pypy:latest
WORKDIR /app
COPY . /app
RUN requirements.txt
CMD python garden.py