import json

with open('data.json' ,'r' ) as file:
    j = json.load(file)

state = []
for i in j['states']:
    state.append(i['state'])
print(state[24])
        
# print(state[19])

k = 1
for i in j['states']:
    print(f"{k}.{i['state']}")
    k += 1

state_num = int(input("Enter a state number.>> "))


for i in j['states']:
    if i['state'] == state[state_num-1]:
        for e in i['districts']:
            print(e)
  


    

        

# user = input("enter your state number")



