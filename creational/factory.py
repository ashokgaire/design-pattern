from abc import ABC , abstractmethod

class Knife(ABC):
    @abstractmethod
    def getKnife(self):
        pass

class LargeKnife:
    def getKnife(self):
        return("large knife called")

class SmallKnife:
    def getKnife(self):
        return("small knife called")


class KnifeFactory:
    def get_required_knife(self,knifetype):
        return knifetype.getKnife()


factory = KnifeFactory()
print(factory.get_required_knife(LargeKnife()))
print(factory.get_required_knife(SmallKnife()))

