import time
import requests

#Recupere les differents plannings
headers = {
    'Authorization': 'Bearer 950838ab4e6b1da65cf99b8c02ed8b9b',
}

start_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
actual_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()

while start_liste != actual_liste:
    actual_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json() 
    time.sleep(1)
    
print("Nouveau planning daily dispo!")
id_planning = actual_liste[0]["id"]
print(id_planning)

crenauxDuPlanning = requests.get('https://shiftheroes.fr/api/v1/plannings/' + id_planning + '/shifts', headers=headers).json()
print(crenauxDuPlanning)

for i in crenauxDuPlanning:
    id_shift =  i['id']
    print("*****")
    print(id_shift)
    print("*****")
    response = requests.post('https://shiftheroes.fr/api/v1/plannings/' + id_planning + '/shifts/' + id_shift + '/reservations', headers=headers)
    print(response)
    print("*****")


# print(response.json()[2]['id']) #Get the id du troisieme type de planning dont l'index est 2

#id_planning =  response0.json()[0]['id'] 

#Recuperer les crenaux(shifts) lier aux planning du type daily avec index 0 dans la reponse Json
#response1 = requests.get('https://shiftheroes.fr/api/v1/plannings/' + id_planning + '/shifts', headers=headers)
#print(response1.json())

##print(response.json())
##id_shift =  response.json()[0]['id']
##print(id_shift)

##response = requests.post('https://shiftheroes.fr/api/v1/plannings/' + id_planning + '/shifts/' + id_shift + '/reservations', headers=headers)
##print(response)



#iterate through all elements of the table of shifts and book them all
#shift =  response1.json()
"""for i in shift:
    id_shift =  i['id']
    print(id_shift)
    #response = requests.post('https://shiftheroes.fr/api/v1/plannings/' + id_planning + '/shifts/' + id_shift + '/reservations', headers=headers)
    #print(response)
    
while True:
    response2 = requests.get('https://shiftheroes.fr/api/v1/plannings/' + id_planning + '/shifts', headers=headers)
    if response2.json() != response1.json():
        response1 = response2
        shift0 = response2.json()
        for i in shift0:
            id_shift1 =  i['id']
            response = requests.post('https://shiftheroes.fr/api/v1/plannings/' + id_planning + '/shifts/' + id_shift1 + '/reservations', headers=headers)
            print(response.json())
    time.sleep(2)"""
