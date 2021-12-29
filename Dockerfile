FROM python:3.9
COPY . /tech_exam
WORKDIR /tech_exam 
CMD ["python", "test.py"]