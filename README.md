This project is juste a test to remind me what I have been doing during my internship.

As you might know it is pretty easy to forget knowledge when not used.
Hence here is the structure of a python project. 


# Using uv 
This shall be completed later (one day maybe)
The creation of the module can be done using : 
```
uv init -app NAME
```
it is possible to add a module to the project using 
```
uv add numpy 
```

Then it is possible to install the code on local machine using 
```
uv pip install -e .  
```

To reload and sync the venv (particularly when dependencies are used):
```
uv sync --reinstall
```

# Using git 
It is possible to use the versioning app gitlab or github
Here are the basic commands 
```
git init 
git clone myproject@gitlab.com
git checkout mybranch
git checkout .
git checkout -b newbranch
git pull origin develop
git add 
git commit -m "Commit message"
git push origin develop
git log
```

It is possible to connect your machine and github using an ssh key.
