# Instructions to getting IFC Viewer working on Jupyter NoteBook

1. You have to install previously [Anaconda](https://www.anaconda.com/distribution/) and I supposed you're under Windows OS, otherwise you had already IFC Viewer working :)
2. It's boring but will rid you from some trouble. You should create a new Environment on Anaconda
  * Open Anaconda
  * Go to `Environments`
  * Click on `+Create`
  * Choose an appropriate name, like `ifc_viewer`
3. Still on Anaconda, we're gonna go deeper. Click on arrow right to the name of the environment you just created, and you should access a menu, and then choose `Open Terminal`
4. You must be thrilled to see this beautiful black terminal. I always think I'm Neo in Matrix this time :) But you're here just to install 3 Python Libs that we need to make things working. And you're gonna type the following lines on terminal, hit enter and wait for the magic happens.

 ```conda install -c conda-forge ifcopenshell```
 
 ```conda install -c dlr-sc pythonocc-core```
 
 ```conda install -c conda-forge pythreejs```
 
 5. You should have an IFC file to see Jupyter NoteBook working, I recommend you download [IFCOpenHouse](https://github.com/aothms/IfcOpenHouse)
 6. Now, you have to be able to view IFC files on Jupyter Notebook, as the following file attached here in this Gist.
 7. In order to work properly you have to let the both file in the same directory.
 8. By default, when you start Jupyter Notebook on Anaconda, it uses your Home Folder. You should put all files in a folder there, including your IFC File or IFC OpenHouse. 
 9. Just start Jupyter Notebook, go to the folder you save the files and open `ifc_visualizer.ipynb` Pay attention to the Jupyter Notebook cell 2 command file path. It has to point to the correct location and find a valid IFC file.
 
 I hope this lines help you to get involved with programing.