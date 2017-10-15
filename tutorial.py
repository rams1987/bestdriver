import xgboost as xg  # Calculate Gradient faster
import pandas as pd  # Data processing - Easy Input/Ouput
import matplotlib.pyplot as plt  # plotting library



def check_data(train_data, test_data):
    print('train {}'.format(train_data.shape), 'test {}'.format(test_data.shape))  # shape of the data
    print('header {}'.format(train_data.head()))  # header of the data

    # check if the data is repeated
    train_id = train_data['id']
    test_id = test_data['id']
    # check to see if there is any overlap
    if (set(train_id) & set(test_id)):
        print('id Overlap')
    return train_data, test_data

def data_cleanup(train_data, test_data):
    train_data.drop('id',axis=1,inplace=True)
    test_data.drop('id', axis=1, inplace=True)
    return train_data, test_data

if __name__ == "__main__":
    train_data = pd.read_csv('/home/lakeba/kaggle/safeDriverPrediction/data/train.csv')
    test_data = pd.read_csv('/home/lakeba/kaggle/safeDriverPrediction/data/test.csv')
    train_data, test_data = check_data(train_data,test_data)
    print('check completed')
    train_data, test_data = data_cleanup(train_data,test_data)
    print('cleanup completed')