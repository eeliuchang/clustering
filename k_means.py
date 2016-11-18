def k_means(rows, distance = distance_pearson, k=4):

	# converged = False
	# last_clusters = {}
	# last_clusters.keys() = rows[:k]

	# while not converge:
	# 	current_clusters = {}
	# 	for i in range(len(rows)):
	# 		belong_to_centroid_row = last_clusters.keys()[0]
	# 		min_distance = distance(belong_to_centroid_row, rows[i])

	# 		for j in range(k):
	# 			if (distance(last_clusters.keys()[j], rows[i])< min_dstance):
	# 				belong_to_centroid_row = j
	# 				min_distance = distance(last_clusters.keys()[j], rows[i])

	# 		last_clusters[belong_to_centroid_row].append(rows[i])

	# 	for j in range(k):
	# 		current_clusters.keys()[j] = sum(current_clusters[current_clusters.keys()[j]])/len(current_clusters[current_clusters.keys()[j]])


	# 	if last_clusters.keys() == current_clusters.keys():
	# 		converged = True

	# return current_clusters
# Determine the minimum and maximum values for each point
  ranges=[(min([row[i] for row in rows]),max([row[i] for row in rows])) 
  for i in range(len(rows[0]))]

  # Create k randomly placed centroids
  clusters=[[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0] 
  for i in range(len(rows[0]))] for j in range(k)]
  
  lastmatches=None
  for t in range(100):
    print 'Iteration %d' % t
    bestmatches=[[] for i in range(k)]
    
    # Find which centroid is the closest for each row
    for j in range(len(rows)):
      row=rows[j]
      bestmatch=0
      for i in range(k):
        d=distance(clusters[i],row)
        if d<distance(clusters[bestmatch],row): bestmatch=i
      bestmatches[bestmatch].append(j)

    # If the results are the same as last time, this is complete
    if bestmatches==lastmatches: break
    lastmatches=bestmatches
    