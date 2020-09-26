import datetime
import random
import numpy
import math
import random
from datetime import date, timedelta
from numpy.lib.stride_tricks import as_strided
import pandas as pd
import numpy as np
from  pathlib import Path
from os import path
import shutil
import os
import pdb
from digfilters import filters
from bandperiod import bandpassfilt
from hurst import compute_Hc
from deap  import algorithms,base,creator,gp,base,creator,tools
import itertools
import operator
k=pd.read_pickle('indvars.pkl')
print(len(k))
def funcgen(gtval,dir):
    if(dir==1):
        def func(val):
            if(val>gtval):
                return True
            else:
                return False
    else:
        def func(val):
            if(val>gtval):
                return False
            else:
                return True


    return func   
def gt(num1,num2):
    if num1>=num2:
        return 1
    else:
        return 0
def gt1(num1,num2):
    if num1>=num2:
        return -1
    else:
        return 0


def ls(num1,num2):
    if num1>=num2:
        return 0
    else:
        return 1
def ls1(num1,num2):
    if num1>=num2:
        return 0
    else:
        return -1

def protectedDiv(left,right):
    try:
        return left/right
    except Exception:
        return 1
def fit(individual):
    return 1

pset=gp.PrimitiveSetTyped('main',itertools.repeat(float,12),float)
pset.addPrimitive(gt,[float,float],float)
pset.addPrimitive(ls,[float,float],float)
pset.addPrimitive(gt1,[float,float],float)
pset.addPrimitive(ls1,[float,float],float)

#pset.addPrimitive(operator.xor, [bool, bool], bool)
#pset.addPrimitive(operator.and_, [bool, bool], bool)
#pset.addPrimitive(operator.or_, [bool, bool], bool)
#pset.addPrimitive(operator.not_, [bool], bool)
pset.addPrimitive(operator.add, [float, float], float)
pset.addPrimitive(operator.mul, [float, float], float)
pset.addPrimitive(operator.sub, [float, float], float)
pset.addPrimitive(protectedDiv, [float, float], float)
pset.addPrimitive(math.cos, [float], float)
pset.addPrimitive(math.sin, [float], float)
pset.addPrimitive(math.tanh, [float], float)
def get_key(val,my_dict): 
    keys=[]
    for key, value in my_dict.items(): 
         if val == value: 
             keys.append(key) 
  
    return keys
for i in range(1,20):
        pset.addTerminal(i*0.05,float)
k['ranchoice']=[random.choice([-1,0,1]) for _ in range(len(k))]
def fiteval(individual,treeorret):
    global k
    penalty=0
    nodes,edges,evals=gp.graph(individual)
    print(evals)
    print(len(evals))
    keys = get_key('gt',evals)
    keys1 = get_key('ls',evals)
    keys2 = get_key('ls1',evals)
    keys3 = get_key('gt1',evals)
    print(keys)
    print(keys1)
    f=gp.compile(individual,pset)
    def f1(row):
      x=np.array(row)
      try:
          return f(*x)
      except Exception as e:
          return 0
    def pencalc(keys): 
        penalty=0
        for i in keys:
            subject = [evals[i+1],evals[i+2]]
            print(subject)
            cond = (operator.or_(*[isinstance(j,float) for j in subject]) and (any(i in pset.arguments for i in subject)) ) 
            print(cond)
            if(cond==True):
                if((subject[0] in pset.arguments) and
                 isinstance(subject[1],float)):
                    penalty=penalty+10



                penalty=penalty+10
        return penalty
    presgt='gt' not in evals.values()
    presls = 'ls' not in evals.values()
    pres=presgt and presls
    presgt='gt1' not in evals.values()
    presls = 'ls1' not in evals.values()
    pres1=presgt and presls

    print(pres)
    peninc = -100 if pres else 10
    peninc1 = -100 if pres1 else 10
    penaltyfin=pencalc(keys)+pencalc(keys1)+pencalc(keys2)+pencalc(keys3)+peninc+peninc1-len(evals)
    if(treeorret):
        k['vals']=k.drop(['targret','Symbol','ranchoice'],axis=1).apply(f1,axis=1)
        retfit = (k.vals*k.targret).sum()-(k.ranchoice*k.targret).sum() 
        k = k.drop('vals',axis=1)
        return (penaltyfin,retfit)
    else:
        return(penaltyfin,)


#pset.addTerminal(1,bool)
#pset.addTerminal(0,bool)
pset.addEphemeralConstant('a',lambda:random.uniform(-1,1),ret_type=float)
creator.create('fit',base.Fitness,weights=(1,))
creator.create('Individual',gp.PrimitiveTree,fitness=creator.fit,pset=pset)
toolbox=base.Toolbox()
toolbox.register('expr',gp.genHalfAndHalf,pset=pset,min_=3,max_=7)
toolbox.register('individual',tools.initIterate,creator.Individual,toolbox.expr)
toolbox.register('population',tools.initRepeat,list,toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)
toolbox.register("evaluate",fiteval,treeorret=False)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

def main(gen_size,pop = toolbox.population(n=300)):
    random.seed(318)
    hof = tools.HallOfFame(10)
    
    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", numpy.mean)
    mstats.register("std", numpy.std)
    mstats.register("min", numpy.min)
    mstats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, gen_size, stats=mstats,
                                   halloffame=hof, verbose=True)
    # print log
    return pop, log, hof
if __name__ == "__main__":
    pop,log,hof=main(70,pop=toolbox.population(n=500))
    toolbox.register("evaluate",fiteval,treeorret=True)
    creator.create('fit',base.Fitness,weights=(1,1))
    pop,log,hof=main(30,pop)
