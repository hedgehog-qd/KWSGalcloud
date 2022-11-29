FROM python:3.9

WORKDIR ./docker

ADD . .

RUN pip3.9 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]