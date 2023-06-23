import pandas as pd
from sklearn.model_selection import train_test_split
from  sklearn import preprocessing
import numpy as np
from queue import PriorityQueue
import datetime 
import random
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
import mysql.connector

best_route_cost = 0
best_route = ''
best_route_dir = ''

def backend() :
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'cse_404'
    }

    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()


    traffic_data = pd.read_csv('/home/rafi/cse404/project/traffic_dataset.csv')

    X=traffic_data.drop(columns=['traffic_indicator'])
    Y=traffic_data['traffic_indicator']

    le=preprocessing.LabelEncoder()

    encoded_location = le.fit_transform(traffic_data['location'])
    encoded_month = le.fit_transform(traffic_data['month'])
    encoded_day = le.fit_transform(traffic_data['day'])
    encoded_date = le.fit_transform(traffic_data['date'])
    encoded_time_block = le.fit_transform(traffic_data['time_block'])
    encoded_weather = le.fit_transform(traffic_data['weather'])
    encoded_traffic_indicator = le.fit_transform(traffic_data['traffic_indicator'])

    X = np.array(list(zip(encoded_location, encoded_month, encoded_day, encoded_date, encoded_time_block, encoded_weather)))
    Y = encoded_traffic_indicator

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

    model = HistGradientBoostingRegressor()

    model.fit(X_train, Y_train)

    contigency = [1, 2, 3]
    con = lambda : random.choice(contigency)

    query = "SELECT * FROM i_values"
    cursor.execute(query)

    rows = cursor.fetchall()

    custom_values = [x for x in rows[len(rows)-1] ]

    full_date = custom_values[1].split('-')

    custom_date = full_date[2]
    custom_month = full_date[1]
    custom_year = full_date[0]

    month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    custom_month = month[int(custom_month)]

    full_time = custom_values[2].split(':')

    custom_time_zone = full_time[0]+full_time[1]

    if '0000' <= custom_time_zone < '0400' :
        custom_time_block = 'a'
    elif '0400' <= custom_time_zone < '0800' :
        custom_time_block = 'b'
    elif '0800' <= custom_time_zone < '1200' :
        custom_time_block = 'c'
    elif '1200' <= custom_time_zone < '1600' :
        custom_time_block = 'd'
    elif '1600' <= custom_time_zone < '1800' :
        custom_time_block = 'e'
    elif '1800' <= custom_time_zone < '2400' :
        custom_time_block = 'f'
        
    custom_day_find = custom_date+' '+custom_month+' '+custom_year
    day_name= ['mon', 'tue', 'wed', 'thu', 'fri', 'sat','sun']
    custom_day = datetime.datetime.strptime(custom_day_find, '%d %b %Y').weekday()
    custom_day = day_name[custom_day]

    if custom_month in ['nov', 'dec', 'jan', 'feb'] :
        custom_weather = 2
    elif custom_month in ['jul', 'aug', 'sep', 'oct'] :
        custom_weather = 3
    else :
        custom_weather = 1
        
    custom_data = pd.read_csv('/home/rafi/cse404/project/custom_input.csv')
        
    custom_data_input = pd.DataFrame([['mirpur_10', custom_month, custom_day, custom_date, custom_time_block, custom_weather ], 
                        ['mirpur_11', custom_month, custom_day, custom_date, custom_time_block, custom_weather ],
                        ['mirpur_12', custom_month, custom_day, custom_date, custom_time_block, custom_weather ],
                        ['mirpur_14', custom_month, custom_day, custom_date, custom_time_block, custom_weather ],
                        ['bijoy_shoroni', custom_month, custom_day, custom_date, custom_time_block, custom_weather ],
                        ['cantonment', custom_month, custom_day, custom_date, custom_time_block, custom_weather ],
                        ['jahangir_gate', custom_month, custom_day, custom_date, custom_time_block, custom_weather ],
                        ['kalshi', custom_month, custom_day, custom_date, custom_time_block, custom_weather ],
                        ['begum_rokeya', custom_month, custom_day, custom_date, custom_time_block, custom_weather ],
                        ['matikata', custom_month, custom_day, custom_date, custom_time_block, custom_weather ]], 
                        columns=['location', 'month', 'day', 'date', 'time_block', 'weather'])
    custom_data_input.to_csv('custom_input.csv', index=False)

    custom_encoded_location = le.fit_transform(custom_data['location'])
    custom_encoded_month = le.fit_transform(custom_data['month'])
    custom_encoded_day = le.fit_transform(custom_data['day'])
    custom_encoded_date = le.fit_transform(custom_data['date'])
    custom_encoded_time_block = le.fit_transform(custom_data['time_block'])
    custom_encoded_weather = le.fit_transform(custom_data['weather'])

    C = np.array(list(zip(custom_encoded_location, custom_encoded_month, custom_encoded_day, custom_encoded_date, custom_encoded_time_block, custom_encoded_weather)))

    prediction = model.predict(C)



    class Node(object):
        """This class represents a node in a graph."""
        
        def __init__(self, label: str=None):
            """
            Initialize a new node.
            
            Args:
                label: the string identifier for the node
            """
            self.label = label
            self.children = []
            
        def __lt__(self,other):
            """
            Perform the less than operation (self < other).
            
            Args:
                other: the other Node to compare to
            """
            return (self.label < other.label)
        
        def __gt__(self,other):
            """
            Perform the greater than operation (self > other).
            
            Args:
                other: the other Node to compare to
            """
            return (self.label > other.label)
        
        def __repr__(self):
            """Return a string form of this node."""
            return '{} -> {}'.format(self.label, self.children)
        
        def add_child(self, node, cost=1):
            """
            Add a child node to this node.
            
            Args:
                node: the node to add to the children
                cost: the cost of the edge (default 1)
            """
            edge = Edge(self, node, cost)
            self.children.append(edge)
        
        
    class Edge(object):
        """This class represents an edge in a graph."""
        
        def __init__(self, source: Node, destination: Node, cost: int=1):
            """
            Initialize a new edge.
            
            Args:
                source: the source of the edge
                destination: the destination of the edge
                cost: the cost of the edge (default 1)
            """
            self.source = source
            self.destination = destination
            self.cost = cost
        
        def __repr__(self):
            """Return a string form of this edge."""
            return '{}: {}'.format(self.cost, self.destination.label)
        
    def ucs(root, goal):
        """
        Return the uniform cost search path from root to gaol.
        
        Args:
            root: the starting node for the search
            goal: the goal node for the search
            
        Returns: a list with the path from root to goal
        
        Raises: ValueError if goal isn't in the graph
        """
        # create a priority queue of paths
        queue = PriorityQueue()
        queue.put((0, [root]))
        # iterate over the items in the queue
        while not queue.empty():
            # get the highest priority item
            pair = queue.get()
            current = pair[1][-1]
            # if it's the goal, return
            if current.label == goal:
                return pair[1]
            # add all the edges to the priority queue
            for edge in current.children:
                # create a new path with the node from the edge
                new_path = list(pair[1])
                new_path.append(edge.destination)
                # append the new path to the queue with the edges priority
                queue.put((pair[0] + edge.cost, new_path))
                
    ECB = Node('ECB')
    CANTONMENT = Node('CANTONMENT')
    MATIKATA = Node('MATIKATA')
    KALSHI = Node('KALSHI')
    MIRPUR_12 = Node('MIRPUR_12')
    JAHANGIR_GATE = Node('JAHANGIR_GATE')
    MIRPUR_14 = Node('MIRPUR_14')
    MIRPUR_10 = Node('MIRPUR_10')
    MIRPUR_11 = Node('MIRPUR_11')
    BIJOY_SHARANI = Node('BIJOY_SHARANI')
    BEGUM_ROKEYA = Node('BEGUM_ROKEYA')
    AGARGAON = Node('AGARGAON')

    ECB.add_child(CANTONMENT, prediction[5]+0)
    ECB.add_child(MATIKATA, prediction[9]+0)
    ECB.add_child(KALSHI, prediction[7]+0)
    ECB.add_child(MIRPUR_12, prediction[2]+0)

    CANTONMENT.add_child(JAHANGIR_GATE, con()*prediction[6]+con()*prediction[5])

    MATIKATA.add_child(MIRPUR_14, con()*prediction[3]+con()*prediction[9])

    KALSHI.add_child(MIRPUR_11, con()*prediction[1]+con()*prediction[7])

    MIRPUR_12.add_child(MIRPUR_11, con()*prediction[1]+con()*prediction[2])

    JAHANGIR_GATE.add_child(BIJOY_SHARANI, con()*prediction[4]+con()*prediction[6])
    JAHANGIR_GATE.add_child(MIRPUR_14, con()*prediction[3]+con()*prediction[6])

    MIRPUR_11.add_child(MIRPUR_10, con()*prediction[0]+con()*prediction[1])

    MIRPUR_10.add_child(MIRPUR_14, con()*prediction[3]+con()*prediction[0])

    MIRPUR_14.add_child(MIRPUR_10, con()*prediction[0]+con()*prediction[3])
    MIRPUR_14.add_child(JAHANGIR_GATE, con()*prediction[6]+con()*prediction[3])

    BIJOY_SHARANI.add_child(BEGUM_ROKEYA, con()*prediction[8]+con()*prediction[4])

    MIRPUR_10.add_child(BEGUM_ROKEYA, con()*prediction[8]+con()*prediction[0])

    BEGUM_ROKEYA.add_child(AGARGAON, 0+con()*prediction[8])

    route_A = ['ECB', 'CANTONMENT', 'JAHANGIR_GATE', 'BIJOY_SHARANI', 'BEGUM_ROKEYA', 'AGARGAON']
    route_B = ['ECB', 'MATIKATA', 'MIRPUR_14', 'JAHANGIR_GATE', 'BIJOY_SHARANI', 'BEGUM_ROKEYA', 'AGARGAON']
    route_C = ['ECB', 'MATIKATA', 'MIRPUR_14', 'MIRPUR_10', 'BEGUM_ROKEYA', 'AGARGAON']
    route_D = ['ECB', 'KALSHI', 'MIRPUR_11', 'MIRPUR_10', 'MIRPUR_14', 'JAHANGIR_GATE', 'BIJOY_SHARANI', 'AGARGAON']
    route_E = ['ECB', 'KALSHI', 'MIRPUR_11', 'MIRPUR_10', 'BEGUM_ROKEYA', 'AGARGAON']
    route_F = ['ECB', 'MIRPUR_12', 'MIRPUR_11', 'MIRPUR_10', 'BEGUM_ROKEYA', 'AGARGAON']

    route = []
    for x in ucs(ECB, 'AGARGAON') :
        route_temp = str(x).split(' ')
        route.append(route_temp[0])

    def map_finder() :
        global best_route_cost, best_route, best_route_dir
        if route == route_A :
            best_route_cost = prediction[5]+prediction[6]+prediction[4]+prediction[8]
            best_route_dir = 'ECB -> CANTONMENT -> JAHANGIR GATE -> BIJOY SHARANI -> BEGUM ROKEYA AVE -> AGARGAON'
            best_route = 'a' 
        elif route == route_B :
            best_route_cost = prediction[9]+prediction[3]+prediction[6]+prediction[4]+prediction[8]
            best_route_dir = 'ECB -> MATIKATA -> MIRPUR 14 -> JAHANGIR GATE -> BIJOY SHARANI -> BEGUM ROKEYA AVE -> AGARGAON'
            best_route = 'b'
        elif route == route_C :
            best_route_cost = prediction[9]+prediction[3]+prediction[0]+prediction[8]
            best_route_dir = 'ECB -> MATIKATA -> MIRPUR 14 -> MIRPUR 10 -> BEGUM ROKEYA AVE -> AGARGAON'
            best_route = 'b'
        elif route == route_D :
            best_route_cost = prediction[7]+prediction[1]+prediction[0]+prediction[8]+prediction[3]+prediction[6]+prediction[4]
            best_route_dir = 'ECB -> KALSHI -> MIRPUR 11 -> MIRPUR 10 -> MIRPUR 14 -> JAHANGIR GATE -> BIJOY SHARANI -> BEGUM ROKEYA AVE -> AGARGAON'
            best_route = 'c'
        elif route == route_E :
            best_route_cost = prediction[7]+prediction[1]+prediction[0]+prediction[8]
            best_route_dir = 'ECB -> KALSHI -> MIRPUR 11 -> MIRPUR 10 -> BEGUM ROKEYA AVE -> AGARGAON'
            best_route = 'd'
        elif route == route_F :
            best_route_cost = prediction[7]+prediction[2]+prediction[0]+prediction[8]
            best_route_dir = 'ECB -> MIRPUR 12 -> MIRPUR 11 -> MIRPUR 10 -> BEGUM ROKEYA AVE -> AGARGAON'
            best_route = 'e'
        else :
            best_route_dir = 'No suitable route available! Try Again'
            best_route = 'f'
            
    map_finder()
            
    sql = ("INSERT INTO best_route(route, cost, dir)"
        "VALUES (%s, %s, %s)")

    val = [
        (best_route , best_route_cost, best_route_dir)
    ]

    cursor.executemany(sql, val)
    cnx.commit()

    cursor.close()
    cnx.close()









