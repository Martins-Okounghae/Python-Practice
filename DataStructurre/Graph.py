# A dictionary with graph elements

# Vertices = {a,b,c,d,e}

# Edges = {ab, ac, bd, cd, de}

graph = {"a": ["b","c"],
         "b": ["a","d"],
         "c": ["a", "d"],
         "d": ["c", "e"],
         "e": ["d"]
}


print(graph)



# Display graph vertices

class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = []
        self.gdict = gdict


#Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())


#Create the distionary with graph elements
graph_elements = {"a": ["b","c"],
                  "b": ["a","d"],
                  "c": ["a","d"],
                  "d": ["c","e"],
                  "e": ["d"]
}

g = Graph(graph_elements)

print(g.getVertices())
