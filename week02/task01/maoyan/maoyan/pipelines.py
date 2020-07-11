# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
from .db_util import ConnDB

db = ConnDB()


class MaoyanPipeline:
    def process_item(self, item, spider):
        name = item['name']
        tags = item['tags']
        release_time = item['release_time']

        sql = 'INSERT INTO t_movies(name,tags,releas_time) VALUES (%s,%s,%s);'
        db.insert(sql, (name, tags, release_time))
        return item
