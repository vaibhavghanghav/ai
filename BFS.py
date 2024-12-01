#This function will visit all nodes of graph using bfs traversal
def bfs_connected_component(graph,start):
	explored=[]  #keep track of all visited nodes
	queue=[start]  #keep track of nodes to be check
	
	while queue:  #keep looping until their are nodes still to be check
		node=queue.pop(0)  #pop shallowest node/first node from queue
		
		if node not in explored:
			explored.append(node)  #add node to list of checked nodes
			neighbours=graph[node]  
			
			for neighbour in neighbours:
				queue.append(neighbour)
	return explored

#this function will find the shortest path between two nodes of a graph using bfs
def bfs_shortest_path(graph,start,goal):
	explored=[]
	queue=[[start]]
	
	if start==goal:
		return "That was easy because the start node is goal node"
	
	while queue:
		path=queue.pop(0)  #pop the first path from the queue
		node=path[-1]  #it will return last node from the path

		if node not in explored:
			neighbours=graph[node]
			#go through all neighbour nodes, construct a new path and push it into the queue

			for neighbour in neighbours:
				new_path=list(path)
				new_path.append(neighbour)
				queue.append(new_path)

				if neighbour==goal:
					return new_path  #return path if neighbour is the goal node
			
			explored.append(node)    #mark node as explored
			
	return "Path does not exist"	#in case if there is no path between the two nodes
	
if _name=='main_':
	graph={'A':['B','C'], 'B':['A','D'], 'C':['A','E','F'], 'D':['B'], 'E':['C'], 'F':['C']}
	print("Here are the nodes of the graph visited by BFS starting from node A: ",bfs_connected_component(graph,'A'))
	print("Here is the shortest path between nodes D and E: ",bfs_shortest_path(graph,'D','E'))
