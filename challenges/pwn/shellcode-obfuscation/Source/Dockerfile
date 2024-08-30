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
ENV FLAG1="flag-X9F3K7ZQ2JPXLMN4V5QW8TYC6DZ8JR6A"
ENV OBF_FLAG1="flag-ML5V9JD3K8WTYQZA7R6YA2C3DZ8V7T1B"
ENV OBF_FLAG2="flag-N4LU7V5Q2C3DZ8JKR6YA2PXLMW4ZQVT1"
ENV OBF_FLAG3="flag-R6YA2C3DZ8V7T9JPX9F3K7ZQ2JPXLMN4"
EXPOSE ${PORT} 

CMD python3 api.py
