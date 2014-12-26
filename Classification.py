# Machine Learning Project
__author__ = 'Eslam Hamouda'
import math
from _operator import itemgetter



# Genres : Action | Romance | Horror | Mystry | Sci-Fi | Music | Animation | Comedy | Animation | Cartoon | Fantasy
# this is dummy dataset not real !
# each vector value represents answer to the questions coming later in the code.
dataset = {"Action":[1,0,1,1,1,0,0,1],
           "Romance":[0,1,0,1,0,1,0,0],
           "Horror":[1,1,1,1,1,0,0,0],
           "Mystry":[0,0,0,1,1,0,0,0],
           "Sci-Fi":[1,0,0,1,1,0,0,0],
           "Thriller":[1,0,1,1,0,0,0,0],
           "Adventure":[0,0,1,1,0,0,1,0],
           "Musical":[0,1,0,0,0,1,0,0],
           "Comedy":[0,0,0,0,0,1,1,1],
           "Animation":[0,0,0,0,0,0,1,0],
           "Cartoon":[0,0,0,0,0,0,1,1],
           "Fantasy":[1,0,0,1,1,0,0,0]
           
          }



# calculate the similarity between two genres
def GetCosSimilarityForGenres(user_film,dataset_film):
    v1_2, v2_2,v1_x_v2 =0,0,0
    for i in range(len(user_film)):
        v1_2 += int(user_film[i]) * int(user_film[i])
        v2_2 += dataset_film[i] * dataset_film[i]
        v1_x_v2 += int(user_film[i]) * dataset_film[i]

    sim = (v1_x_v2 / (math.sqrt(v1_2) * math.sqrt(v2_2)))
    return sim



# create the user vector by answering this questions
# this questions in not real too, it's only demonstrate the idea.
user_answer = list()
print("Please Answer this Questions : ")
q1 = input("have you seen any kisses in this film ?")
if q1=="yes":
    user_answer.append(1)
else:
    user_answer.append(0)

q1 = input("have you seen any hits or voilance ?")
if q1=="yes":
    user_answer.append(1)
else:
    user_answer.append(0)

q1 = input("have you seen any space ships ?")
if q1=="yes":
    user_answer.append(1)
else:
    user_answer.append(0)

q1 = input("have you seen any forests ?")
if q1=="yes":
    user_answer.append(1)
else:
    user_answer.append(0)

q1 = input("have you seen any blood ?")
if q1=="yes":
    user_answer.append(1)
else:
    user_answer.append(0)

q1 = input("have you seen cartoon characters ?")
if q1=="yes":
    user_answer.append(1)
else:
    user_answer.append(0)

    q1 = input("have you seen any cars ?")
if q1=="yes":
    user_answer.append(1)
else:
    user_answer.append(0)

q1 = input("have you seen any wars ?")
if q1=="yes":
    user_answer.append(1)
else:
    user_answer.append(0)


user_answer
final_data = list()
# calculate the similarity between the user answers vector and all the data set genres.
# then sort them and pick the highest one. (K=1)
for k,v in dataset.items():
    sim_of_gen = GetCosSimilarityForGenres(user_answer,v)
    final_data.append([k,sim_of_gen])
sorted_data = sorted(final_data,key=itemgetter(1),reverse=True)

# print the result
print("You Film Is Classified as : ",sorted_data[0][0],", by : ",round(sorted_data[0][1]*100),"%")
    