class UnitOfWork:
    def __init__(self, mapper):
        self.mapper = mapper
        self.newObjects = []
        self.dirtyObjects = []
        self.removedObjects = []

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

    def rollback():
        pass

