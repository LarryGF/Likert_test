import json
dictionary = {'criticidad': [1, ], 'eficiencia': [5, 1, 2, 4], 'agilidad': [
	3, 2, 4, 5], 'innovacion': [3, 2, 5, 1], 'criterio': [5, 4, 5, 2, 1, 4, 3, 2, 5, 1, 4]}

try:
	file = open('users.json')
	# exisiting_users = json.load(file)

except:
	file = open('users.json', 'w')
	file.write("{}")
	file.close()


def calculate_limits(exisiting_users):
	val = len(exisiting_users)
	limits = {'first': val, 'second': val*2,
			  'third': val*3, 'fourth': val*4, 'fifth': val*5}
	return limits

def remove_user(user):
	try:	
		existing_users = load_data()
		existing_users.pop(user)
		save_data(existing_users)
	except Exception as e:
		return e
	return 'Succes'
	
def new_user(name: str, dic: dict):
	existing_users= load_data()
	existing_users[name] = dic
	print(existing_users)
	# return exisiting_users
	save_data(existing_users)
	return 'Success'


def load_data():
	file = open('users.json')
	users = json.load(file)
	return users


def save_data(exisiting_users):
	file = open('users.json', 'w')
	json.dump(exisiting_users, file)
	file.close()
	return "Success"


def calculate_element(table: str, aspect: int, dic: dict, limits: dict):
	users = dic
	total = 0
	for user in users:
		user_dic = users[user]
		aspect_list = user_dic[table]
		value = aspect_list[aspect]
		total = total + value

	if table == 'criticidad':
		if total < limits['second']:
			return (total, 'Muy Baja')

		elif total < limits['third'] or total == limits['second']:
			return (total, 'Baja')

		elif total < limits['fourth'] or total == limits['third']:
			return (total, 'Media')

		elif total < limits['fifth'] or total == limits['fourth']:
			return (total, 'Alta')

		else:
			return (total, 'Muy Alta')

	else:
		if total < limits['second']:
			return (total, 'No se toma en cuenta')

		elif total < limits['third'] or total == limits['second']:
			return (total, 'Poco importante')

		elif total < limits['fourth'] or total == limits['third']:
			return (total, 'Medianamente importante')

		elif total < limits['fifth'] or total == limits['fourth']:
			return (total, 'Sumamente importante')

		else:
			return (total, 'Indispensable')


def calculate_total(users, limits):
	final_result = {}
	user_dic = users
	limit = limits
	for categoria in dictionary:
		result_list = []
		for i in range(len(dictionary[categoria])):
			result = calculate_element(categoria, i, user_dic, limit)
			result_list.append(result)

		final_result[categoria] = result_list

	return final_result
