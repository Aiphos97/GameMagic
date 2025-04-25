# GameMagic 🎮✨

**GameMagic** is a Python-based simple application that analyzes your gaming habits, predicts which games you're likely to play for long periods, and offers insights into your gaming history. It uses machine learning to make predictions based on your gaming logs and provides insightful data visualizations to help you better understand your gameplay.

<p align="center">
  <img src="https://raw.githubusercontent.com/Aiphos97/GameMagic/main/pc_games_over_30.png" alt="PC Games Over 30 Minutes" width="400"/>
</p>

## 📊 Features

- **Game Duration Analysis**: Analyzes how much time you've spent on each game and groups them by platform and playtime.
- **Game Prediction**: Uses a Random Forest model to predict whether you'll play a game for over 60 minutes based on previous data.
- **Visualization**: Generates visual representations (bar charts) for the time played on PC games for over 60 minutes.
- **Customizable Inputs**: Select the platform (PC, Switch, etc.) and time duration (over 30 mins or 60 mins) to generate personalized insights.
  
## 🚀 Installation

### Clone the repository:


## 💻 Usage

Game Analysis: To analyze your gaming log and see how much time you've played on each platform, simply run the game analysis script.
python game_analysis.py
Game Prediction: If you're interested in predictions based on your gaming habits, run the following:
python predict.py
Interactive Main Menu: The main file main.py allows you to interactively choose whether you want to analyze game data or make predictions.
python main.py
It will prompt you to:

Choose the platform (PC or Switch)
Choose the duration (over 30 minutes or 60 minutes)
Make predictions on which games you're likely to play for a long time.

## 📈 Visuals

The app will also generate a bar chart for games played over 60 minutes on your chosen platform and save it as an image file.

## 🔧 Technologies Used

Python: The core language for building the application.
Pandas: For data manipulation and analysis.
Scikit-learn: Used for the machine learning model that predicts game duration.
Matplotlib: For creating graphs and visualizations.


