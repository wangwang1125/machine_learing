import numpy as np

def euclidean_score(dataset, user1, user2):
    if user1 not in dataset:
        raise TypeError('User' + user1 + 'not present in the dataset')
    if user2 not in dataset:
        raise TypeError('User' + user2 + 'not present in the dataset')
        
    rated_by_both = {}
    for item in dataset[user1]:
        if item in dataset[user2]:
            rated_by_both[item] = 1
        
    if len(rated_by_both)==0:
        return 0;
    print(rated_by_both)
    squated_differences = []
    for item in dataset[user1]:
        if item in dataset[user2]:
            squated_differences.append(np.square(dataset[user1][item] - dataset[user2][item]))
    return 1/(1 + np.sqrt(np.sum(squated_differences)))
