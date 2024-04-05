import random
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder



lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()


one_hot_style = OrdinalEncoder()
data["whoAmI_OH_code"] = one_hot_style.fit_transform(data[["whoAmI"]])
data[["whoAmI", "whoAmI_OH_code"]].head(11)



print(data)
