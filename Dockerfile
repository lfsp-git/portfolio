# 1. Usamos uma imagem leve do Python (Alpine Linux)
FROM python:3.10-slim

# 2. Definimos a pasta de trabalho dentro do container
WORKDIR /app

# 3. Copiamos o arquivo de dependências primeiro (otimiza o cache)
COPY requirements* .

# 4. Instalamos as bibliotecas necessárias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos o resto do código (servidor.py, etc)
COPY . .

# 6. Expomos a porta 5000 (a porta do Flask)
EXPOSE 5000

# 7. O comando que inicia a nossa ferramenta
# Usamos o modo Web por padrão, mas o usuário pode sobrescrever via CLI
CMD ["python", "servidor.py"]