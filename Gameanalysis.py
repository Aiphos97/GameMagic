import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('game.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Ask the user
platform = input("🎮 Choose a platform (e.g., PC, Switch): ").strip().lower()  # Convert to lowercase
min_duration = int(input("⏱️ Minimum playtime in minutes (e.g., 30, 60): "))

# Filter the data
filtered_data = df[df['Platform'].str.lower() == platform]  # Convert the 'Platform' column to lowercase for matching
filtered_data = filtered_data[filtered_data['Duration (mins)'] > min_duration]

if filtered_data.empty:
    print("⚠️ No games found for the selected criteria.")
else:
    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['Game'], filtered_data['Duration (mins)'], color='orchid')
    plt.title(f'{platform.capitalize()} Games Played for More Than {min_duration} Minutes', fontsize=14)
    plt.xlabel('Game', fontsize=12)
    plt.ylabel('Duration (minutes)', fontsize=12)
    plt.xticks(rotation=90)
    plt.tight_layout()

    filename = f"{platform}_games_over_{min_duration}.csv"
    filtered_data.to_csv(filename, index=False)
    print(f"\n📁 Filtered data saved to: {filename}")

    img_name = f"{platform}_games_over_{min_duration}.png"
    plt.savefig(img_name, dpi=300)
    print(f"🖼️ Chart saved to: {img_name}")
    plt.show()
