# MVC with Flask

- Install Flask

`pip install flask`
- Create a file called `app.py`

- Create a folder called `templates`, and keep any HTML files in there
- Link files to certain addresses on the port with
```python
@app.route("/home/")
def home():
    return render_template("index.html")
```
- `flask run` connects, and Ctrl + C disconnects

- A template file can be created, e.g. for reusing the same header on multiple pages

- The template defines blocks where content will go
```
{% block content %}
{% endblock %}
```

- To inherit the template, `{% extends "base.html" %}` goes at the start of the body, and then the same block tags wrap the necessary content