double-click Jupyter Notebook.exe

a browser window will open to your Jupyter Notebook Dashboard

to open a Notebook from a Github repository, click 'Upload'
> navigate to your Github repository, select >> upload the notebook > work on it and save it



To get your Jupyter Notebook.exe to open up your GitHub repositories....
change directory in Spyder>settings>.jupyter>jupyter_notebook_config.py
>>
# The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = u'C:/Users/atm19/Documents/GitHub' <<<<CHANGE PATH HERE