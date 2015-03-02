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
    
    
    def isEnabled(self, port, mbean, protocol, log):
        '''decide whether or not this should be monitored'''
        result = self.scan.proxy.get(self.scan.ipaddr, port, self.scan.username, self.scan.password, mbean)
        log.debug('params: %s, %s %s %s %s' % (self.scan.ipaddr, port, self.scan.username, self.scan.password, mbean))
        log.debug("result: %s" % result)
        result = self.scan.getBeanAttributeValues(port=port, mbean=mbean, attributes=['Count','Mean','FiveMinuteRate'], protocol=protocol)
        log.debug("result: %s" % result)
        if 'Count' in result.keys():  return True
        return False
     
    def process(self, device, results, log):
        #log.info("got %s results" % len(results))
        log.info("The plugin %s returned %s results." % (self.name(), len(results)))
        #self.scan =  None
        if len(results) == 0: return None
        rm = self.relMap()
        for result in results:
            if self.isEnabled(result['port'], result['mbean'], result['protocol'], log) is False: continue
            enabled = result['enabled']
            result.pop('enabled')
            om = self.objectMap(result)
            om.setJavaapp = ''
            om.setIpservice = ''
            om.monitor = enabled 
            rm.append(om)
            log.debug(om)
        return rm

