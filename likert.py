import json


class User(object):
	'''One user's worth of Likert's data '''
	
	# name = str
	criticidad = int
	eficiencia = list
	agilidad = list
	innovacion = list
	criterio = list
#dic = {'name':'','criticidad':'','eficiencia':'','agilidad':'','innovacion':'','criterio':''}
#name,criticidad,eficiencia,agilidad,innovacion,criterio
	
	def __init__(self,dic:dict):
		
		# self.name=dic['name']
		self.criticidad=dic['criticidad']
		self.eficiencia=dic['eficiencia']
		self.agilidad=dic['agilidad']
		self.innovacion=dic['innovacion']
		self.criterio=dic['criterio']




	def save(self,dic:dict):
		file = open('users.json','w')
		json.dump(dic,file)
		file.close()



