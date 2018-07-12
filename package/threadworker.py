from PyQt4 import QtCore


class WorkerSignals(QtCore.QObject):
    # Defines signals available from running workers
    int_passback = QtCore.pyqtSignal(int)
    str_passback = QtCore.pyqtSignal(str)
    obj_passback = QtCore.pyqtSignal(object, object)


class Worker(QtCore.QRunnable):
    # Generic thread class

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs["cb_int_passback"] = self.signals.int_passback
        self.kwargs["cb_str_passback"] = self.signals.str_passback
        self.kwargs["cb_obj_passback"] = self.signals.obj_passback

    @QtCore.pyqtSlot()
    def run(self):
        # Executes functions passed in
        self.fn(*self.args, **self.kwargs)
