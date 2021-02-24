import ifcopenshell
import json
import math

file = ifcopenshell.open("C:\\Users\\admin\\OneDrive\\WorkInProgress\\FAPESP\\AduelasConstrutora.IFC")

output = open('Processamento_IFC.txt','w')

#1 Data - Identidade do Empreendimento
projeto = file.by_type('IfcProject')
output.write("Identidade do Empreendimento:"+projeto[0].Name+'\n')

#2 Data - Identificação do Local
sitio = file.by_type('IfcSite')
output.write("Identificação do Local:"+sitio[0].Name+'\n')

#3 Data - Endereço de entrega
endereco = sitio[0].SiteAddress
output.write("Endereço de entrega:")
for i in endereco.AddressLines:
    output.write(i+'\n')
output.write("Cidade:"+endereco.Town+'\n')
output.write("Estado:"+endereco.Region+'\n')
output.write("CEP:"+endereco.PostalCode+'\n')
output.write("País:"+endereco.Country+'\n')

#4 Data - Identificação da Torre
edificio = file.by_type('IfcBuilding')
output.write("Identificação da torre:"+edificio[0].Name+'\n')

#5 Data - Pedido (IfcProjectOrder)
# IfcWorkPlan
plan = []
planejamentos = file.by_type('IfcRelDeclares')
for i in planejamentos:
    if i.RelatingContext.is_a().find('IfcProject') != -1:
        for j in i.RelatedDefinitions:
            if j.is_a().find('IfcWorkPlan') != -1:
                plan.append(j)

# IfcProjectOrder
controles = file.by_type('IfcRelAssignsToControl')
tarefas_aninhadas = file.by_type('IfcRelNests')
sch = file.by_type('IfcRelAggregates')
tipos = file.by_type('IfcRelDefinesByType')
propriedades = file.by_type('IfcRelDefinesByProperties')
material = file.by_type('IfcRelAssociatesMaterial')
ordens = []
pedidos = {}
relatedtasks = {}
summary_tasks = {}
relatedschedules = {}
for i in controles:
    for id,j in enumerate(plan):
        # Encontrando IfcProjectOrder associado ao IfcWorkPlan
        if i.RelatingControl.id() == j.id():
            #output.write("WorkPlan número "+str(id+1)+": "+str(j.id())+'\n')
            for k in i.RelatedObjects:
                if k.is_a().find('IfcProjectOrder') != -1:
                    output.write("Pedido: "+str(k.id())+'\n')
                    pedidos[str(k.id())] = j.id()
                    #output.write(json.dumps(pedidos)+'\n')
                    for x in sch:
                        if x.RelatingObject.id() == k.id():
                            for indice,y in enumerate(x.RelatedObjects):
                                if y.is_a().find('IfcWorkSchedule') != -1:
                                    #output.write("Workschedule numero "+str(indice+1)+": "+str(y.id())+'\n')
                                    relatedschedules[str(y.id())]=k.id()                                    
        # Encontrando IfcTasks associadas ao IfcWorkSchedule
        if i.RelatingControl.is_a().find('IfcWorkSchedule') != -1:
            for t in i.RelatedObjects:
                if t.is_a().find('IfcTask') != -1:
                    if not (str(t.id()) in summary_tasks):
                        summary_tasks[str(t.id())]=i.RelatingControl.id()
                        #output.write(json.dumps(summary_tasks)+'\n')
                        for u in tarefas_aninhadas:
                            if u.RelatingObject.id() == t.id():
                                for v in u.RelatedObjects:
                                    relatedtasks[str(v.id())]=t.id()                                    

# RebarCage and IfcTask
processos = file.by_type('IfcRelAssignsToProcess')
tasks = []
associated_rebarcages = {}
for i in processos:
    if str(i.RelatingProcess.id()) in relatedtasks:
        for j in i.RelatedObjects:
            if j.is_a().find('IfcElementAssembly') != -1:
                associated_rebarcages[str(j.id())] = i.RelatingProcess.id()                

# RebarCage and Rebars
rebarcages = []
associated_rebars = {}
for i in sch:
    if i.RelatingObject.is_a().find('IfcElementAssembly') != -1:
        for j in i.RelatedObjects:
            if j.is_a().find('IfcReinforcingBar') != -1:
                associated_rebars[str(j.id())]=i.RelatingObject.id()
# Agentes
agentes = file.by_type('IfcRelAssignsToActor')
organizacoes = []
associated_orders = []
for i in agentes:
 associated_orders.append(i.RelatedObjects)
 organizacoes.append(i.RelatingActor.TheActor.TheOrganization)
 
