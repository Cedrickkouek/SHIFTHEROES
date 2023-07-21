import requests

#Recupere les differents plannings
headers = {
    'Authorization': 'Bearer 950838ab4e6b1da65cf99b8c02ed8b9b',
}

response = requests.get('https://shiftheroes.fr/api/v1/plannings', headers=headers)

# print(response.json()[2]['id']) #Get the id du troisieme type de planning dont l'index est 2

id_planning =  response.json()[0]['id'] 

#Recuperer les crenaux(shifts) lier aux planning du 3eme type
response = requests.get('https://shiftheroes.fr/api/v1/plannings/' + id_planning + '/shifts', headers=headers)


##print(response.json())
##id_shift =  response.json()[0]['id']
##print(id_shift)

##response = requests.post('https://shiftheroes.fr/api/v1/plannings/' + id_planning + '/shifts/' + id_shift + '/reservations', headers=headers)
##print(response)



#iterate through all elements of the table of shifts and book them all
shift =  response.json()
for i in shift:
    id_shift =  i['id']
    print(id_shift)
    response = requests.post('https://shiftheroes.fr/api/v1/plannings/' + id_planning + '/shifts/' + id_shift + '/reservations', headers=headers)
    print(response)    
