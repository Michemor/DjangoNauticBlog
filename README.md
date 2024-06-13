# INTRODUCTION

This is a project to practice and learn django while creating a blog.

## WHAT IS DJANGO

> Django is a python framework used to build dynamic web applications.
> It utilizes a Model, View, Template architecture.

### MODELS

Models are a class which represent a table in a database
>>Each data (i.e Articles, Users) is represented by its own model
>>Each model maps to a single table in a database

#### Code

``` python

Class Article():
    title = models.CharField()
    body = models.TextField()

```

#### Articles Table

id  Title   body
1   Name    John
2   Name    John
3   Name    John

### MIGRATIONS

> A model is created to map to a table in a database
> Our database doesn't know about our models
When we make a model, we migrate it to the database so that it can create a table and other fields.
> Migration files tracks changes made to a model

```bash

python manage.py makemigrations # makes migrations
python manage.py migrate # migrates the changes

```
