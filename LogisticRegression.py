# Machine Learning Project
__author__ = 'Eslam Hamouda'
import math

# dummy dataset contains some details about each student
# each student vector contains his [GPA, GRE TOEFL], [Accepted(1) or Not Accepted(0)]
# then we want to predict the coming student will be accepted or not based on this dataset after training.

dataset = {"Eslam":[[4,90,40],1],
           "Ahmed":[[3,95,45],0],
           "Hossam":[[2,10,30],0],
           "Mohamed":[[3,100,100],1],
           "Amr":[[3,50,20],0],
           "Bahaa":[[4,80,30],1],
           }


# sigmoid function returns a value netween 0 and 1
def sigmoid(z):
    y = (1 / (1 + math.exp(-1 * z)))
    return y

# initial weights for each value in the students grades vector
w1,w2,w3 = .1,.2,.3

# calculate summation of weights multiplied by each grades vector value
def sum_w(x):
    return w1 * x[0] + w2 * x[1] + w3 * x[2]

# update the wrong weights to find a new correct one for the learning process.
def update_w(wo,d,y,x):
    print("old w :",wo) # in case you want to print the old weight
    a = 0.001 # learinig rate (CONSTANT) - should be very small value
    wn = wo + a * (d - y) * x
    print("new w :",wn) # in case you want to insure the new weight is different from the old one.
    return wn

TRAINING_ROUNDS = 30 # number of training iterations

for t in range(1,TRAINING_ROUNDS):
    print(("*" * 5)," Round ",t,("*") * 5)
    # for each student grades vector calculate the sigmoid value and round it to 0 or 1
    for k,v in dataset.items():
        test1 = round(sigmoid(sum_w(v[0])))
        # check if the returned value matches the accepted value of the student
        while test1 != v[1]:
            # if not matched then we have to update the weights until it became correct.
            w1 = update_w(w1,v[1],test1,v[0][0])
            w2 = update_w(w2,v[1],test1,v[0][1])
            w3 = update_w(w3,v[1],test1,v[0][2])
            test1 = round(sigmoid(sum_w(v[0])))
        print(k," : ",test1) # in case you want to see the accepted value of each student after every learning round.

# ask the user to enter the new grades vector to predict it will be accepted or not.
user_data = input("please enter GPA GRE TOEFL :") # seprated by space ex:4 80 40
user_attr = list()
# create the user grades vector
for v in user_data.split(" "):
    user_attr.append(int(v))
# test it based on the current correct weights
test2 = sigmoid(sum_w(user_attr))
# print the result as 0 or 1
print("User Accpted : ", round(test2))