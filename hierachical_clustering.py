from math import sqrt

def readfile(filename):
	line = [line for line in file(filename)]

	colnames = line[0].strip().split('\t')[1:]

	rownames = []
	data = []
	for l in line[1:]:
		p = l.strip().split('\t')
		rownames.append(p[0])
		data.append([float(x) for x in p[1:]])

	return rownames, colnames, data


def distance_pearson(data1, data2):

	sum1 = sum(data1)
	sum2 = sum(data2)

	sum1Sq = sum(pow(i,2) for i in data1)
	sum2Sq = sum(pow(j,2) for j in data2)
	pSum = sum(data1[i] * data2[i] for i in range(len(data1)))

	n = len(data1)
	num = pSum - (sum1*sum2)/n
	den = sqrt((sum1Sq - pow(sum1, 2)/n)*(sum2Sq - pow(sum2,2)/n))
	if den == 0: return 0

	r = num/den

	return 1-r


class bicluster:
	def __init__(self, vec, left=None, right = None, distance = 0.0, id = None):
		self.vec = vec
		self.left = left
		self.right = right
		self.id = id
		self.distance = distance

rownames, colnames, data = readfile('blogdata.txt')

#print len(rownames)

def hierachical_cluster(rows, distance = distance_pearson):
	# import numpy as np
	# num_cluster = len(rows)
	# distance_arr = np.zeros([len(rows),len(rows)])
	# for i in len(rows):
	# 	for j in len(rows):
	# 		if ( i < j):
	# 			distance_arr[i,j] = distance(i,j)

	# cluster = []

	# while (num_cluster > 1):
	# 	idx1,idx2 = np.where(distance_arr == min(distance_arr))
	# 	rows[idx1] =  (rows[idx1] +rows[idx2])/2
	# 	cluster.append([idx1, idx2])
	# 	rows.drop(rows[idx2])
	# 	num_cluster -= 1

	distances = {}
	current_id = -1
	cluster = [bicluster(rows[i],id = i) for i in range(len(rows))]
	
	while (len(cluster) > 1):
		min_pair = (0,1)
		min_distance = distance_pearson(cluster[0].vec, cluster[1].vec)

		for i in range(len(cluster)):
			for j in range(i+1, len(cluster)):
				if (cluster[i].id, cluster[j].id) not in distances:
					distances[(cluster[i].id,cluster[j].id)] = distance_pearson(cluster[i].vec,cluster[j].vec)

				if distances[(cluster[i].id,cluster[j].id)] < min_distance:
					min_distance = distances[(cluster[i].id,cluster[j].id)]
					min_pair = (i,j)
					
		merged_row = [(cluster[min_pair[0]].vec[k] + cluster[min_pair[1]].vec[k])/2 for k in range(len(cluster[0].vec))]
		current_cluster = bicluster(merged_row, left = cluster[min_pair[0]], right=cluster[min_pair[1]], distance = min_distance, id = current_id)
		print min_pair[0]
		print min_pair[1]
		del cluster[min_pair[1]]
		del cluster[min_pair[0]]
		cluster.append(current_cluster)
		current_id -= 1

	return cluster[0]

def printclust(clust,labels=None,n=0):
  # indent to make a hierarchy layout
  for i in range(n): print ' ',
  if clust.id<0:
    # negative id means that this is branch
    print '-'
  else:
    # positive id means that this is an endpoint
    if labels==None: print clust.id
    else: print labels[clust.id]

  # now print the right and left branches
  if clust.left!=None: printclust(clust.left,labels=labels,n=n+1)
  if clust.right!=None: printclust(clust.right,labels=labels,n=n+1)


def distance_tanimoto(data1, data2):
	num = sum([data1[i]* data2[i] for i in range(len(data1))])
	dem = sum([ (data1[i] ==1) | (data2[i]== 1 ) for i in range(len(data1))])

	distance = num/dem
	return 1-distance



    # Move the centroids to the average of their members
    for i in range(k):
      avgs=[0.0]*len(rows[0])
      if len(bestmatches[i])>0:
        for rowid in bestmatches[i]:
          for m in range(len(rows[rowid])):
            avgs[m]+=rows[rowid][m]
        for j in range(len(avgs)):
          avgs[j]/=len(bestmatches[i])
        clusters[i]=avgs
      
  return bestmatches


blognames, words, data = readfile('blogdata.txt')
cluster = hierachical_cluster(data)
printclust(cluster, labels = blognames)
					



