from ZenPacks.community.ConstructionKit.ClassHelper import *

def Graylog2MetricgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class Graylog2MetricInfo(ClassHelper.Graylog2MetricInfo):
    ''''''


