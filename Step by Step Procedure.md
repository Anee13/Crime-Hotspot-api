# step by step procedure

1.	First, you need to run the ‘ crime-analysis.ipynb’ file to ensure that it contains the code you want to use in your FastAPI application. The notebook file can be opened using Jupyter Notebook or JupyterLab. Once you're ready, run the notebook to generate the output.
2.	Next, you need to convert the “crime-analysis.ipynb” file into a Python module that can be imported into your FastAPI application. You can do this using the “nbconvert “command in your terminal or command prompt. The command you need to run is:

               jupyter nbconvert --to python crime-analysis.ipynb

This will create a new file named “crime-analysis.py” in the same directory as the notebook file.
3.	Finally, you can run the “main.py” file to start your FastAPI application. This file contains the code that creates your API endpoints and imports the “crime-analysis.py” module. Once your application is running, you can use the API to perform crime hotspot visualization mapping and prediction.
4.	You can run the “main.py” file using the python command in your terminal or command prompt. The command you need to run is:

                                                              python main.py

5.	Once your application is running, you can access the interactive API documentation by visiting http://localhost:8000/docs in your web browser.

