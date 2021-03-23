# use python container image
From python:3.8

# set the working directory of the image filesystem 
WORKDIR /back
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]