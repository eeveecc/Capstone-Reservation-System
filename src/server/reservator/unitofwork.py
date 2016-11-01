class UnitOfWork:
    def __init__(self):
        self.mapper = None
        self.newObjects = []
        self.dirtyObjects = []
        self.removedObjects = []

    def attachMapper(self, mapper):
        self.mapper = mapper

    def registerNew(self, obj):
        self.newObjects.append(obj)

    def registerDirty(self, obj):
        self.dirtyObjects.append(obj)
    
    def registerRemoved(self, obj):
        self.removedObjects.append(obj)

    def commit(self):
        self.mapper.insert(self.newObjects)
        self.mapper.update(self.dirtyObjects)
        self.mapper.delete(self.removedObjects)
        
        #clear buffers
        del self.newObjects[:]
        del self.dirtyObjects[:]
        del self.removedObjects[:]

    def rollback():
        pass


