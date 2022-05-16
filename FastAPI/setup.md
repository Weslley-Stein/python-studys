# Setup of Flask

### Required packages
```bash
#On Terminal
sudo pip install fastapi[all] 
sudo pip install fastapi
sudo pip install venv
```

### Config venv
```bash
#On Terminal
python3 -m venv /path/to/new/virtual/environment
source venv/bin/activate
```

### Setup on code:
```py
#On py file
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()
```

### Running the code
```bash
#On Terminal
uvircorn py_file:instance_name --reload
```
