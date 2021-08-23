import sys
import ast
my_path = "C:\\Users\\Michael\\Desktop\\wyf\\intern\\connected_graph"
sys.path.append(my_path)
import functions as functions


file = open(r"C:\Users\Michael\Desktop\wyf\intern\connected_graph\connected_graph.txt")
contents = file.read()
link_list = ast.literal_eval(contents)
file.close()
# link_list={"1":["2","3"],"2":["1","3"], "3":["1", "2", "4" ], "4":["3"]} #This is a connected graph for test
#link_list={"1":["2","3"],"2":["1","3"], "3":["1", "2", "4" ], "4":["3"], "5":["6"], "6":["5"]} #unconnected graph
 
unvisited_list=functions.create_unvisited_list(link_list)
# stack=functions.create_unvisited_node(unvisited_list)
stack={}
# print("link list: "+str(link_list))
# print(list(link_list.keys())[0])
# print("univisted list  "+str(unvisited_list))
# print(link_list["1"])
# for ele in link_list["1"]:
#     unvisited_list.remove(ele)
# unvisited_list.remove(list(link_list.keys())[0]) # remove the start node from the unvisited node list
# print("unvisited node list: "+str(unvisited_list))
stack[list(link_list.keys())[0]]=0 #assign the first node in stack the 0 value
# stack[list(link_list.keys())[1]]=1 #test
# print("stack:"+ str(stack))

c=-1
null_value=0
while True:
    if null_value in stack.values():
        # print("Yes")
        if stack[list(stack)[c]]==0: #if the last element has a null_value
            # print("Y")
            stack[list(stack)[c]]=1
            # print(list(stack)[c])
            for ele in link_list[list(stack)[c]]:
                if ele in unvisited_list:
                    unvisited_list.remove(ele)
                    stack[ele]=0
            print("unvisited node list: "+ str(unvisited_list))
            print("stack_new "+str(stack))           
        else:
            # print("N")
            c=c-1 
    else:
        if len(unvisited_list):
            print("The graph is not connected.")
        else:
            print("The graph is connected.")
        break
       
