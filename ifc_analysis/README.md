# IFC analysis

Repository on data analysis in Architecture, Engineering, Construction (AEC) and Urbanism

# Introdução

### IFC – Industry Foundation Class

IFC (Industry Foundation Classes) é um esquema de dados abertos e um conjunto de formatos usados para armazenar dados [OpenBIM](https://wiki.osarch.org/index.php?title=OpenBIM).

Quando se fala em arquivo IFC:

- MeuProjeto.ifc: o arquivo IFC (formato de arquivo digital para exportar/importar informações de (ou o próprio) modelos BIM);
- Modelagem da informação da construção: o esquema de dados IFC;

Os dados IFC podem descrever digitalmente muitos conceitos, incluindo:

- Objetos físicos em nosso ambiente construído (paredes, lajes, colunas, tubos)
- Geometria 2D e 3D que representa objetos ou anota objetos
- Um conjunto diversificado de propriedades e atributos que abrangem muitos domínios
- Atributos de materiais e cores de exibição
- Planejamento de construção, alocação de recursos e programação
- Quantificação de elementos
- Funções e responsabilidades de organizações e indivíduos
- Estratégias de design e restrições legais
- Modelos analíticos para análise estrutural, análise de energia e análise de luz

### Versões

Atualmente, há duas versões comumente suportadas de IFC: 

- IFC2x3 - padrão ISO desde 2005
- IFC4   - padrão ISO desde 2013

IFC4 contém novos recursos,porém , é menos proeminente do que IFC2x3. 

### PFormatos

- .ifc Formato IFC-SPF, um formato de texto simples comumente usado com base no STEP
- .ifczipFormato IfcZIP, onde um único .ifcarquivo é compactado em um pacote ZIP
- .ifcxml Formato IfcXML, um formato de texto simples
- .json Formato JSON, um formato de texto simples
- .hdf Formato HDF5, um formato binário
- .sqlite Formato SQLite, um formato binário


### Interoperabilidade

*“... é a capacidade de trocar dados entre aplicações, de modo a suavizar o fluxo de trabalho e algumas vezes facilitar sua automação”* – BIM Handbook, 2011.

- Tipos de troca de dados: 
- 
Atalhos diretos;

Formato proprietário de troca;

Formato público de modelo de dados do produto;

- Trocas norteadas por fluxos de trabalho:

Vários grupos de profissionais, com habilidades e interesses distintos,
usando diferentes softwares;

### ISO-STEP e EXPRESS

- STEP (STandard for the Exchange of Product Model Data): ISO-10303;
- A [linguagem EXPRESS](https://en.wikipedia.org/wiki/EXPRESS_(data_modeling_language)) foi um dos principais resultados da ISO-STEP, desenvolvida por Douglas Schenck e posterior contribuição de Peter Wilson;

*Exemplo simples de um modelo de dados EXPRESS simples: código e figura:*

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/EXPRESS-G_diagram_for_Family_schema.svg/1280px-EXPRESS-G_diagram_for_Family_schema.svg.png)
*Fig. Um diagrama EXPRESS-G para o esquema Família ([fonte](https://en.wikipedia.org/wiki/EXPRESS_(data_modeling_language))).*
```
SCHEMA Family;

ENTITY Person
   ABSTRACT SUPERTYPE OF (ONEOF (Male, Female));
     name: STRING;
     mother: OPTIONAL Female;
     father: OPTIONAL Male;
END_ENTITY;

ENTITY Female
   SUBTYPE OF (Person);
END_ENTITY;

ENTITY Male
   SUBTYPE of (Person);
END_ENTITY;

END_SCHEMA;

```

- Tornou-se o mecanismo central de suporte à modelagem de produtos entre um grande número de indústrias: sistemas mecânicos e elétricos, plantas de processos, construção de navios, planos de processos, mobiliário, modelos de elementos finitos, edifícios e pontes;

- Usar as bibliotecas compartilhadas de Recursos (shared libraries Resources);

### Classes

Exemplos de classes de IFC são IfcWall, IfcBuildinge IfcTask. 

As classes podem ter atributos (ex.: IfcWall podem ter um Nameatributo). As classes também podem estar relacionadas com outras classes (ex.: IfcWall pode ser relacionado a um IfcBuildingpor estar espacialmente contido em IfcBuilding).

![](https://wiki.osarch.org/images/3/31/Ifcwall.png)

*Um exemplo de hierarquia de classes IFC. (Fonte: [OSarch](https://wiki.osarch.org/index.php?title=Industry_Foundation_Classes_(IFC)))*

As classes podem herdar de outras classes, construindo uma hierarquia de classes. Se uma classe herda de outra classe, ela herda todos os seus atributos e relacionamentos. 

Por exemplo, a IfcProductclasse tem um Representationatributo, que pode armazenar geometria 3D que representa essa classe. Como a IfcWallclasse herda da IfcProductclasse, ela também possui um Representationatributo para armazenar geometria 3D. No entanto, a IfcPersonclasse não herda da IfcProductclasse e, portanto, não tem um Representationatributo.


Quando falamos sobre conceitos BIM, nos referimos a objetos como paredes, portas e janelas. Às vezes, nos referimos a elementos não-objeto, como edifícios, materiais e anotações. Também nos referimos a outros conceitos, como coordenadas, propriedades e geometria. Cada substantivo, elemento, objeto ou conceito distinto a que nos referimos é chamado de "classe" no IFC. O jargão "classe", em vez do termo mais amplamente compreensível "elemento" ou "conceito", vem da indústria de desenvolvimento de software.

Todos os dados digitais em IFC pertencem a uma classe IFC. Classes IFC podem ser divididos em duas categorias: 

- enraizada - herdam atributos de uma classe IFC chamada IfcRoot
- não-enraizada  - não herdam atributos de uma classe IFC chamada IfcRoot 

Essa IfcRootclasse é importante porque fornece os quatro atributos abaixo:

| Atributo      | Requerido   |    Descrição       |
|:-------------:|:-----------:|:------------------:|
| GlobalId    | Sim       |  Um identificador único do objeto, gerado por um computador        |
|OwnerHistory |           |  Este atributo especial pode armazenar nomes, datas, organizações, fornecedor de software e detalhes de contato das pessoas responsáveis por este objeto                |
|  Name       |           | Isso pode conter um texto curto que nomeia o objeto                |
| Description |           | Texto para descrever o objeto                 |

Todas as classes enraizadas são semanticamente significativas para os usuários finais e criadas especificamente para um projeto ou biblioteca. Exemplos incluem IfcProject, IfcBuildinge, IfcWall. Eles geralmente são anotados na documentação ou nomeados especificamente nas programações. Esses objetos são geralmente úteis para usuários finais e, por esse motivo, podem ser rastreados com um GlobalIde dado a Name.

Em contraste, as classes não enraizadas não têm a capacidade de atribuir um GlobalId, Nameou de outra forma, e são usadas para armazenar dados não específicos do projeto, como coordenadas XYZ, valores de cores RGB, vetores e assim por diante. Eles são necessários de uma perspectiva técnica e geralmente são gerados automaticamente pela ferramenta de autoria BIM e geralmente podem ser ignorados com segurança pelos usuários finais. 

As classes são frequentemente descritas como o que herdam. Por exemplo, classes com raiz podem ser descritas como classes que herdam de IfcRoot, ou subclasses de IfcRoot. Se uma classe herda de outra classe ou é uma subclasse de outra classe, ela herda as mesmas habilidades dessa classe, como a habilidade de ter certos atributos, propriedades ou relacionamentos atribuídos a ela. As subclasses não herdam realmente os valores dos atributos em si, mas apenas a capacidade de ter esse atributo.

### Subclasses IfcRoot

As classes enraizadas podem ser subdivididas em três tipos de classes.

|Classe IFC | Descrição|
|:--------:|:----------:|
|IfcObjectDefinition | Descrevem "objetos" ou "coisas" que se relacionam com a indústria de AEC. Isso inclui paredes, pessoas e tarefas. Você pode considerá-los os "substantivos" na IFC.|
|IfcPropertyDefinition | descrevem propriedades de "objetos" e "coisas". Eles próprios não são um objeto, mas sim uma propriedade ou quantidade, como classificação de incêndio, uso de energia ou volume. |
|IfcRelationship |descrevem relacionamentos entre os próprios "objetos", entre propriedades ou entre objetos e propriedades. Os relacionamentos podem ser objetos que contêm outros objetos, se conectam a objetos, têm entradas ou saídas do sistema ou são atribuídos a uma propriedade ou quantidade. |


### Subclasses IfcObjectDefinition

Embora existam muitas subclasses de IFC, existem apenas algumas relevantes para diferentes autores de BIM e é útil fornecer um resumo delas. Embaixo dessas poucas subclasses que entram em mais detalhes, mas saber que essas categorizações amplas existem ajuda a compreender os dados da IFC. A tabela a seguir não é completa.

| Classes IFC         |   Descrição          |
|:---------:|:----------:|
|  IfcContext        |    Esta categoria especial contém o ponto de partida dos dados IFC, descrevendo um projeto ou biblioteca. Existem apenas duas subclasses: IfcProjecte IfcProjectLibrary         |
|  IfcElement        |  Eles contêm elementos físicos construídos que encontramos todos os dias, como lajes, colunas, vigas, móveis, canos, cabos, dutos e assim por diante. Exemplos de subclasses IfcElementincluem IfcColumn, IfcBeame IfcFurniture. Eles podem ter geometria associada a eles.           |
| IfcSpatialElement         | Descrevem conceitos espaciais, como locais, edifícios, pontes, andares e espaços. Essas IfcSpatialElementclasses podem conter IfcElementelementos dentro delas, como uma laje dentro de um andar de construção. Exemplos de subclasses IfcSpatialElementincluem IfcSite, IfcBuildinge IfcSpace.            |
| IfcElementType         | Descrevem os tipos de construção. Um tipo de construção pode ser atribuído a um IfcElement, assim como um tipo particular IfcWallpode ter um tipo particular de construção de 2 camadas de placa de gesso em uma estrutura de metal. Exemplos de subclasses IfcElementTypeincluem IfcWallType, IfcDoorTypee IfcWindowType.            |
|IfcStructuralActivity, IfcStructuralItem          | Eles são úteis para análise estrutural. Eles contêm dados para descrever um modelo analítico, incluindo membros, nós, conexões, cargas e forças, bem como os resultados dos cálculos. Exemplo subclasses incluem IfcStructuralCurveMember, IfcStructuralPointConnectione IfcStructuralPointReaction.            |
| IfcActor, IfcControl, IfcProcess,IfcResource         |  Eles são úteis para agendar informações, descrevendo responsabilidades, tarefas, recursos e cronogramas para o sequenciamento da construção ou planejamento do projeto. Exemplo subclasses incluem IfcTask, IfcConstructionMaterialResourcee IfcWorkSchedule.           |

### Subclasses IfcPropertyDefinition

A seguinte tabela descreve subclasses comuns usadas para descrever propriedades, que podem ser posteriormente atribuídas a objetos.



### Subclasses IfcRelationship


### Um resumo dos elementos não enraizados


https://wiki.osarch.org/index.php?title=IFC_classes


# Industry Foundation Classes (IFC)

https://biblus.accasoftware.com/en/ifc-file-structure-the-ifcobjectdefinition/

https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2_TC1/HTML/schema/ifcproductextension/lexical/ifcbuildingelement.htm

