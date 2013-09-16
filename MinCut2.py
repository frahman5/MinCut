from random import sample
import math

def getVertices(location):
    """
    Produces an adjacency list representation of an undirected Graph
    """
    answer = []
    line_number = 0
    with open(location,encoding = 'utf-8') as file:
        for a_line in file:
            if "\n" in a_line:
                edited_line = a_line[:len(a_line)-1]
            else:
                edited_line = a_line
            edited_line = edited_line.replace('\t',' ')
            edited_line = edited_line.split()
            edited_line.pop(0)
            answer.append(edited_line)
            line_number += 1
    return answer

def getEdges(G):
    """
    produces a list of all the edges in a undirected graph
    that has no parallel edges
    ListofLists -> ListofSets
    """
    answer = []
    for i in range(0,len(G)):
        for j in G[i]:
            if int(j) > i:
                answer.append(set((i+1,int(j))))
            else:
                continue
    return answer

def remove_all(L,e):
    """
    ListofX X -> None
    To remove all instances of element e in L (in place. i.e., edits the given list. Does
    not create a new list
    """
    for i in range(0,len(L)):
        if e in L:
            L.remove(e)
        else:
            break

def minCut(G,E):
    """
    ListOfLists ListOfSets -> Integer[>=0]
    
    Given two adjacency lists, one from vertices to edges
    and one from edges to vertices, produces the number
    of crossings in the mincut of the graph
    """
    x = len(G)
    step = 0
    while step < x - 2:
        step += 1
        to_contract = sample(E,1)
        bbv,nv = min(to_contract[0]),max(to_contract[0])    #bbv = bye_bye_vertex nv = new vertex
        remove_all(E,to_contract[0])                        #to remove all instances of the contracted edge in E
        to_add = G.pop(bbv-1)                               #get a list of the perished vertex's edges, remove it from G
        G.insert(bbv-1,1)                                   #put a placeholder where the vertex used to be, to maintain indexing
        remove_all(to_add,str(nv))                          #get rid of self loops, because they are wack
        G[nv-1].extend(to_add)                              #add the perished edges to the new dual-vertex
        remove_all(G[nv-1],str(bbv))                        #get rid of all references to the old vertex in the new vertex
        for i in range(0,x):
            if type(G[i]) == list:
                loop3_num = 0
                while loop3_num < len(G[i]):
                    if str(bbv) in G[i]:
                        G[i].remove(str(bbv))
                        G[i].append(str(nv))
                        loop3_num += 1
                    else:
                        break                   
        for v in to_add:
            E.append(set((nv,int(v))))
            E.remove(set((bbv,int(v))))
    return len(E)
            
def main(text):
    """
    Text -> Integer[>=0}

    Given as input a text file which represents a graph,
    outputs the number of crossings in the minCut of the corresponding graph
    """
    answer = len(getVertices(text))                         #initializing the answer at an absurdly large number
    x = answer
    limit = math.floor(x*math.log(x,math.e))
    for i in range(0,limit):
        G = getVertices(text)
        E = getEdges(G)
        maybe_answer = minCut(G,E)
        answer = min(answer,maybe_answer)
    return answer

