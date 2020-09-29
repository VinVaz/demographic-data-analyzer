import pandas as pd

adult_file = pd.read_csv("./adult.data", names=["age","workclass","fnlwgt",
                                                "education","education-num",
                                                "marital-status","occupation",
                                                "relationship","race","sex",
                                                "capital-gain","capital-loss",
                                                "hours-per-week",
                                                "native-country","salary"])
                                                
print(adult_file)
