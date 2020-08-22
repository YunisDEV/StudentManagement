There is dependencies in this application. So you will need to create a virtual environment to install dependencies. Follow commands below:
```bash
> virtualenv stmng
#for windows
> \stmng\Scripts\activate
#for linux
> source ./stmng/bin/activate

#for install dependencies
(stmng) > pip install -r requirements.txt

#to start app
(stmng) > python3 main.py
```