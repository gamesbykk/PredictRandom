import streamlit as st
import math

def isclose(x, y):
    if math.floor(x / 10) == math.floor(y // 10) - 1 or math.floor(x / 10) == math.floor(y // 10) or math.floor(x / 10) == (math.floor(y // 10) + 1) % 10:
        if math.floor(x % 10) == math.floor(y % 10) - 1 or math.floor(x % 10) == math.floor(y % 10) or math.floor(x % 10) == (math.floor(y % 10) + 1) % 10:
            return True

def predict(data):
    probs = dict(zip(list(range(100)), [0 for _ in range(100)]))
    for i in range(10, len(data) - 1):
        for j in range(9):
            if isclose(data[i - j], data[-(j + 1)]):
                probs[data[i + 1]] += 1
                if data[i - 1] == data[-1]:
                    probs[data[i + 1]] += 2
            else:
                break
    return max(probs, key=probs.get)

# Load the data from "rand.txt"
try:
    with open("rand.txt", "r") as f:
        data = f.read().split('\n')
        data = [int(i) for i in data if i]
except FileNotFoundError:
    data = []

st.title("Number Prediction App")
st.write("This app predicts the next number based on patterns in the existing data.")

# Input number
inps = st.number_input("Enter a number (1-100):", min_value=1, max_value=100, step=1)

if st.button("What the program thought you would say"):
    prediction = predict(data)
    st.write(f'Predicted next number: {prediction:.4f}')
    
    # Append new number to data and save
    data.append(int(inps))
    with open("rand.txt", "a") as f:
        f.write(f'\n{int(inps)}')
