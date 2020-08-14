from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
print('room graph', room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path will be filled in with the directions, literally w, e, n, s
traversal_path = []
# return path will contain cardinal directions that will lead us back to where we started
# this will be useful when player hits leaf node but hasn't visited all rooms yet
return_path = []
# dictionary that stores all visited rooms. Key is room id and value is directions of exits.
visited = {}
# This gives us the opposite of the direction we just traveled.  We will put this opposite value in the return-path list.
reverse_direction = {'w': 'e', 'e': 'w', 'n': 's', 's': 'n'}

# start at room 0 and find possible exits
visited[player.current_room.id] = player.current_room.get_exits()
print('initial visited', visited)
# if length of visited{} is equal to length of room_graph, then all rooms have been visited
while len(visited) < len(room_graph):
    print('length of visited', len(visited))
    print('length', len(room_graph))
    print('updated visited', visited)
     # if room that we moved to isn't in dict
    print('current room', player.current_room.id)
    # if current room is not in visited dict
    if player.current_room.id not in visited:
        print('entering new room', player.current_room.id)
        # add key/value of current room/possible exits to visited dict
        visited[player.current_room.id] = player.current_room.get_exits()
        # set variable to the value of the last direction the player moved
        remove_prev = return_path[-1]
        print('remove', remove_prev)
        print('return path', return_path) 
        # removes the previous direction from the possible exits for the current room
        visited[player.current_room.id].remove(remove_prev)
    
    # else: if we get to dead end but there's another way (need to go back)
    # if length of visited at current room is 0, then we have no new options
    elif len(visited[player.current_room.id]) == 0:
        remove_prev = return_path[-1]
        print('return path', return_path)
        return_path.pop()
        traversal_path.append(remove_prev)
        player.travel(remove_prev)

    # this is our general move logic
    else:
        print('ELSE')
        # pop off last direction in visited dict for current room, and go there next
        # ex: if dict shows {0: ['n', 's', 'w', 'e']}, then we pop 'e' off and go that way
        choice = visited[player.current_room.id].pop()
        print('choice', choice)
        print('visited 2', visited[player.current_room.id])
        # add the direction to the traversal_path
        traversal_path.append(choice)
        # add the opposite of the choice to the return_path so we can turn around if needed
        return_path.append(reverse_direction[choice])
        print('reverse choice', reverse_direction[choice])
        # move player using choice variable
        player.travel(choice)






# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
