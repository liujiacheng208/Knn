import  numpy as np
import operator
def DataSet():
    group=np.array([[1,100],[3,100],[0,0],[100,100],[99,5],[50,50]])
    labels=['死宅','死宅','死宅','现充','现充','正常人']
    return group,labels
def KNN(in_x,x_labels,y_labels,k):
    in_x=np.array(in_x).reshape(1,-1)
    distances=np.sqrt(((in_x-x_labels)**2).sum(axis=1))
    ed_distances=np.argsort(distances)
    classdict={}
    for i in range(k):
        voteI_laber=y_labels[ed_distances[i]]
        classdict[voteI_laber]=classdict.get(voteI_laber,0)+1
    sort_classdict=sorted(classdict.items())
    return sort_classdict[-1][0]

if __name__=='__main__':
    group,labels=DataSet()
    test_x=[80,22]
    print("输入：{}".format(KNN(test_x, group, labels, 3)))