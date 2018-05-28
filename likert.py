import eel
import json
from functions import *

eel.init('web')


@eel.expose
def load():
	data = load_data()
	return data


@eel.expose
def save(name, dic, existing):
	# print(name, dic, existing)
	result =  new_user(name, dic, existing)
	print(result)


eel.start('likert.html')
