# 1. Используем официальный образ Python как основу
FROM python:3.11-slim

# 2. Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Копируем файл с зависимостями и устанавливаем их (используем кэш)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копируем весь остальной код приложения
COPY . .

# Создаем пользователя appuser
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Переключаемся на этого пользователя
USER appuser

# Указываем команду для запуска (она выполнится от имени appuser)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
