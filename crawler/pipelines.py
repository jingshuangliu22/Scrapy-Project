# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os
import sys

sys.path.append('../website')

from getcomments import GetComments


class CrawlerPipeline(object):
    def __init__(self):
        self.current_dir = os.getcwd()

    def process_item(self, item, spider):
        dir_path = self.current_dir + '/docs/' + 'finance' + '/' + item['date']
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        news_file_path = dir_path + '/' + item['newsId'] + '.json'
        if os.path.exists(news_file_path) and os.path.isfile(news_file_path):
            print '---------------------------------------'
            print item['newsId'] + '.json exists, not overriden'
            print '---------------------------------------'
            return item
        para_dict = {'sina':{'source':'sina', 'cmtId':item['newsId'], 'channelId':item['channelId'], 'boardId':'news_shehui7_bbs'} }
        news_file = codecs.open(news_file_path, 'w', 'utf-8')
        line = json.dumps(dict(item))
        news_file.write(line)
        js = json.dumps(GetComments(para_dict['sina']))
        f = open(dir_path + '/' + item['newsId'] + '-comments.json', 'w')
        f.write(js)
        f.close()
        news_file.close()
        return item
