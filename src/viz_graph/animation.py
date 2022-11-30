import networkx as nx 
import matplotlib.pyplot as plt
#from viz_graph.graph import Graph
from viz_graph.graph import Graph 
from viz_graph.search import search 
from collections import defaultdict
#from viz_graph.search import search 
from matplotlib.animation import FuncAnimation
import yaml 
from yaml.loader import SafeLoader


def get_pseudo_text(file_name):
    # read text file 
    file = open(file_name)
    code_array = [row.strip("\n") for row in file.readlines()]
    string = "\n".join(code_array)
    return code_array 
        

def get_config(yml_file_name):
    with open(yml_file_name) as f:
        config = yaml.load(f, Loader=SafeLoader)
    return config 


def get_line_color_for_loop(mode, line_id, config, type):
    for iter_num, list_of_rows in config.items():
        if (line_id in list_of_rows) and (mode==iter_num):
            return 1
    return 0
    

def format_text(annotation, lst):
    texts = []
    n = 6 
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield ", ".join([str([j for j in lst[i:i + n]])])  

    text = ",\n ".join([t for t in chunks(lst, n)])

    return '{}: {}'.format(annotation, text)


def animation_search_algo(graph_input, start, end, algo_name):
    fig, ax = plt.subplots(nrows=1, ncols=2,
                           gridspec_kw={"width_ratios": [1.5,1]})
    plt.xticks([])
    plt.yticks([])
    plt.subplots_adjust(
            left=0.02, 
            right=0.98, 
            top=0.98, 
            bottom=0.02,
            wspace=0.02)

    
    font_size = 8.5
    graph = Graph()
    graph.create_from_graph(graph_input)
    pos = nx.get_node_attributes(graph, "pos")
 
    (traveled_path, 
     traveled_dict,
     traveled_edges, 
     shortest_path, 
     shorted_path_edges, 
     total_cost, queues) = search(graph, start, end, algo_name)

    text = get_pseudo_text("src/viz_graph/text/{}.txt".format(algo_name))
    text_config = get_config("src/viz_graph/text/{}.yml".format(algo_name))
     
    # these lines is to calcuate the line to show "pop from queue"
    number_of_config_line = 2

    ncf = number_of_config_line

    traveled_loop = sum([len(nei)+1 for node, nei in traveled_dict.items()])*ncf
    #print(traveled_dict)
    #print(traveled_edges)


    def index_mapping():
        reindex_mapping = defaultdict()
        reindex_mapping_traedgex = defaultdict()
        reindex_node_mapping = defaultdict()

        parent_nodeid_mapping = defaultdict() #mapping to node in insteed of index 
        parent_nodes = [] 
        visited_indexs = defaultdict() 

        loop_idx=-1
        new_node_idx=0
        new_edge_idx=0
        prev_node_id=0

        for parent_node, nei_list in traveled_dict.items():
            
           
            loop_idx+=1

            new_node_idx+=0 #just to remind 
            new_edge_idx+=0 

            reindex_mapping[loop_idx]=prev_node_id
            parent_nodes.append(loop_idx) #node_is parent 
            parent_nodeid_mapping[loop_idx]=parent_node 

            for nei in nei_list:
                    loop_idx+=1
                    new_node_idx+=1
                    prev_node_id=new_node_idx 

                    reindex_mapping[loop_idx]=new_node_idx
                    parent_nodeid_mapping[loop_idx]=parent_node


        return (reindex_mapping, 
                parent_nodes, 
                parent_nodeid_mapping, 
                visited_indexs) 

    (reindex_mapping, 
     parents, 
     parent_nodeid_mapping, 
     visited_indexs) = index_mapping()
     
    #print("preindex_mapping", reindex_mapping)
    path_loop = (len(shortest_path)) 
    visited = [k for k,v in traveled_dict.items()]
    
