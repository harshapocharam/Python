import pickle
import numpy as np

data_dick = {
    'volts': np.random.random(10),
    'current':np.random.random(10),
}
# with open('data_pickle.pkl', 'wb') as pickle_file:
#     # Hear data_dick is a dictionary so are storing in an object called pickle_file 
#     # so to do that we use dump() method in python.
#     pickle.dump(data_dick,pickle_file)

with open('data_pickle.pk1', 'rb') as pickle_file:
    new_data = pickle.load(pickle_file)
print(new_data)
 