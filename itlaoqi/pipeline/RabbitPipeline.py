import pika.credentials
import json


class RabbitPipeline:
    host = 'himcs.io'
    virtual_host = '/itlaoqi'
    username = 'mcs'
    password = 'mcs'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host,
                                                                            virtual_host=self.virtual_host,
                                                                            credentials=pika.PlainCredentials(
                                                                                username=self.username,
                                                                                password=self.password)))
        self.channel = self.connection.channel()

    def close_spider(self, spider):
        self.channel.close()
        self.connection.close()

    def process_item(self, item, spider):
        exchange = item['exchange']
        del item['exchange']
        self.channel.basic_publish(exchange=exchange,
                                   routing_key='',
                                   body=json.dumps(item, ensure_ascii=False))
        return item
