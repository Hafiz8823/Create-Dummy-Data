# To create Dummy profile data, I took help of Pandas library.
# import required library and modules.

from faker import Faker 
import pandas as pd
fake = Faker() 
data=[fake.profile()for i in range(50)]
data=pd.DataFrame(data)
print(data.head())