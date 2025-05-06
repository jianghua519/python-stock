# 使用 Python 基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制当前服务的代码
COPY ./app /app

# # 复制 shared 目录到容器中
# COPY ../../shared /app/shared

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 暴露服务端口
EXPOSE 8000

# 启动服务
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]