#for indice,(i,k) in enumerate(zip(pedidos,relatedtasks)):
 #output.write("No. do pedido:"+i.Identification+'\n')
 #output.write("No. do pedido:"+i.Description+'\n')
 
 for index,j in enumerate(associated_orders):
  for h in j:
   if h.id() == i.id():
    output.write("Fabricante:"+organizacoes[index].Name+'\n')

 for index,(j,m) in enumerate(zip(tasks,associated_rebarcages)):
  if j.id() == k.id():
   output.write("RebarCage n#:"+m.Name+'\n')

#desenho = file.by_type('IfcDocumentInformation')
referencia = file.by_type('IfcRelAssociatesDocument')

for key, value in associated_rebarcages.items():
    rebars_in_cage = [i for i,j in associated_rebars.items() if j == int(key)]
    for b in referencia:
        lista = b.RelatedObjects
        for c in lista:
            if c.id() == int(key):
                desenho = b.RelatingDocument 
    
    for a in rebars_in_cage:
        #output.write('Rebar: '+file.by_id(int(a)).Name+'\n')
        #output.write(a+'\n')
        quant = {}
        peso = {}
        mat = {}        
        for w in propriedades:
            if w.RelatingPropertyDefinition.is_a().find('IfcElementQuantity') != -1:
                for u in w.RelatedObjects:
                    if u.id() == int(a):
                        for v in w.RelatingPropertyDefinition.Quantities:
                            if v.is_a().find('IfcQuantityCount') != -1:
                                quant[str(u.id())] = v.CountValue
                            elif v.is_a().find('IfcQuantityWeight') != -1:
                                peso[str(u.id())] = v.WeightValue
        for k in tipos:
            for l in k.RelatedObjects:
                if l.id() == int(a):                    
                    if ( a in quant ) and ( a in peso ):
                        output.write('BVBS: BF2D@Hj'+projeto[0].Name+'@r'+desenho.Name+'@i'+desenho.Revision+'@p'+file.by_id(int(a)).Name+'@l'+str(k.RelatingType.BarLength)+'@n'+str(quant[a])+'@d'+str(peso[a])+'@e'+str(k.RelatingType.NominalDiameter))
                    else:
                        output.write('BVBS: BF2D@Hj'+projeto[0].Name+'@r'+desenho.Name+'@i'+desenho.Revision+'@p'+file.by_id(int(a)).Name+'@l'+str(k.RelatingType.BarLength)+'@e'+str(k.RelatingType.NominalDiameter))
                    for m in material:
                        for mtl in m.RelatedObjects:
                            if mtl.id() == k.RelatingType.id():
                                output.write('@g'+m.RelatingMaterial.Name)
                    # Geometry for IfcPolyLine
                    # Apenas uma representação por tipo
                    polyline = k.RelatingType.RepresentationMaps[0].MappedRepresentation.Items[0].Directrix
                    angle0 = 0
                    for h,hi in enumerate(polyline.Points):
                        if h != 0:
                            anterior = polyline.Points[h-1]
                            #output.write('Pontos: ('+str(anterior.Coordinates[0])+','+str(anterior.Coordinates[1])+','+str(anterior.Coordinates[2])+')\n')
                            valor = math.sqrt(pow(hi.Coordinates[0]-anterior.Coordinates[0],2)+pow(hi.Coordinates[1]-anterior.Coordinates[1],2))
                            
                            if h == 1:
                                #flag = 1
                                output.write('@Gl'+str(valor))
                            else:
                                anterior2 = polyline.Points[h-2]
                                angle = math.atan2(anterior.Coordinates[1]-anterior2.Coordinates[1],anterior.Coordinates[0]-anterior2.Coordinates[0])
                                angle = angle*180/math.pi
                                output.write('@w'+str(angle-angle0))
                                output.write('@Gl'+str(valor))
                                angle0 = angle
                            #anterior = hi
                    h = len(polyline.Points)
                    if angle0 == 0:
                        output.write('@w0\n')
                    else:
                        anterior2 = polyline.Points[h-2]
                        anterior = polyline.Points[h-1]
                        angle = math.atan2(anterior.Coordinates[1]-anterior2.Coordinates[1],anterior.Coordinates[0]-anterior2.Coordinates[0])
                        angle = angle*180/math.pi
                        output.write('@w'+str(angle-angle0)+'\n')
                    # Geometry for IfcIndexedPolyCurve
                    #output.write("Tipo: "+str(k.RelatingType.NominalDiameter)+'\n')
   
#output.write('Working Schedules associados ao IfcProjectOrder: '+json.dumps(relatedschedules)+'\n')
#output.write('Tarefas aninhadas à Summary Task: '+json.dumps(relatedtasks)+'\n')
#output.write('Rebar Cage: '+json.dumps(associated_rebarcages)+'\n')
#output.write("Rebars: "+json.dumps(associated_rebars)+'\n')
output.close()
