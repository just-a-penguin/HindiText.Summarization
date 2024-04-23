#give code to load a csv using dataloader for .csv that has 2 columns articles and summary
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd

class CustomDataset(Dataset):

    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data.iloc[idx]
    
dataset = CustomDataset('data.csv')
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)


#give code to load a csv using load_dataset for validation
from datasets import load_dataset
dataset = load_dataset('csv', data_files='data.csv')
dataset = dataset['train']
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

article_train = df_train['Article'].tolist()
article_summary = df_train['Summary'].tolist()

#give code to make dataset_dict using above data
d