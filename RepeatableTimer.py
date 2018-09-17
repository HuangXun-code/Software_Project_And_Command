import threading

class RepeatableTimer(object): 
    
    def __init__(self, interval, function): 
        self.interval = interval
        self.function = function

    def start(self): 
        self.stop()
        self._timer = threading.Timer(self.interval, self._run) 
        self._timer.setDaemon(True) 
        self._timer.start()

    def restart(self): 
        self.start()

    def stop(self): 
        if "_timer" in self.__dict__: 
            self._timer.cancel() 
            del self._timer

    def _run(self): 
        try: 
            self.function() 
        except: 
            pass 
        self.restart()
