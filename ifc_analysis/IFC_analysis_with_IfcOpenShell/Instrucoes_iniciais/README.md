# Instruções para fazer o IFC Viewer funcionar no Jupyter NoteBook (sistema operacional Windows)

Isso o livrará de alguns problemas.

1 - Instale o Anaconda;

2 - Crie um novo ambiente no Anaconda:

- Abra o *Anaconda*;

- Vá para *ambientes*;

- Clique em *+ Criar*;

- Escolha um nome apropriado, como *ifc_viewer*.

Ainda no Anaconda, clique na seta à direita ao lado do nome do ambiente criado, acesse o menu e escolha *Abrir Terminal*.

Digite as seguintes linhas no terminal e pressione Enter.

```
conda install -c conda-forge ifcopenshell
```
```
conda install -c dlr-sc pythonocc-core
```
```
conda install -c conda-forge pythreejs
```

O arquivo IFC usado para este exercício foi o [IFCOpenHouse](https://github.com/aothms/IfcOpenHouse).

```
import ifcopenshell
import ifcopenshell.geom

# You must have an IFC valid file to Open
# I recommend you get a good one on IfcOpenHouse repository
# https://github.com/aothms/IfcOpenHouse
file = ifcopenshell.open(f"./IfcOpenHouse/IfcOpenHouse_IFC4.ifc")

settings = ifcopenshell.geom.settings()
settings.set(settings.USE_PYTHON_OPENCASCADE, True)
geometry = dict((file[item.data.id], (item.geometry, item.styles)) 
                for item in ifcopenshell.geom.iterator(settings, file))
       

from ifc_viewer import ifc_viewer
        
viewer = ifc_viewer()

for product, (shape, styles) in geometry.items():
    # if not product.is_a("IfcWall"): continue
    viewer.DisplayShape(product, shape, styles)
    
viewer.Display()
```

Visualizar o arquivo IFC no Jupyter Notebook usando o script abaixo (ou baixando o anexad [aqui](https://github.com/renatogcruz/Data-science-for-architecture/blob/main/ifc_analysis/IFC_analysis_with_IfcOpenShell/Instrucoes_iniciais/ifc_visualizer.ipynb)).

Para funcionar corretamente, você deve deixar os dois arquivos no mesmo diretório. 


[Fonte](https://gist.github.com/feromes/b9e7935b9313e7eb7e197d267168ebdb)
