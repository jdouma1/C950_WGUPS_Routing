# Vertex class used to map delivery route on graph
class Vertex:
    # Vertices begin with a distance of infinity and no predecessor vertices
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.predecessor = None