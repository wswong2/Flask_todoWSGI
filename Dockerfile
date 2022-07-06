FROM python
COPY . /app
WORKDIR /app

RUN python -m pip install \
		 flask \
		 flask_sqlalchemy \
		 SQLAlchemy \
		 waitress


CMD ["python", "app.py"]
EXPOSE 5000


		

#
# https://realpython.com/python-versions-docker/