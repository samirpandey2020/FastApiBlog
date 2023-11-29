# FastApiBlog

#installing pipenv
use: python 3.12
use where python to find path to the python


#command

```
    "python path to 3.12" -m pip install pipenv
    pipenv python "path to python 3.12" install
    pipenv shell
    pipenv install
```


#running the fastapi
```
    uvicorn app.main:app --reload
```


#dir structure
app
 -router
    -post
    -user
 -schemas
    -post
    -user
database
models
main
