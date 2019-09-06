#!/usr/bin/python36
import keras 
import sys
import numpy as np

inp=sys.argv[1:]

import keras
from keras.models import Sequential
from keras.layers import Dense,Activation
lambd=0
labels=8
mod=Sequential()
mod.add(Dense(labels,input_shape=(18,),kernel_regularizer=keras.regularizers.l2(lambd)))
mod.add(Activation('sigmoid'))


mod.load_weights("predmod.h5")

f=open('PEfet.csv')
allfet=f.read().split(',')
f1=open('output.csv')
outfet=f1.read().split(',')


def mypred(pastlst,fm,em):
	i=0
	val=0
	fet=[]
	for x in allfet:
		val=0
		if x.strip() in pastlst:
			val=1
		fet.append(val)
	fet.append(fm)
	fet.append(em)
	return fet
X=mypred(inp[0],inp[1],inp[2])
X=np.array(X)

out=mod.predict(X.reshape(1,-1))
outsrt=np.argsort(out,axis=1)
ind1=outsrt[0,-1]
ind2=outsrt[0,-2]
print([outfet[ind1],outfet[ind2]])





