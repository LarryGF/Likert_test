from functions import *

dic ={'criticidad':[],'eficiencia':[5,1,2,4],'agilidad':[3,2,4,5],'innovacion':[3,2,5,1],'criterio':[5,4,5,2,1,4,3,2,5,1,4]}
users = load_data()
users = new_user('fernando',dic,users)
limits = calculate_limits(users)
save_data(users)

# final = calculate_total('eficiencia',3,users,limits)
# print(final)