#    print("reind", reindex_mapping)
#    print("traveled_dict", traveled_dict)
#    print("traveled_path", traveled_path)
#
#    print(len(traveled_path))
#    print("traveled_edges", traveled_edges)
#    print(len(traveled_edges))
#    print("reindex_id_mapping", reindex_mapping)
#    print("parent_node_mapping:", parent_nodeid_mapping)
    def animation_frame(loop_id):
        ax_left = ax[0] 
        ax_left.clear()
        ax_left.axis("off")

        #show text
        ax_right = ax[1]
        ax_right.clear()
        ax_right.axis("off")
        ax_right.invert_yaxis()
       
        if loop_id < traveled_loop:
            fid = loop_id
            iid_big_loop = fid // ncf

            id_in_traveled_path = reindex_mapping[iid_big_loop]
            mode =  fid % ncf
            #print("loop_id", loop_id, "mode", mode, "iid",iid, "i", i)
            

            nx.draw_networkx(graph, 
                             pos = pos, 
                             node_size=200, 
                             node_color="tab:gray",
                             style="dashed", 
                             edge_color='gray', 
                             width=.5, 
                             alpha=.5,
                             ax=ax_left,
                             font_size=8,
                             )
            nx.draw_networkx_nodes(
                        graph, 
                        pos=pos, 
                        nodelist=[start], 
                        node_color="#F3896F",
                        node_size=350,
                        ax=ax_left,
                        )
            nx.draw_networkx_nodes(
                        graph, 
                        pos=pos, 
                        nodelist=[end], 
                        node_color="#F3896F",
                        node_size=350,
                        ax=ax_left,
                        )
            labels={}
            labels[start]=r"Start"
            labels[end]=r"End"
            nx.draw_networkx_labels(graph, pos, labels, font_size=10, font_color="whitesmoke")


            #print(loop_id, traveled_edges[:id_in_traveled_path-1],"--id", id_in_traveled_path)
            #print(loop_id, traveled_path[:id_in_traveled_path])
            nx.draw_networkx_nodes(graph, 
                                   pos=pos,
                                   nodelist=traveled_path[:id_in_traveled_path+1], 
                                   node_color="#FFC300", 
                                   node_size=250,
                                   alpha=0.8,
                                   ax=ax_left
                                   )
                                    
            # SHOW PARENT NODE 
            nx.draw_networkx_nodes(
                        graph, 
                        pos=pos, 
                        nodelist=[parent_nodeid_mapping[iid_big_loop]], 
                        # alway highlight parent node
                        node_color="#785303",
                        node_size=300,
                        ax=ax_left,
                        linewidths=2, 
                        edgecolors="#785303",
                        )
            # SHOW EDGES 
            if id_in_traveled_path >0 and id_in_traveled_path<len(traveled_path): 
                nx.draw_networkx_edges(graph, 
                                   pos,
                                   edgelist = traveled_edges[:id_in_traveled_path], 
                                   edge_color="#FFC300",
                                   width=1,
                                   alpha=1,
                                   style="solid", 
                                   ax=ax_left) 
#                print("oldId", iid_big_loop, "newId", id_in_traveled_path, 
#                      "node", traveled_path[id_in_traveled_path],
#                      "edge",  traveled_edges[id_in_traveled_path-1],
#                      "parent", parent_nodeid_mapping[iid_big_loop], 
#                      "Show -parent_text", iid_big_loop in parents
#                      )

            #print Visited and Queue 
            ax_right.text(
                    0,
                    0.7,
                    format_text("visitied", traveled_path[:id_in_traveled_path+1]), 
                    )

            if id_in_traveled_path!=None:
                ax_right.text(
                    0,
                    0.8,
                    format_text("queue", queues[iid_big_loop]), 
                    )       

            for line_id, line in enumerate(text):
                #enqueue and while loop: 
                if iid_big_loop in parents: 
                    color = get_line_color_for_loop(
                            mode,
                            line_id, 
                            text_config['enqueue_and_while'],
                            algo_name)
                    #if color==1:
                        #print("enqueue", line_id, mode, loop_id, "real_loop", i)

                
                # loop and adding neighbor 
                else: 
                    color=get_line_color_for_loop(
                            mode, 
                            line_id, 
                            text_config['loop'], 
                            algo_name)
                if color==1:
                    ax_right.text(
                        0,
                        1-line_id*0.031, 
                        line,
                        color ="#FFC300", 
                        fontweight='bold',
                        size = font_size,
                        va="center",
                        ha="left",
                        transform=ax_right.transAxes)
                else:
                    ax_right.text(
                        0,
                        1-line_id*0.03, 
                        line, 
                        color ="black", 
                        size = font_size,
                        va="top",
                        ha="left",
                        transform=ax_right.transAxes) 
            
                 
            
        else:
            n = loop_id - traveled_loop + 1 
            nx.draw_networkx(graph, 
                             pos = pos, 
                             node_size=200, 
                             node_color="tab:gray",
                             style="dashed", 
                             edge_color='gray', 
                             width=.5, 
                             alpha=.5,
                             ax=ax_left,
                             font_size=8,
                             )
            nx.draw_networkx_nodes(
                        graph, 
                        pos=pos, 
                        nodelist=shortest_path[:n],
                        node_color="#F3896F",
                        node_size=300,
                        ax=ax_left,
                        )
            nx.draw_networkx_edges(graph, 
                                   pos,
                                   edgelist = shorted_path_edges[:n], 
                                   edge_color="#F3896F", 
                                   width=1,
                                   alpha=1,
                                   style="solid", 
                                   ax=ax_left, 
                                    ) 
            ax_right.text(
                    0,
                    0.5, 
                    format_text(
                        "Shortest path from {} to {} is\n".format(start, end), 
                        shortest_path)
                    )
            ax_right.text(
                    0,
                    0.7, 
                    "Total Cost:{}".format(total_cost)
                    )

    anim = FuncAnimation(
            fig, 
            animation_frame, 
            frames=traveled_loop+path_loop, 
            interval = 300, 
            repeat=False 
            )
    #plt.show()
    return anim 
   

if __name__=="__main__":
    G = nx.gnp_random_graph(15, 0.3, seed=123)
    start = 1
    end =  6


    animation_search_algo(G, int(start), int(end), "gbfs")


