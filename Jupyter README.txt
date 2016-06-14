double-click Jupyter Notebook.exe

a browser window will open to your Jupyter Notebook Dashboard

to open a Notebook from a Github repository, click 'Upload'
> navigate to your Github repository, select >> upload the notebook > work on it and save it



To get your Jupyter Notebook.exe to open up your GitHub repositories....
change directory in Spyder>settings>.jupyter>jupyter_notebook_config.py
>>
# The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = u'C:/Users/atm19/Documents/GitHub' <<<<CHANGE PATH HERE


to add jupyter to your PATH envrionmental variable:
http://pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/

to add R kernel you have to run R from the WinPython Command Prompt!
Follow these instructions:
https://irkernel.github.io/installation/

install.packages(c('repr', 'pbdZMQ', 'devtools')) # repr is already on CRAN
devtools::install_github('IRkernel/IRdisplay')
devtools::install_github('IRkernel/IRkernel')
IRkernel::installspec()

