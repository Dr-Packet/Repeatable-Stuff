import os
import sys

scriptDir = sys.path[0]

ITEMS = os.path.join(scriptDir, 'ITEMS.txt')
ITEMSFile = open(ITEMS, "r")
ITEMSlines = ITEMSFile.readlines()
