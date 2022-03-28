# Fundamentals
```py
#Consider this as a py file
from flask import Flask
app = Flask(__name__)#Instance Flask

@app.route('/path_of_your_choose')#Here we are using a decorator do specify what we will load on the specified path its something like "localhost/path_of_your_choose"
def func():
	return 'something'
```

### Pass things on url(dynamic Route)
```py
from flask import Flask
app = Flask(__name__)
@app.route("/about-<username>")
def about(username)
	return f'About this username "{username}"'
```
