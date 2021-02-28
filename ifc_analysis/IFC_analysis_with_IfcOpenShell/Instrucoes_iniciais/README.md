# Abrindo arquivo IFC utilizando Python, IfcOpenShell e Joypter Notebook

#### Primeiro passo

Importe a biblioteca ifcopenshell

```
import ifcopenshell
import ifcopenshell.geom
```

#### Segundo passo:

Abra o abrir o arquivo IFC.

Para que tudo funcione corretamente, precisamos de um arquivo IFC válido. Mantenha todos os arquivos no mesmo diretório.

```
file = ifcopenshell.open("Nome_do_aquivo.ifc")
```

#### Terceiro passo:

```
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_PYTHON_OPENCASCADE, True)
geometry = dict((file[item.data.id], (item.geometry, item.styles)) 
                for item in ifcopenshell.geom.iterator(settings, file))
```

#### Quarto passo:

Importe o ifc_viewwer

```
from ifc_viewer import ifc_viewer
        
viewer = ifc_viewer()

for product, (shape, styles) in geometry.items():
    # if not product.is_a("IfcWall"): continue
    viewer.DisplayShape(product, shape, styles)
    
viewer.Display()
```

[Baixe os arquivos](https://github.com/renatogcruz/Data-science-for-architecture/tree/main/ifc_analysis/IFC_analysis_with_IfcOpenShell/Instrucoes_iniciais) e faça você mesmo.

Material de referência [AQUI](https://gist.github.com/feromes/b9e7935b9313e7eb7e197d267168ebdb)
