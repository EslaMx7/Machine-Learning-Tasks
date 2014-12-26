# Machine Learning Project
__author__ = 'Eslam Hamouda'
import math
from _operator import itemgetter
import json,sys


#Genres Action | Romance | Horror | Mystry | Sci-Fi
# dummy dataset copied from the IMDb top 250 film with some fabrications.
dataset = dict()
# load the dataset from json file.
with open("recommendation_dataset.json","r") as dataset_file2:
    dataset =json.loads(dataset_file2.read())

# calculate the similarity between two films
def GetCosSimilarityForGenres(user_film,dataset_film):
    v1_2, v2_2,v1_x_v2 =0,0,0
    for i in range(len(user_film[0])):
        v1_2 += user_film[0][i] * user_film[0][i]
        v2_2 += dataset_film[0][i] * dataset_film[0][i]
        v1_x_v2 += user_film[0][i] * dataset_film[0][i]

    sim = (v1_x_v2 / (math.sqrt(v1_2) * math.sqrt(v2_2)))
    return sim

# some code used for the GUI of this script.
user_film=""
if len(sys.argv) > 1 and sys.argv[1] =="-r": # return the recommended films directly given a film name.
    user_film=sys.argv[2]
elif len(sys.argv)>1 and sys.argv[1] =="-list": # return all dataset film names only
    for f in dataset.keys():
        print(f)
    exit(0)
else:
    user_film = input("Enter the film name :") # in case you run the script without any arguments you will be asked to enter a film name from the dataset.

# check if the user film in the dataset or not.
if user_film not in dataset.keys():
    print("this film is not in the dataset.")
    exit(0)

# get the film vector from the dataset
film_attr = dataset[str(user_film)]
final_data = list()
# for each film in the dataset calculate the similarity between it and the user film.
for k,v in dataset.items():
    # caculate the similarity based on the film genres.
    sim_of_gen = GetCosSimilarityForGenres(film_attr,v)
    # then add the total rating of the film to the score.
    total_score = (sim_of_gen + v[1])
    # don't add the user film itself to avoid recommending it because it's completely similar
    if k != user_film:
        final_data.append([k,total_score])
# sort the final data by the total score
sorted_data = sorted(final_data,key=itemgetter(1),reverse=True)

# recommend the top 3 films
for i in range(0,3):
    print("Film : ",sorted_data[i][0]," | Rate : ", round(sorted_data[i][1],1))
    