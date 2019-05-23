#! /usr/bin/env python
class FilterModule(object):
    def filters(self):
        return {
            'snort_interface': self.filter_snort_interface,
        }

    def filter_snort_interface(self, interfaces):
        for interface in interfaces:
            if interface != 'lo':
                snort_interface = interface
                break
        return snort_interface
