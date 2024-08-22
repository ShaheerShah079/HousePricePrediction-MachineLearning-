import json
import pickle

__col_name=None
__location=None
__model=None

def get_locations_name():
    global __location
    with open('../model/columns.json', 'r') as f:
        __col_name = json.load(f)['data_col']
        __location = __col_name[3:]
    return __location


def predict_price(location, sqft, bath, bhk):
    global __col_name
    global __location
    global __model
    with open('../model/columns.json', 'r') as f:
        __col_name = json.load(f)['data_col']
        __location = __col_name[3:]
    print('location load', __location)
    with open('../model/bengaluru_house_prices', 'rb') as f:
        __model = pickle.load(f)
    index = __col_name.index(location.lower())
    length = (len(__col_name))
    default_list = [False] * length

    default_list[0] = sqft
    default_list[1] = bath
    default_list[2] = bhk

    if index >= 0:
        default_list[index] = True
    return __model.predict([default_list])[0]

def load_save():
    print("loading save")
    global __col_name
    global __location
    global __model
    with open('../model/columns.json','r') as f:
        __col_name=json.load(f)['data_col']
        __location=__col_name[3:]
    print('location load',__location)
    with open('../model/bengaluru_house_prices','rb') as f:
        __model=pickle.load(f)
    print('Loading done')


if __name__ == '__main__':
    print('Starting util')
    load_save()
    print(get_locations_name())
    print(predict_price('Indira Nagar', 1000.000 , 3.0 , 3 ))

