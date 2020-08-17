import numpy as np

def find_similar_users(dataset, user, num_users):
    if user not in dataset:
        raise TypeError("user:"+user +'not in present in the dataset')
        
    #计算所有用户皮尔逊相关度
    scores = np.array([[alluser, pearson_score(dataset, user, alluser)] for alluser in dataset if user!=alluser])
    #评分在第二列按降序排列
    scores_sorted = np.argsort(scores[:,1])
    scored_sorted_dec = scores_sorted[::-1]
    
    #提取出k个最高分
    top_k = scored_sorted_dec[0:num_users]
    return scores[top_k]
