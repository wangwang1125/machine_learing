import numpy as np

def pearson_score(dataset, user1, user2):
    if user1 not in dataset:
        raise TypeError('user1'+user1+'not person in the dataset')
    if user2 not in dataset:
        raise TypeError('user2'+user2+'not person in the dataset')
        
    rated_by_both = {}
    for item in dataset[user1]:
        if item in dataset[user2]:
            rated_by_both[item] = 1
    
    num_ratings = len(rated_by_both)
    
    if num_ratings == 0:
        return 0
    
    #计算同一用户所有电影评分的之和
    user1_sum = np.sum([dataset[user1][item] for item in rated_by_both])
    user2_sum = np.sum([dataset[user2][item] for item in rated_by_both])

    # 计算同一用户所有电影评分的评分的平方和
    user1_squared_sum = np.sum([np.square(dataset[user1][item]) for item in rated_by_both])
    user2_squared_sum = np.sum([np.square(dataset[user2][item]) for item in rated_by_both]) 
    
    # 计算数据集的乘积之和
    product_sum = np.sum([dataset[user1][item] * dataset[user2][item] for item in rated_by_both]) 
    
    # 计算皮尔逊相关度
    Sxy = product_sum - (user1_sum * user2_sum / num_ratings)
    Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
    Syy = user2_squared_sum - np.square(user2_sum) / num_ratings 
    
    if Sxx * Syy == 0:
        return 0 
    return Sxy / np.sqrt(Sxx * Syy) 
