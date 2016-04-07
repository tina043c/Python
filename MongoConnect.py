##sample
#import pymongo
# client = pymongo.MongoClient("10.42.254.9", 27017)
# db = client['sco']


# from pymongo import MongoClient
# client = MongoClient()
# db = client.sco



#D:\@Build\SCO\20151022\saas-ansible-deploy-2.8.0-739.0f49f47.el6.noarch\saas-ansible-deploy-2.8.0-739.0f49f47.el6.noarch\opt\trendmicro\saas\ansible\deploy\roles\sco\files\ets\sjc1\config.ini

import ConfigParser
from pymongo import MongoClient

#config parsing
config_testinfo = ConfigParser.ConfigParser()
###change config.ini
# config_testinfo.readfp(open('/opt/trendmicro/saas/common/etc/config.ini'))
config_testinfo.readfp(open('config.ini'))
mongo_server = config_testinfo.get('mongo','url')
mongo_db = config_testinfo.get('mongo','db')
#print mongo_server

#client = MongoClient()
#client = MongoClient("mongodb://sco:0006@vm-appserver1.saas-sd.lava.tw/storage/sco",27017)
uri = mongo_server
#create connecttion
client = MongoClient(uri,27017)
#get db
db = client[mongo_db]






# #get collection3w
# collection = db["dcron_job"]
# condition = {"valid":True}
# field = {"_id":0,"name":1,"last_run_at":1,"cron_string":1}
# dcrons = collection.find(condition,field)
# print "%s , %s , %s , %s , %s , %s <br>"%("name" , "next_time" , "last_run_at" , "delta_time" , "cron_str" , "status")
# for x in dcrons:
#     #cron_str = croniter.croniter(x["cron_string"], datetime.datetime.now())
#     next_time = croniter.croniter(x["cron_string"], datetime.datetime.now()).get_next(datetime.datetime)
#     last_run_at = datetime.datetime.fromtimestamp(x["last_run_at"])
#     delta_time = next_time-last_run_at
#     #print "%s , %s , %s "%(next_time,last_run_at,delta_time)
#     cron_str = x["cron_string"].split()
#      print "%s , %s , %s , %s , %s , %s <br>"%(x["name"] , next_time , last_run_at , str(delta_time).replace(",",":") , x["cron_string"] , status)