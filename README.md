# hello world
## Description
This project is used for testing the different ways to make and manage a python package.
Currently, this package is made with the minimum folders and complications without cookie cutter.

## Notes
**FOLDER STRUCTURE**<br />
* The .gitignore was the default given when creating the repo on github, 
  I added to ignore pipfile, pipfile.lock, and .idea/
  
* Inside the root directory we can use a src folder to house different 
  packages if we wanted to, for this simple example I chose to only have one 
  package (i.e. helloworld), so a src folder was not necessary. The src directory
  also will force the pytest to use the recently installed package becasue in the
  test_helloworld.py the import will still be from helloworld import sayhello and
  not from src.helloworld import sayhello.
  
* The MANIFEST.in was automatically created using check-manifest in the root dir. 
  The MANIFEST.in is used to include certain files (ex: LICENSE.txt) into 
  the dist/ folder, which includes the files in the tar.gz file for distribution.
```bash
$ pip install check-manifest
$ check-manifest --create
```

* For developing the dist/, build/ folders can be created using the 
  below commands in the root dir. bdist_wheel will also add 
  the .whl file to the dist folder
  
```bash
$ python setup.py bdist_wheel sdist
```

* check the setup.py file, I left arguments commented out. we can specify 
  where the installation can find either our packages or modules.
  
**WORKFLOW**<br />
* my workflow would be to do a git clone of the remote repo, 
  then install the pipenv. then cd to the repo and run the follow command, 
  which will install the extras_require listed in the setup.py along with the
  install_requires. The -e will make sure the install is editable meaning
  any changes to the code but not the dependency packages will be reflected immediately
  for development. if dependencies are changed then re-run the command
  
```bash
(base) jeremy@Jeremy:~/Desktop/helloworld$ pipenv install
```

```bash
(base) jeremy@Jeremy:~/Desktop/helloworld$ pipenv shell
```
  
```bash
(helloworld) (base) jeremy@Jeremy:~/Desktop/helloworld$ pip install -e .[dev]
```

* The pip list will now point to the directory you are working in
```bash
(helloworld) (base) jeremy@Jeremy:~/Desktop/helloworld$ pip list
Package            Version             Location
------------------ ------------------- -------------------------------
attrs              20.3.0
helloworld         0.0.1               /home/jeremy/Desktop/helloworld
importlib-metadata 3.3.0

```

**TESTING**<br />
* The tests folder needed an init file in order for pytest to import helloworld. 
  other option would be to put a conftest.py (empty) in the root dir which will force pytest
  to add the root dir to the sys.path when running the tests.
  
* To test the code after installing the package inside the pipenv virtual envrionment,
run pytest in the package directory
  
```bash
(helloworld) (base) jeremy@Jeremy:~/Desktop/helloworld$ pytest -v
========================================================================================================== test session starts ===========================================================================================================
platform linux -- Python 3.7.9, pytest-6.2.1, py-1.10.0, pluggy-0.13.1 -- /home/jeremy/.local/share/virtualenvs/helloworld-iDqgLxeq/bin/python3.7
cachedir: .pytest_cache
rootdir: /home/jeremy/Desktop/helloworld
collected 2 items                                                                                                                                                                                                                        

tests/test_helloworld.py::test_helloworld_no_params PASSED                                                                                                                                                                         [ 50%]
tests/test_helloworld.py::test_helloworld_with_param PASSED                                                                                                                                                                        [100%]

=========================================================================================================== 2 passed in 0.02s ============================================================================================================
```
  

## Installation
**Deployment Install:**<br />
```bash
$ pip install git+https://github.com/jtap159/helloworld.git
```
or
```bash
$ pip install git+https://github.com/jtap159/helloworld.git
```

## Discussion
* check on using tox to test multiple versions of python on the code

* .travis.yml for testing on clean machines

**Badges**
* Code Coverage( Coveralls, codecov.io)

* Quality Metrics (Code Climate, Landscape.io)