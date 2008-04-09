# coding: utf-8

"""
outputs the children of nodes that can appear more than once
e.g. "* foo bar" but not "? foo bar"
this is helpful in ensuring all plural names are not accidentially used
	for children than can appear more than once
"""

import os
import xml.dom.minidom as DOM

desalBase = "/media/files/Desal"
inputPath = os.path.join(desalBase,"nodes.xml")

def selectAll(node, selector) :
	return node.getElementsByTagName(selector)

def selectFirst(node, selector) :
	return selectAll(node, selector)[0]

def textVal(node) :
	return node.firstChild.nodeValue.strip()

doc = DOM.parse(inputPath)

for child in selectAll(doc,"child") :
	count = textVal(selectFirst(child,"count"))
	if len(selectAll(child, "spec-name")) == 0 :
		continue
	specName = textVal(selectFirst(child,"spec-name"))
	if count in ["*", "+"] :
		print '"%s" in "%s"' % (
			specName,
			textVal(selectFirst(child.parentNode,"spec-type"))
		)
