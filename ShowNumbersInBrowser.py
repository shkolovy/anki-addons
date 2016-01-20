from aqt.browser import Browser
from aqt.browser import DataModel

baseSetupColumns = Browser.setupColumns
baseColumnData = DataModel.columnData

def customSetupColumns(self):
	baseSetupColumns(self)
	self.columns.append(('number', _("#")))
	
def customColumnData(self, index):
	type = self.columnType(index.column())
	if type == "number":
		n = self.cards.index(self.cards[index.row()]) + 1
		return "%d" % (n)
	else:
		return baseColumnData(self, index)
	
DataModel.columnData = customColumnData
Browser.setupColumns = customSetupColumns