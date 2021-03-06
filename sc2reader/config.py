from processors import *
from readers import *

FULL = "FULL"
PARTIAL = "PARTIAL"
CUSTOM = "CUSTOM"

FILES = {
    "FULL": [
            'replay.initData',
            'replay.details',
            'replay.attributes.events',
            'replay.message.events',
            'replay.game.events'
        ],

    "PARTIAL": [
            'replay.initData',
            'replay.details',
            'replay.attributes.events',
            'replay.message.events'
        ],
}

PROCESSORS = {
    "FULL": [
            PeopleProcessor,
            AttributeProcessor,
            TeamsProcessor,
            MessageProcessor,
            RecorderProcessor,
            EventProcessor,
            ApmProcessor,
            ResultsProcessor,
        ],

    "PARTIAL": [
            PeopleProcessor,
            AttributeProcessor,
            TeamsProcessor,
            MessageProcessor,
            RecorderProcessor,
        ],
}

class ReaderMap(dict):
    def __init__(self):
        self.set1 = {
                'replay.initData': InitDataReader(),
                'replay.details': DetailsReader(),
                'replay.attributes.events': AttributeEventsReader(),
                'replay.message.events': MessageEventsReader(),
                'replay.game.events': GameEventsReader(),
            }

        self.set2 = {
                'replay.initData': InitDataReader(),
                'replay.details': DetailsReader(),
                'replay.attributes.events': AttributeEventsReader(),
                'replay.message.events': MessageEventsReader(),
                'replay.game.events': GameEventsReader_16561(),
            }

        self.set3 = {
                'replay.initData': InitDataReader(),
                'replay.details': DetailsReader(),
                'replay.attributes.events': AttributeEventsReader_17326(),
                'replay.message.events': MessageEventsReader(),
                'replay.game.events': GameEventsReader_16561(),
            }

        for key in (16117,16195,16223,16291):
            self[key] = self.set1

        for key in (16561,16605,16755,16939):
            self[key] = self.set2

        for key in (17326,17682,17811,18092,18221,18317):
            self[key] = self.set3

    def __getitem__(self,key):
        try:
            return super(ReaderMap,self).__getitem__(key)
        except KeyError:
            return self.set3

READERS = ReaderMap()