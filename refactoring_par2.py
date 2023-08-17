from pprint import pprint
class Campaign:
    def __init__(self, id, name, status, customer_id, uid):
        self.id = id 
        self.name = name 
        self.status = status 
        self.customer_id = customer_id 
        self.uid = uid 

campaign = Campaign('Test Name', 111, 'Ready', 50, 'my_super-uid')

# Lets say we want to grab some of the fields from this class and put them into a 
# Python dictionary.Perhaps this dictionary will be served as an API response via JSON
# You may write a code like the following-importantly note that the dictionary keys
# have the same name as the fields of the class

# campaign_dict = {}
# campaign_dict['id'] = campaign.id 
# campaign_dict['name'] = campaign.name 
# campaign_dict['status'] = campaign.status 
# campaign_dict['customer_id'] = campaign.customer_id 
# campaign_dict['uid'] = campaign.uid

# pprint(campaign_dict)

# Now lets see how can can refactor this

keys = ('id', 'name', 'status', 'customer_id', 'uid')
campaign_dict = {key: getattr(campaign, key) for key in keys}
pprint(campaign_dict)

# lets see what getattr do

#print(getattr(campaign, 'status'))
# as you see it is ckecking the object for the attribute(field) with that name

# you could use __dict__ method to get all the attributes from the dictionary
#pprint(campaign.__dict__)



