import random
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder



lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()


one_hot_style = OrdinalEncoder()    #переменная. которая принимает значение функции, чтобы потом заменить значение в категориях
data["whoAmI_OH_code"] = one_hot_style.fit_transform(data[["whoAmI"]])  #здесь мы создаем копию объекта, в котором будут записаны двоичные значения в категориях human и robot
data[["whoAmI", "whoAmI_OH_code"]].head(20)


print(data)
