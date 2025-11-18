import matplotlib.pyplot as plt
import time
import matplotlib.patches as patches

environment = {
    "Room 1": "Clean",
    "Room 2": "Dirty",
    "Room 3": "Dirty",
    "Room 4": "Clean"
}

room_positions = {
    "Room 1": (0, 1),
    "Room 2": (1, 1),
    "Room 3": (0, 0),
    "Room 4": (1, 0)
}

rooms = list(environment.keys())
agent_index = 0  # Start in Room 1

def reflex_agent(state):
    if state == "Dirty":
        return "Clean"
    else:
        return "Move"
    

def draw_environment(env, agent_position, step):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f'Step {step} - Agent in {rooms[agent_position]}')
    
    for room, pos in room_positions.items():
        x, y = pos
        color = 'red' if env[room] == "Dirty" else 'green'
        rect = patches.Rectangle((x, y), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        ax.text(x + 0.5, y + 0.5, room, ha='center', va='center', color='white')
    
    agent_x, agent_y = room_positions[rooms[agent_position]]
    agent_patch = patches.Circle((agent_x + 0.5, agent_y + 0.5), 0.1, color='blue')
    ax.add_patch(agent_patch)

    plt.pause(1.5)
    plt.close()



plt.ion()
steps = 8

for step in range(steps):
    current_room = rooms[agent_index]
    current_state = environment[current_room]
    
    draw_environment(environment, agent_index, step)
    
    action = reflex_agent(current_state)
    
    if action == "Clean":
        environment[current_room] = "Clean"
    else:
        agent_index = (agent_index + 1) % len(rooms)

plt.ioff()
print("Simulation complete.")