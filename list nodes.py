"""
outputs a list of node typenames
"""

import os
import xml.dom.minidom as DOM
from lib import *

desalBase = "/media/files/Desal"
inputPath = os.path.join(desalBase,"nodes.xml")

def getTypename(elem) :
	typenameElem = filter(lambda x: x.tagName == "typename", childElements(elem))[0]
	return textValue(typenameElem).strip()

doc = DOM.parse(inputPath)
nodeTypenames = map(getTypename, childElements(doc.documentElement))
nodeTypenames.sort()
print "\n".join(nodeTypenames)