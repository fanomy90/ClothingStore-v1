FROM python:3.8

SHELL ["/bin/bash", "-c"]


# Настройки виртуального окружения: запрет создания кэш файлов и запрет буферизации сообщений с логами 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Обновим pip
RUN pip install --upgrade pip
# Установим дополнительные пакеты в контейнер
RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim
# Создадим нового пользователя для работы в контейнере
RUN useradd -rms /bin/bash store/ && chmod 777 /opt /run
# Создание и переход в каталог /yt
WORKDIR /store
# Создадим директории для файлов джанго в папке пользователя и дадим пользователю права на чтение и запись
RUN mkdir /store/static && mkdir /store/media && chown -R store:store /store && chmod 755 /store
# Меняем владельца каталогов и файлов на пользователя yt и копируем файлы из текущего каталога (где лежит Dockerfile) в рабочий каталог /yt
COPY --chown=store:store . .
# Установим зависимости проекта
RUN pip install -r requirements.txt
#новая версия click, которая не совместима с текущей версией Celery.
#RUN pip install --upgrade celery
# Установим права на выполнение для manage.py
RUN chmod +x manage.py
# Переключаемся на пользователя
USER store
# Запускаем проект с портом 8001, с веб сервером gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8001", "store.wsgi:application"]
# Зайдем в директорию на сервере где лежит Dockerfile и выполним команду docker build - t yt_django