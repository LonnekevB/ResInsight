import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '../api'))
import ResInsight

def createResult(poroChunks, permxChunks):
    for (poroChunk, permxChunk) in zip(poroChunks, permxChunks):
        resultChunk = []
        for (poro, permx) in zip(poroChunk.values, permxChunk.values):
            resultChunk.append(poro * permx)
        yield resultChunk



resInsight     = ResInsight.Instance.find()

poroChunks = resInsight.properties.activeCellResults(0, 'STATIC_NATIVE', 'PORO', 0)
permxChunks = resInsight.properties.activeCellResults(0, 'STATIC_NATIVE', 'PERMX', 0)

resInsight.properties.setActiveCellResultsAsync(createResult(poroChunks, permxChunks), 0, 'GENERATED', 'POROPERMXAS', 0)

print("Transferred all results back")