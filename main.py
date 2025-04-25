import subprocess

def main():
    print("🎮 Welcome to Game Magic!")
    print("What would you like to do?")
    print("1. Show PC games played for more than 60 minutes")
    print("2. Predict if a game session is long")
    print("3. Exit")

    choice = input("Enter your choice (1, 2 or 3): ").strip()

    if choice == '1':
        print("📊 Running game analysis...")
        subprocess.run(['python', 'Gameanalysis.py'])

    elif choice == '2':
        print("🔮 Running prediction model...")
        subprocess.run(['python', 'predict.py'])

    elif choice == '3':
        print("👋 Goodbye!")

    else:
        print("❌ Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
