import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import rips

import dataroot

def test_Launch(rips_instance, initializeTest):
    assert(rips_instance is not None)

def test_EmptyProject(rips_instance, initializeTest):
    cases = rips_instance.project.cases()
    assert(len(cases) is 0)

def test_OneCase(rips_instance, initializeTest):
    case = rips_instance.project.loadCase(dataroot.PATH + "/TEST10K_FLT_LGR_NNC/TEST10K_FLT_LGR_NNC.EGRID")
    assert(case.name == "TEST10K_FLT_LGR_NNC")
    assert(case.id == 0)
    cases = rips_instance.project.cases()
    assert(len(cases) is 1)

def test_MultipleCases(rips_instance, initializeTest):
    casePaths = []
    casePaths.append(dataroot.PATH + "/TEST10K_FLT_LGR_NNC/TEST10K_FLT_LGR_NNC.EGRID")
    casePaths.append(dataroot.PATH + "/Case_with_10_timesteps/Real0/BRUGGE_0000.EGRID")
    casePaths.append(dataroot.PATH + "/Case_with_10_timesteps/Real30/BRUGGE_0030.EGRID")

    caseNames = []
    for casePath in casePaths:
        caseName = os.path.splitext(os.path.basename(casePath))[0]
        caseNames.append(caseName)
        rips_instance.project.loadCase(path=casePath)

    cases = rips_instance.project.cases()
    assert(len(cases) == len(caseNames))
    for i, caseName in enumerate(caseNames):
        assert(caseName == cases[i].name)

def test_10k(rips_instance, initializeTest):
    casePath = dataroot.PATH + "/TEST10K_FLT_LGR_NNC/TEST10K_FLT_LGR_NNC.EGRID"
    case = rips_instance.project.loadCase(path=casePath)
    assert(case.gridCount() == 2)
    cellCountInfo = case.cellCount()
    assert(cellCountInfo.active_cell_count == 11125)
    assert(cellCountInfo.reservoir_cell_count == 316224)
    timeSteps = case.timeSteps()
    assert(len(timeSteps.dates) == 9)

def test_brugge_0010(rips_instance, initializeTest):
    casePath = dataroot.PATH + "/Case_with_10_timesteps/Real10/BRUGGE_0010.EGRID"
    case = rips_instance.project.loadCase(path=casePath)
    assert(case.gridCount() == 1)
    cellCountInfo = case.cellCount()
    assert(cellCountInfo.active_cell_count == 43374)
    assert(cellCountInfo.reservoir_cell_count == 60048)
    timeSteps = case.timeSteps()
    assert(len(timeSteps.dates) == 11)