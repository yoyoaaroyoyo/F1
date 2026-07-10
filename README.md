# 🏁 Random F1 Race Simulation

A simple Formula 1-inspired race simulation built with **Python** and the **Turtle** graphics library. Instead of user-controlled cars, the simulation features multiple colored arrows representing racing cars that move forward randomly until one reaches the finish line.

This project demonstrates randomness, animation, and basic simulation concepts using Python's built-in Turtle module.

## ✨ Features

* Multiple racers represented by different colored Turtle arrows
* Random movement where each racer advances by either **0** or **1** step each turn
* Animated race visualization
* Automatically determines the winning racer
* Simple and beginner-friendly implementation

## 🛠️ Built With

* Python 3
* Turtle Graphics (built into Python)
* Random module

## 🚀 How It Works

1. Multiple colored arrows are placed at the starting line.
2. During each iteration of the simulation, every racer randomly moves forward by either:

   * **0 steps** (no movement), or
   * **1 step** (moves forward).
3. The process repeats until one racer crosses the finish line.
4. The first racer to reach the finish line is declared the winner.

Because the movement is random, each race can produce a different winner.

## ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/yoyoaaroyoyo/F1
```

Navigate to the project folder:

```bash
cd F1.py
```

Run the program:

```bash
python F1.py
```

## 📁 Project Structure

```text
F1/
│── F1.py
│── README.md
```

## 🎯 Learning Objectives

This project demonstrates:

* Python Turtle graphics
* Random number generation
* Loops and conditional statements
* Simple simulation design
* Basic animation concepts

## 💡 Possible Improvements

* Adjustable race length
* Variable movement speeds (instead of only 0 or 1)
* Different probability distributions for each racer
* Race statistics over multiple simulations
* Finish line graphics
* Countdown before the race starts
* Display the winning racer and race time
* Add spectator or track visuals

## 📜 License

This project is open source and available under the MIT License.
