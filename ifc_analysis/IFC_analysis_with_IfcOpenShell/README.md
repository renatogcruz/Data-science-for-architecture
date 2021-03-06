# IFC analysis with IfcOpenShell

IfcOpenShell is an open source software library for working with the Industry Foundation Classes (IFC) file format. Currently supported IFC releases are IFC2x3 TC1 and IFC4 Add2 TC1.

For more information, see

- http://ifcopenshell.org

- http://academy.ifcopenshell.org

## Instructions for installing IfcOpenShell to work with IFC files using Python and Jupyter NoteBook 

Windows OS

1 - Install [Anaconda](https://docs.anaconda.com/anaconda/install/)

2 - Access Anaconda command prompt.

2.1 - Click Start, search, or select Anaconda Prompt from the menu

2.2 - Type the following line in the terminal and press Enter.

```
conda install -c conda-forge -c oce -c dlr-sc -c ifcopenshell ifcopenshell
```

```
conda install -c dlr-sc pythonocc-core
```

```
conda install -c conda-forge pythreejs
```

Wait for the installation to finish.

## What do we find here?

Initial instructions for opening an IFC file using Python, IfcOpenShell and Jupyter NoteBook

1 - [Initial instructions - View IFC file on Jupyter Notebook using Python](https://github.com/renatogcruz/Data-science-for-architecture/tree/main/ifc_analysis/IFC_analysis_with_IfcOpenShell/Instrucoes_iniciais)

2 - [Introduction_to_Python_for_use_with_BIM](https://github.com/renatogcruz/Data-science-for-architecture/tree/main/ifc_analysis/IFC_analysis_with_IfcOpenShell/02_Introduction_to_Python_for_use_with_BIM)

3 - [Basics with ifcopenshell notebook](https://github.com/renatogcruz/Data-science-for-architecture/tree/main/ifc_analysis/IFC_analysis_with_IfcOpenShell/03_Basics_with_ifcopenshell_notebook)

4 - [Basics Project](https://github.com/renatogcruz/Data-science-for-architecture/tree/main/ifc_analysis/IFC_analysis_with_IfcOpenShell/04_Basics_Project)

5 - [Get list of room names and descriptions](https://github.com/renatogcruz/Data-science-for-architecture/tree/main/ifc_analysis/IFC_analysis_with_IfcOpenShell/05_Get_list_of_room_names_and_descriptions)

6 - [Redefining an IfcBuildingElementProxy to IfcWall](https://github.com/renatogcruz/Data-science-for-architecture/tree/main/ifc_analysis/IFC_analysis_with_IfcOpenShell/06_Redefining_an_IfcBuildingElementProxy_to_IfcWall)

## Reference materials

Material for a basic [course](https://github.com/bimfag/intro-python-bim) in python for use with BIM

[Análise de IFC utilizando Python e IfcOpenShell](https://www.youtube.com/watch?v=fKIuYu0-hVk)

[BIM Notebooks](https://github.com/c4rlosdias/BIM-Notebooks)

[Instructions to getting IFC Viewer working on Jupyter NoteBook](https://gist.github.com/feromes/b9e7935b9313e7eb7e197d267168ebdb)

[Scripts and tools for analyzing ifc with ifcopenshell and python-occ](https://github.com/johannesmichael/ifc-python)
