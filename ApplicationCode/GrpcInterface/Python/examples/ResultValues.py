import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '../api'))
import ResInsight

resInsight     = ResInsight.Instance.find()
#gridCount      = resInsight.gridInfo.getGridCount(caseId=0)
#gridDimensions = resInsight.gridInfo.getAllGridDimensions(caseId=0)

poroChunks = resInsight.properties.activeCellResults(0, 'STATIC_NATIVE', 'PORO', 0)
poroResults = []
for poroChunk in poroChunks:
    for poro in poroChunk.values:
        poroResults.append(poro)

permxChunks = resInsight.properties.activeCellResults(0, 'STATIC_NATIVE', 'PERMX', 0)
permxResults = []
for permxChunk in permxChunks:
    for permx in permxChunk.values:
        permxResults.append(permx)

results = []
for (poro, permx) in zip(poroResults, permxResults):
    results.append(poro * permx)

print("Transferred " + str(len(results)) + " cell results")
print("30th active cell: ")
print(results[29])