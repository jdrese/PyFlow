from nine import str
from Qt import QtCore
from Qt import QtGui
from Qt.QtWidgets import QUndoView
from Qt.QtWidgets import QWidget
from Qt.QtWidgets import QVBoxLayout

from PyFlow.Packages.PyflowBase.Tools import RESOURCES_DIR
from PyFlow.UI.Tool.Tool import DockTool


class HistoryTool(DockTool):
    """docstring for History tool."""
    def __init__(self):
        super(HistoryTool, self).__init__()
        self.setMinimumSize(QtCore.QSize(200, 50))
        self.content = QWidget()
        self.content.setObjectName("historyToolContent")
        self.verticalLayout = QVBoxLayout(self.content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.undoStackView = QUndoView(self)
        self.undoStackView.setObjectName("undoStackView")
        self.verticalLayout.addWidget(self.undoStackView)
        self.setWidget(self.content)

    @staticmethod
    def getIcon():
        return QtGui.QIcon(RESOURCES_DIR + "/history.png")

    def onShow(self):
        super(HistoryTool, self).onShow()
        self.undoStackView.setStack(self.canvas.undoStack)

    @staticmethod
    def defaultDockArea():
        return QtCore.Qt.LeftDockWidgetArea

    @staticmethod
    def toolTip():
        return "Undo stack"

    @staticmethod
    def name():
        return str("History")
