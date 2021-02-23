# IFC analysis

Repository on data analysis in Architecture, Engineering, Construction (AEC) and Urbanism

# Introdução

### IFC – Industry Foundation Class

- MeuProjeto.ifc: o arquivo IFC (formato de arquivo digital para exportar/importar informações de (ou o próprio) modelos BIM);
- Modelagem da informação da construção: o esquema de dados IFC;

### Product Data

- No meio da década de 80, foram percebidas as vantagens em se ter um esquema para organizar os dados e outro para a linguagem que carregaria os dados;
- Os modelos de produtos tendem a serem ricos e redundantes, para atender aos diferentes interesses dos profissionais que manipulam suas informações;

### Product Data: IFC

- Foi concebido como um “framework model” extensível;
- Deveria prover um amplo conjunto de definições gerais de objetos e dados a partir das quais modelos mais detalhados e específicos a determinadas tarefas poderiam ser definidos;
- Foi direcionado para abranger todas as informações da edificação, por todo o seu ciclo de vida, da análise de viabilidade e planejamento, ao projeto (incluindo análise e simulação), construção, ocupação e operação;

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
- A [linguagem EXPRESS](https://en.wikipedia.org/wiki/EXPRESS_(data_modeling_language) foi um dos principais resultados da ISO-STEP, desenvolvida por Douglas Schenck e posterior contribuição de Peter Wilson;

Exemplo simples de um modelo de dados EXPRESS simples: código e figura:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/EXPRESS-G_diagram_for_Family_schema.svg/1280px-EXPRESS-G_diagram_for_Family_schema.svg.png)
Fig. Um diagrama EXPRESS-G para o esquema Família ([fonte](https://en.wikipedia.org/wiki/EXPRESS_(data_modeling_language))).
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


