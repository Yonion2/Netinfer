import numpy as np 
import json
import pickle 

def load_pickle(data_path):
    with open(data_path, 'rb') as f:
        data = pickle.load(f)
    return data

def save_pickle(data, data_path):
    with open(data_path, 'wb') as f:
        pickle.dump(data, f)
        
        
#使用np.save和np.load进行numpy文件的管理