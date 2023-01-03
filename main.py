class Edge:
    def __init__(self, target, cost):
        self.cost = cost
        self.target = target
    
    def GetCost(self):
        return self.cost

    def GetTarget(self):
        return self.target

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.adjacent = None
        self.costIncrement = 0

    def GetName(self):
        return self.name

    def GetHeuristic(self):
        return self.heuristic

    def GetTotalCost(self):
        return self.costIncrement + self.heuristic

    def GetCostIncrement(self):
        return self.costIncrement

    def GetAdjacent(self):
        return self.adjacent

    def GetListAdjacent(self):
        return self.listAdjacent


    def SetAdjacent(self, adjacent):
        self.adjacent = adjacent

    def SetListAdjacent(self, adjacent):
        self.listAdjacent = adjacent


    def SetCostIncrement(self, constIncrement):
        self.costIncrement = constIncrement

def FindLowestTotalCost(priority):
    lowest = 0
    for index in range(0, len(priority)):
        if priority[lowest].GetTotalCost() > priority[index].GetTotalCost():
            lowest = index
    return priority.pop(lowest)

def theStar(origin, destiny):
    explorer = []
    priority = []
    if origin.GetName() != destiny.GetName():
        origin.SetCostIncrement(0)
        priority.append(origin)
        
        destinyFind = False

        while len(priority) > 0 and not(destinyFind):
            current = FindLowestTotalCost(priority)
            explorer.append(current)
            
            if current.GetName() == destiny.GetName():
                destinyFind = True
            else:
                for edge in current.GetListAdjacent():
                    child = edge.GetTarget()
                    costIncrement = current.GetCostIncrement() + edge.GetCost()
                    TotalCost = costIncrement + child.GetHeuristic()

                    if child in explorer and TotalCost > current.GetTotalCost():
                        continue
                    elif (child not in priority) or (child.GetTotalCost() > TotalCost):
                         child.SetAdjacent(current)
                         child.SetCostIncrement(costIncrement)
                         if child not in priority:
                            priority.append(child)

def Travel(target):
    path = "]"
    while not(target is None):
        path = ', ' + target.GetName() + path
        target = target.GetAdjacent()
    path = "[" + path[2:]
    return path

arad = Node("Arad",366) 
bucharest = Node("Bucharest",0) 
craiova = Node("Craiova",160) 
eforie= Node("Eforie",161) 
fagaras= Node("Fagaras",178) 
giurgiu = Node("Giurgiu", 77) 
zerind = Node("Zerind", 374) 
oradea = Node("Oradea", 380) 
sibiu = Node("Sibiu", 253) 
rimnicu = Node("Rimnicu Vilcea", 193) 
pitesti = Node("Pitesti", 98) 
timisoara = Node("Timisoara", 329) 
lugoj = Node("Lugoj", 244) 
mehadia = Node("Mehadia", 241) 
drobeta = Node("Drobeta", 242)

arad.SetListAdjacent([Edge(zerind,75),Edge(sibiu,140),Edge(timisoara,118)])
zerind.SetListAdjacent([Edge(arad,75),Edge(oradea,71)]) 
oradea.SetListAdjacent([Edge(zerind,71),Edge(sibiu,151)]) 
sibiu.SetListAdjacent([Edge(arad,140),Edge(fagaras,99),Edge(oradea,151),Edge(rimnicu,80)]) 
fagaras.SetListAdjacent([Edge(sibiu,99),Edge(bucharest,211)]) 
rimnicu.SetListAdjacent([Edge(sibiu,80),Edge(pitesti,97),Edge(craiova,146)]) 
pitesti.SetListAdjacent([Edge(rimnicu,97),Edge(bucharest,101),Edge(craiova,138)]) 
timisoara.SetListAdjacent([Edge(arad,118),Edge(lugoj,111)]) 
lugoj.SetListAdjacent([Edge(timisoara,111),Edge(mehadia,70)]) 
mehadia.SetListAdjacent([Edge(lugoj,70),Edge(drobeta,75)]) 
drobeta.SetListAdjacent([Edge(mehadia,75),Edge(craiova,120)]) 
craiova.SetListAdjacent([Edge(drobeta,120),Edge(rimnicu,146),Edge(pitesti,138)]) 
bucharest.SetListAdjacent([Edge(pitesti,101),Edge(giurgiu,90),Edge(fagaras,211)])

theStar(arad, bucharest)
print(Travel(bucharest))