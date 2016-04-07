
import sys

from MongoConnect import db
# rbac_vendor_companies = db['rbac_vendor_companies']
# # post2 = rbac_vendor_companies.find_one()
# # db.hes_domains.find({ "domains" : /^tina^/ }).limit(20);

# rbac_vendor_companies = db['rbac_vendor_companies']
rbac_customer_companies=db['rbac_customer_companies']
rbac_customer_products = db['rbac_customer_products']


data1 = rbac_customer_companies.find_one({"id" : "2429CC85-BBB7-4A1D-939F-9B5C8A522CDE"})
print  "data1: ", data1

print  "cid: ", data1['id']
print  "accounts: ", data1['accounts'][3]

data2 = rbac_customer_products.find_one({"cid" : "2429CC85-BBB7-4A1D-939F-9B5C8A522CDE" })
print  "data2: ", data2



# cursor = rbac_customer_companies.find({"id" : "2429CC85-BBB7-4A1D-939F-9B5C8A522CDE"})
# for document in cursor:
#     print(document)



# 1. enter user name
# 2. choose 1 you like if have more
# 3. list cid vid eid wfbss(did)prodcut name


#cursor = db.restaurants.find()
# cursor = db.accounts.find({"borough": "Manhattan"})
# for document in cursor:
#     print(document)

#
# License, profile	db.rbac_customer_companies
# cyberdyne_profile.find
# Account relative command	{
# "profile.companyprofile.companyname" :"customer041728"
# }
# db.rbac_customer_products.find({ "activationcode" : "NM-YX24-KE8WL-HXAW3-UFGJT-Z5HU2-NLYFD" }).limit(50);
#
# db.rbac_customer_products.find({ "vid" : "TM-B4F3B6C1-1C33-4F6F-9917-CBFE24AC3CF6", "product" : "hes" }).limit(50);
#
# {
#   "accounts.useraccountemail" :"tina_c_chang@trend.com.tw"
# }
#vendor company
# {"accounts.useraccountname" :"tinac3c01"}
#


