pip : command line tool for installing python packages, found on python pcakages. https://pypi.org

# pip version : open command prompt and run the command
pip --version

# this command writes a file with the currently installed libraries in teh project
pip freeze > requirements.txt

# upgrade pip version
python -m pip install --upgrade pip

# pip help
pip --help

# go to python shell
python

# to exit from python interpreter
exit()

# clear screen
cls

# know more about teh python pacvkage
pip search <package_name>


# install a library
pip install <library_name>

# installs it to teh current user python installation directory
python -m pip install --user requests
or
pip install --user requests

# know more about installed package_name
pip show <package_name>

# list out all the installed package_name
pip list

# uninstall any package_name
pip uninstall <package_name>

# pip packages using Pycharm IDE
go to settings > projectname :project_name > project interpreter > click on + > search by package name > click install


