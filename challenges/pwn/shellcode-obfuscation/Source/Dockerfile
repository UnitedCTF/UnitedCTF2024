FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser
RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python3 -m pip install -r requirements.txt

RUN apt update
RUN apt upgrade -y
RUN apt install gcc -y
RUN apt install binutils -y
RUN apt install nasm -y
COPY exec_shellcode.c .
RUN gcc -z execstack -fno-stack-protector -o exec_shellcode exec_shellcode.c
RUN chown appuser:appuser exec_shellcode
USER appuser

COPY . .

ENV PORT=8000
ENV FLAG1=FLAG1
ENV OBF_FLAG1=FLAG2
ENV OBF_FLAG2=FLAG3
ENV OBF_FLAG3=FLAG3
EXPOSE ${PORT} 

CMD python3 api.py
