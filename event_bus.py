class EventBus:
    def __init__(self):
        self.__handlers = [] 

    def Subscribe(self, event_type, method):
        self.__handlers.append([event_type, method])

    def RaiseEvent(self, event_type, *args):
        call_methods = [m for et, m in self.__handlers if et == event_type]
        for method in call_methods:
            method(*args)

    def Unsubscribe(self, event_type, method):
        self.__handlers.remove([event_type, method])


def func(data):
    print('func: {}'.format(data))


def dunc(data):
    print('dunc: {}'.format(data))


def raiseAll(event_bus):
    print()
    event_bus.RaiseEvent('func-event', 'Hello')
    event_bus.RaiseEvent('dunc-event', 'Fuck')


if __name__ == '__main__':
    event_bus = EventBus()

    event_bus.Subscribe('func-event', func)
    event_bus.Subscribe('func-event', dunc)
    event_bus.Subscribe('dunc-event', dunc)

    raiseAll(event_bus)

    event_bus.Unsubscribe('func-event', dunc)
    raiseAll(event_bus)