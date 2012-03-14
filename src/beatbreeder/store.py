""" beatbreeder.store
"""
import couchdb

from beatbreeder.config import read_config

class DataStore(couchdb.Server):
    """ NB: safe to use as a singleton """
    def __init__(self, config):
        if not hasattr(config, 'database'):
            raise RuntimeError,"expected your config would have a [database] section."
        db = config.database
        self.bb_config = config
        super(DataStore,self).__init__(db['server'])
        self.resource.credentials = ( db['username'], db['password'] )


if __name__=='__main__':
    config = read_config()
    couch = DataStore(config)
    db = couch.create('test123')
    print db #<Database 'test'>
    couch.delete('test123')

    # More examples:
    """
    db['foo'] = {'bar': 'test'}
    print db['foo']
    #<Document 'foo'@'1-1d1b1ba13d97badec02a57adb942cd42' {'bar': 'test'}>
    doc = db['foo']
    db.delete(doc)
    """
