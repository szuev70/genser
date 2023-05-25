#!/usr/bin/env python
# coding: utf-8

from copy import copy

def dim_step_down(data,powers): # powers is dictionary in form {n1:N1,n2:N2}, features are unified in n1
    newdata = []
    n1, n2 = tuple(powers.keys())
    for d in data:
        nd = [di if i not in [n1,n2] else d[n1] + powers[n1]*d[n2] for i,di in enumerate(d) if i!= n2]
        newdata.append(nd)
    return newdata
def dim_step_up(data, powers): # powers is dictionary in form {n1:N,n2:N2}, the feature n1 is devided onto n1 of power N1 = N/N2 and n2 of power N2  
    n = len(data[0])
    n1, n2 = tuple(powers.keys())
    N, N2 = tuple(powers.values())
    N1 = int(N/N2)+1 if N/N2 - int(N/N2) else int(N/N2)  
    if N<4:
        return data
    else:
        newdata = []
    # possibilities: n1<n2 and n2<=n-1; n1<n2 and n2=n
    # n1>n2 and n1<n-1; n1>n2 and n1=n-1
        if n1<n2:
            if n2<n:
                for d in data:
                    nd = d[:n1] + [d[n1]%N1] + d[n1+1:n2] + [d[n1]//N1]+d[n2:]
                    newdata.append(nd)
            elif n2 == n:
                for d in data:
                    nd = d[:n1] + [d[n1]%N1] + d[n1+1:] + [d[n1]//N1]
                    newdata.append(nd)
            else:
                newdata = copy(data)
        elif n1<n+1:
            if n1 == n:
                n1 = n-1
            for d in data:
                nd = d[:n2] + [d[n1]//N1] + d[n2:n1] + [d[n1]%N1] + (d[n1+1:] if n1 < n-1 else [])
                newdata.append(nd)
        else:
            newdata = copy(data)
    return newdata 

def transform_to(data, m): # every step will be made with most appropriate features and saving the information 
    n = len(data[0])
    newdata = copy(data)
    story = []
    if m<n:
        for k in range(n,m,-1):
            powers = {i: max([d[i] for d in newdata])+1 for i in range(k)} 
            powers = dict(sorted(powers.items(), key=lambda item: item[1])[:2])
            newdata = dim_step_down(newdata,powers)
            story.append(powers)
    else:
        for k in range(n,m):
            powers = {i: max([d[i] for d in newdata])+1 for i in range(k)} 
            powers = dict(sorted(powers.items(), key=lambda item: item[1], reverse = True)[:1])
            B = sorted(powers.items(), key=lambda item: item[1], reverse = True)[0][1]
            if B<4:
                break
            powers[k] = int((list(powers.values())[0])**(1/2))
            newdata = dim_step_up(newdata,powers)
            story.append(powers)
    return newdata, story

def transform_out_down(data, story): # inverse transform_to downsteps
    n = len(data[0])
    m = n-len(story)
    newdata = copy(data)
    restore = list(reversed(story))
    for k in range(n,m,-1):
        powers = restore[k-n]
        N, N2 = list(powers.items())[0][1],list(powers.items())[1][1]
        N1 = int(N/N2)+1 if N/N2 - int(N/N2) else int(N/N2)
        if N<4:
            break
        powers[list(powers.items())[0][0]] = N1
        newdata = dim_step_down(newdata,powers)
    return newdata
def transform_out_up(data, story): # inverse transform_to upsteps
    n = len(data[0])
    m = n+len(story)
    newdata = copy(data)
    restore = list(reversed(story))
    for k in range(n,m):
        powers = restore[n-k]
        N1, N2 = list(powers.items())[0][1],list(powers.items())[1][1]
        N = N1*N2
        powers[list(powers.items())[0][0]] = N
        newdata = dim_step_up(newdata,powers)
    return newdata
