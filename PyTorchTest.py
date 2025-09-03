import pandas as pd 
import numpy as np 
import torch 
import matplotlib.pyplot as plt 
import torch.nn as nn
import torch.optim as optim  
torch.manual_seed(42)
ap=pd.read_csv('streeteasy.csv')
num_ft=['size_sqft','bedrooms','bathrooms','min_to_subway','floor','building_age_yrs']
X=torch.tensor(ap[num_ft].values,dtype=torch.float)
class NeuralNetwork(nn.Module):
    def __init__(self):
      super(NeuralNetwork,self).__init__()
      self.l1=nn.Linear(6,1024)
      self.relu=nn.ReLU()
      self.l2=nn.Linear(1024,512)
      self.l3=nn.Linear(512,1)
    
    def forward(self,x):
      x=self.l1(x)
      x=self.relu(x)
      x=self.l2(x)
      x=self.relu(x)
      x=self.l3(x)
      return x
#model= nn.Sequential(nn.Linear(2, 128),nn.ReLU(),nn.Linear(128, 64),nn.ReLU(),nn.Linear(64, 1))
y=torch.tensor(ap['rent'].values,dtype=torch.float)
model=NeuralNetwork()
learning_rate=0.01
loss_arr=[]
epoch_arr=[]
for i in range(10):
  pred=model(X)
  loss=nn.MSELoss()
  mse=loss(pred,y)
  if ((i+1)%100==0):
     print((i+1),"->",mse**(0.5),"lr=",learning_rate)
  optimizer = optim.Adam(model.parameters(),lr=learning_rate)
  mse.backward()
  optimizer.step()
  optimizer.zero_grad()
  print(np.array(loss))
#  loss_arr.append(loss.detach())
#  epoch_arr.append(i+1)
