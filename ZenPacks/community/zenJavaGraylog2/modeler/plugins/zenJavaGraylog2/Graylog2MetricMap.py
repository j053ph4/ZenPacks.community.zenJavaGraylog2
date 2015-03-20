from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaGraylog2.Definition import *

__doc__ = """Graylog2MetricMap

Graylog2MetricMap detects JVM Graylog2 Mertics on a per-JVM basis.

This version adds a relation to associated ipservice and javaapp components.

"""

class Graylog2MetricMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(Graylog2MetricDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'metrics:name=*'
    
    def isEnabled(self, port, mbean, log):
        '''decide whether or not this should be monitored'''
        jmx = self.scan.portdict[port]
        self.scan.proxy.setJMX(jmx)
        result = self.scan.proxy.getBeanAttributeValues(mbean, ['Count','Mean','FiveMinuteRate'])
        if 'Count' in result.keys():  return True
        return False
    
    def postprocess(self, result, om, log):
        ''''''
        om.monitor = self.isEnabled(result['port'], result['mbean'], log)
        return om

