FROM python
RUN pip install --upgrade pip
ENV APP_PATH /app
COPY requirements.txt $APP_PATH/
RUN pip install --no-cache-dir -r $APP_PATH/requirements.txt

# COPY app.py $APP_PATH/
# EXPOSE 80

CMD ["python", "/app/app.py"]



