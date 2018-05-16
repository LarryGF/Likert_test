import json


try:
	file = open('users.json')
	# exisiting_users = json.load(file)
	
except:
	file = open('users.json','w')
	file.write("{}")
	file.close()
	

def calculate_limits(exisiting_users):
	val = len(exisiting_users)
	limits = {'first':val,'second':val*2,'third':val*3,'fourth':val*4,'fifth':val*5}
	return limits

def new_user(name:str,dic:dict,exisiting_users):
	exisiting_users[name]=dic
	return exisiting_users

def load_data():
	file = open('users.json')
	users = json.load(file)
	return users

def save_data(exisiting_users):
	file = open('users.json','w')
	json.dump(exisiting_users,file)
	file.close()
	
def calculate_element(table:str,aspect:int,dic:dict,limits:dict):
	users = dic
	total = 0
	for user in users:
		user_dic = users[user]
		aspect_list = user_dic[table]
		value = aspect_list[aspect]
		total = total + value
	
	if table == 'criticidad':
		if total < limits['second']:
			return 'Muy Baja'

		elif total < limits['third'] or total == limits['second']:
			return 'Baja'

		elif total < limits['fourth'] or total == limits['third']:
			return 'Media'

		elif total < limits['fifth'] or total == limits['fourth']:
			return 'Alta'

		else:
			return 'Muy Alta'

	else:
		if total < limits['second']:
			return 'No se toma en cuenta'

		elif total < limits['third'] or total == limits['second']:
			return 'Poco importante'

		elif total < limits['fourth'] or total == limits['third']:
			return 'Medianamente importante'

		elif total < limits['fifth'] or total == limits['fourth']:
			return 'Sumamente importante'

		else:
			return 'Indispensable'



