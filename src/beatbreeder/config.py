"""
"""
import ConfigParser
from collections import defaultdict, namedtuple

def read_config(conf_file='beatbreeder.ini'):
    """ returns dictionary of the configuration being used """
    cp = ConfigParser.ConfigParser()
    cp.read(conf_file)
    config = defaultdict(lambda: {})
    for sec in cp.sections():
        sec_name = sec.lower()
        var_names = cp.options(sec)
        for opt in var_names:
            config[sec_name][opt] = cp.get(sec, opt).strip()
    ConfigObject = namedtuple('BreederConfig', config.keys())
    return ConfigObject(**config)

if __name__ == '__main__':
    print read_config()
