class GenomeStats:
    def __init__(self):
        self.stats = [[0,0,0,0,0,0]]
    
    def updateGenomeLoc (loc,ch):
        assert(loc<len(self.stats))
        stats[loc][getDNAValue(ch)]+=1

    def update (g, threadStats, i):
        for j in range(6):
            self.stats[g][j] += threadStats.stats[i][j]

    def max_pos(self,i):
        maxVal = -1
        pos = -1
        for j in range(1,6):
            if self.stats[i][j] > max_val:
                maxVal = self.stats[i][j]

        return pos

    def size(self):
        return len(self.stats)


class GenomeStatsSSE:
    def __init__(self):
        self.statsSSE = []
        self.getSSEvalueCache = []
        self.invert = 0

def updateGenomeLoc (loc,ch):
    assert(loc<len(self.statsSSE))
    self.statsSSE[loc] = statsSSE[loc] + getSSEValueCache[getDNAValue(ch)]

def update (g, threadStats, i):
    self.statsSSE[g] = self.statsSSE[g] + threadStats.get()

def max_pos(self,i):
    maxVal = -1
    pos = -1
    for j in range(1,6):
        if self.stats[i][j] > max_val:
            maxVal = self.stats[i][j]

    return pos

def size(self):
    return len(self.stats)

class SequenceCompressor:
    def __init__():
        self.reference = None
        self.fixesLoc = []
        self.fixesReplace = []
        self.fixesLocSt = []
        self.chromosome = ""
        self.fixed = ""
        self.fixedStart = 0
        self.fixedEnd = 0
        self.maxEnd = 0

    def getIndexData(out):
        out.clear()

    def getChromosome():
        return self.chromosome

    def getReference():
        return self.reference

class SequenceDecompressor:
    def __init__():
        self.reference = None
        self.chromosome = ""
        self.fixed = ""
        self.fixedStart = 0
        self.fixedEnd = 0


    def getChromosome():
        return self.chromosome

    def getReference():
        return self.reference
