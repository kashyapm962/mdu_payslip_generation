import pandas as pd
import numpy as np


def preprocess(file):
	df = pd.read_csv(file,header=None)
	lst = []
	for i in range(0,df.shape[0],5):
		l = []
		for j in df.iloc[i]:
			l.append(j)
		for j in df.iloc[i+2]:
			l.append(j)
		for j in df.iloc[i+3]:
			l.append(j)
		for j in df.iloc[i+4]:
			l.append(j)
		lst.append(l)
	df = pd.DataFrame(lst)
	df.dropna(axis=1,inplace=True,how='all')
	df.drop([1,153,243,244,245],axis=1,inplace=True)
	df[df.columns[0]] = pd.to_datetime(df[df.columns[0]],dayfirst=True)
	df[df.columns[0]] = pd.to_datetime(df[df.columns[0]],dayfirst=True)
	df['month'] = df[df.columns[0]].dt.month
	df['year'] = df[df.columns[0]].dt.year
	df.month[df.month == 1] = 'JAN'
	df.month[df.month == 2] = 'FEB'
	df.month[df.month == 3] = 'MARCH'
	df.month[df.month == 4] = 'APRIL'
	df.month[df.month == 5] = 'MAY'
	df.month[df.month == 6] = 'JUNE'
	df.month[df.month == 7] = 'JULY'
	df.month[df.month == 8] = 'AUG'
	df.month[df.month == 9] = 'SEPT'
	df.month[df.month == 10] = 'OCT'
	df.month[df.month == 11] = 'NOV'
	df.month[df.month == 12] = 'DEC'
	df.drop(df.columns[0],inplace=True,axis=1)
	df[df.columns[7]].fillna(-1.0,inplace=True)
	df[df.columns[7]] = df[df.columns[7]].astype('int')
	df[df.columns[7]] = df[df.columns[7]].astype('str')
	df[df.columns[7]][df[df.columns[7]] == '-1'] = np.nan
	df[df.columns[8]].fillna(-1.0,inplace=True)
	df[df.columns[8]] = df[df.columns[8]].astype('int')
	df[df.columns[8]] = df[df.columns[8]].astype('str')
	df[df.columns[8]][df[df.columns[8]] == '-1'] = np.nan
	df.fillna(' ',inplace=True)
	return df.values
		
