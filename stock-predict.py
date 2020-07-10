import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./Dataset/BanksDataset/AXISBANK.csv")
data.head(10)
data.drop(["Symbol", "Series","Trades","Deliverable Volume","%Deliverble"], axis= 1)