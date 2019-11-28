from xml.etree import ElementTree as ET
from dateutil.parser import parse


class VideoParser:

    def __init__(self):
        pass

    def log_parser(self, log_path):

        log_list = []

        tree = ET.parse(source=log_path)

        init_timestamp = parse(tree.find('entries/entry/timestamp').text)
        entries = tree.find('entries')
           
        for element in entries:
            action = element.find('action').text
            timestamp = parse(element.find('timestamp').text)
            timestamp = (timestamp-init_timestamp).total_seconds()
            log_list.append({'action':action,'timestamp':timestamp})
        return log_list

if __name__ == '__main__':

    vp = VideoParser()
    test = vp.log_parser(log_path='static/video/log.xml')
    for item in test:
        print(item)