# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class MaoyanPipeline:
    def process_item(self, item, spider):
        name = item['name']
        tags = item['tags']
        release_time = item['release_time']

        output = [{'name': name, 'tags': tags, 'release_time': release_time}]
        movies = pd.DataFrame(data=output)
        # 输出header
        movies.to_csv('./maoyan_movies02.csv', mode='a', encoding='utf8', index=False, header=True)
        return item
