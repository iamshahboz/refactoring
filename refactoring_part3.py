# We are going to look at how to clean up code that searches for a dictionary within
# a list of dictionaries. Lets us first define our list of dictionaries
# called organizations 
from pprint import pprint

organizations = [
    {'id': 1, 'is_admin': True, 'secret': 'abc'},
    {'id': 2, 'is_admin': True, 'secret': 'abc'},
    {'id': 3, 'is_admin': False, 'secret': 'abc'},
    {'id': 4, 'is_admin': True, 'secret': 'abc'},
    {'id': 5, 'is_admin': False, 'secret': 'abc'},
]
# Each dictionary has 3 fields- id, is_admin and secret 

# Lets say we need to find an organization with ID 3 and update the existing dictionary
# with some attributes from this organization. We could write the following code to
# do this search 

# FIND_ID = 3 
# response = {'username': 'jeff'} # new dict 

# for org in organizations:
#     org_id = org.get('id')
#     if org_id == FIND_ID:
#         response['id'] = org_id
#         response['is_admin'] = org.get('is_admin',None)
#         break 
# if response.get('id') is None:
#     raise Exception 

# pprint(response)

# Instead of using the loop, we can use a generator expression to find the organization
# with ID of 3(if it exists) or return None otherwise 

FIND_ID = 3 
response = {'username': 'jeff'} # new dict 
# here is the example of generator expression

organization_generator = (org for org in organizations if org['id'] == FIND_ID)
org = next(organization_generator,None)

if org is None:
    raise Exception 

response.update({'id':org['id'], 'is_admin': org['is_admin']})
print(response)





