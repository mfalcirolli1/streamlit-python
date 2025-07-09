import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Jornada do Robô no Labirinto", layout="centered")
st.title("🤖 Jornada do Robô no Labirinto com Reforço (RL)")

# --- PARÂMETROS DO AMBIENTE ---
maze = np.array([
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 2]
])
start = (0, 0)
goal = (4, 4)
actions = ['up', 'down', 'left', 'right']

# --- PARÂMETROS DO RL ---
alpha = 0.1
gamma = 0.9
epsilon = 0.1
episodes = 100

q_table = np.zeros(maze.shape + (4,))
episode_paths = []  # <--- Armazena os caminhos de cada episódio

def is_valid(state):
    x, y = state
    return 0 <= x < maze.shape[0] and 0 <= y < maze.shape[1] and maze[x, y] != 1

def get_next_state(state, action):
    x, y = state
    if action == 'up': x -= 1
    elif action == 'down': x += 1
    elif action == 'left': y -= 1
    elif action == 'right': y += 1
    new_state = (x, y)
    return new_state if is_valid(new_state) else state

def get_reward(state):
    return 1 if state == goal else -0.1

def choose_action(state):
    if np.random.rand() < epsilon:
        return np.random.choice(actions)
    idx = np.argmax(q_table[state])
    return actions[idx]

# --- TREINAMENTO COM REGISTRO DE TRAJETÓRIAS ---
with st.spinner("Treinando o robô e registrando todas as tentativas..."):
    for _ in range(episodes):
        state = start
        path = [state]
        visited = set()
        while state != goal and len(path) < 100:
            action = choose_action(state)
            next_state = get_next_state(state, action)
            reward = get_reward(next_state)
            a_idx = actions.index(action)
            best_next = np.max(q_table[next_state])
            q_table[state][a_idx] += alpha * (reward + gamma * best_next - q_table[state][a_idx])
            path.append(next_state)
            state = next_state
        episode_paths.append(path)
    st.success("Treinamento completo!")

# --- VISUALIZAÇÃO DA TRAJETÓRIA POR EPISÓDIO ---
st.subheader("🎥 Visualização por Episódio")
selected_episode = st.slider("Escolha o episódio para visualizar", 1, episodes, 1)
path = episode_paths[selected_episode - 1]

fig, ax = plt.subplots()
def draw_maze(path):
    ax.clear()
    for x in range(maze.shape[0]):
        for y in range(maze.shape[1]):
            color = 'white'
            if maze[x, y] == 1:
                color = 'black'
            elif maze[x, y] == 2:
                color = 'green'
            ax.add_patch(plt.Rectangle((y, maze.shape[0] - 1 - x), 1, 1, facecolor=color, edgecolor='gray'))

    for i, (x, y) in enumerate(path):
        color = 'blue' if i != len(path) - 1 else 'red'
        ax.add_patch(plt.Circle((y + 0.5, maze.shape[0] - 1 - x + 0.5), 0.3, color=color))

    ax.set_xlim(0, maze.shape[1])
    ax.set_ylim(0, maze.shape[0])
    ax.set_aspect('equal')
    ax.axis('off')

draw_maze(path)
st.pyplot(fig)
