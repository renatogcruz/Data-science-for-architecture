# Opening IFC file using Python, IfcOpenShell and Jupyter Notebook

1 - Import ifcopenshell library

```
import ifcopenshell
import ifcopenshell.geom
```

2 - Open the IFC file

```
file = ifcopenshell.open("file_name.ifc")
```

For everything to work properly, we need a valid IFC file. Keep all files in the same directory.

3 - Prepare the settings

```
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_PYTHON_OPENCASCADE, True)
geometry = dict((file[item.data.id], (item.geometry, item.styles)) 
                for item in ifcopenshell.geom.iterator(settings, file))
```

4 - Import ifc_viewer

```
from ifc_viewer import ifc_viewer
        
viewer = ifc_viewer()

for product, (shape, styles) in geometry.items():
    # if not product.is_a("IfcWall"): continue
    viewer.DisplayShape(product, shape, styles)
    
viewer.Display()
```

Download the files above and do it yourself.

Reference material [here](https://gist.github.com/feromes/b9e7935b9313e7eb7e197d267168ebdb)
