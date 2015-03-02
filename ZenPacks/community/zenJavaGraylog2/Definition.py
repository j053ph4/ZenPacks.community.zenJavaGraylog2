from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *
from ZenPacks.community.zenJavaApp.Definition import getMBeanDef, addMBeanRelations


ROOT = "ZenPacks.community"
BASE = "zenJavaGraylog2"
VERSION = Version(1, 0, 0)


###################### Graylog2MetricDefinition
definition = getMBeanDef(VERSION, ROOT, BASE, 'Graylog2Metric','Graylog2 Metric', 'Graylog2 Metrics')
definition['componentData']['displayed'] = 'mbean'
Graylog2MetricDefinition = type('Graylog2MetricDefinition', (BasicDefinition,),  definition)
addMBeanRelations(Graylog2MetricDefinition)


