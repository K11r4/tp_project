class Controller:
    def __init__(self):
        self.listeners = dict()

    def subscribe(self, eventType, listener):
        if not eventType in self.listeners:
            self.listeners[eventType] = set()
        self.listeners[eventType].add(listener)
        #print(self.listeners)

    def unsubscribe(self, eventType, listener):
        self.listeners[eventType].pop(listener)

    def notify(self, event):
        if event.type in self.listeners:
            for listener in self.listeners[event.type]:
                listener.update(event)
                
    