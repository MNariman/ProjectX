import numpy as np

#--COMMUNITY--
#Quality of communities
#Number of communities
#Size of the smallest community 
#Size of the largest community
#Size of the average community 

#--TIME--
#Time spent in core algorithm for community detection from Adjacency matrix
#Time spent in performance evaluation

#--PERFORMANCE--
#Success rate/ only if the test dataset is generated by "BENCHMARK GN"


def print_community_stat(community_pool):
	size_array=[]
	for community in community_pool:
		size=len(community.members)
		size_array.append(size)
	sorted_array=sorted(size_array)

	line1= "Size of the Smallest Community: {}\n".format(sorted_array[0])
	line2= "Size of the Largest Community: {}\n".format(sorted_array[-1])
	line3= "Size of the Average Community: {}\n".format( sum(sorted_array)/len(sorted_array) )
	return line1+line2+line3

def data_characteristics(A,section_name):
	total_node=len(A)
	total_edge=np.sum(A)/2
	average_degree=2*total_edge/total_node # is integer

	line1= "\n---Data Characteristics---\n"
	line2= "---{}---\n".format(section_name)
	line3= "--------------------------\n"
	line4= "Total Node Number: {}\n".format(total_node)
	line5= "Total Edge Number: {}\n".format(total_edge)
	line6= "Average Degree per Node: {}\n".format(average_degree)
	line7= "----------END-------------\n"

	with open("statistics.txt", 'a') as file:
		file.write( line1+line2+line3+line4+line5+line6+line7 )



def dir_data_characteristics(dir_A,section_name):

	node_number=len(dir_A)
	edge_number=np.sum(dir_A)
	average_degree=edge_number/node_number
	min_out_degree=np.min(np.sum(dir_A, axis=1))
	max_out_degree=np.max(np.sum(dir_A, axis=1))
	min_in_degree=np.min(np.sum(dir_A, axis=0))
	max_in_degree=np.max(np.sum(dir_A, axis=0))

	line1= "\n---Data Characteristics---\n"
	line2= "---{}---\n".format(section_name)
	line3= "Total Node Number: {}\n".format(node_number)
	line4= "Total Edge Number: {}\n".format(edge_number)
	line5= "Average Degree per Node: {}\n".format(average_degree)
	line6= "Min Out Degree: {}\n".format(min_out_degree)
	line7= "Max Out Degree: {}\n".format(max_out_degree)
	line8= "Min In Degree: {}\n".format(min_in_degree)
	line9= "Max In Degree: {}\n".format(max_in_degree)
	line10= "-------------END---------\n"

	with open("statistics.txt", 'a') as file:
		file.write( line1+line2+line3+line4+line5+line6+line7+line8+line9+line10 )


def print_community_statistics(Qmax,community_pool, section_name):
	line1= "\n---Community Statistics---\n"
	line2= "---{}---\n".format(section_name)
	line3= "--------------------------\n"
	line4= "Quality Factor: {}\n".format(Qmax)
	line5= "Total Number of Communities: {}\n".format(len(community_pool))
	line6= print_community_stat(community_pool)
	line7= "---------\n"
	line8= "---END---\n"

	with open("statistics.txt", 'a') as file:
		file.write( line1+line2+line3+line4+line5+line6+line7+line8 )

