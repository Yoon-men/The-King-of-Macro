import PySide2.QtGui
from PySide2.QtWidgets import QListWidget
from PySide2.QtCore import Signal


class ItemListWidget(QListWidget) : 
    itemMoved = Signal()

    def dropEvent(self, event) -> None:
        super().dropEvent(event)
        self.itemMoved.emit()