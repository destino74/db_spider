# -*- coding: utf-8 -*-

# Scrapy settings for db_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'db_spider'

SPIDER_MODULES = ['db_spider.spiders']
NEWSPIDER_MODULE = 'db_spider.spiders'
DOWNLOAD_DELAY = 2
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'db_spider (+http://www.yourdomain.com)'
