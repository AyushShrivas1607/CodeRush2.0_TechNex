import os
import sys

def print_menu():
    print("\n========================================")
    print("   SPACECRAFT SEGMENTATION PIPELINE   ")
    print("========================================")
    print("1. Train Model (train.py)")
    print("2. Evaluate Metrics (evaluate.py)")
    print("3. Run Single Inference & Visualize (predict.py)")
    print("4. Run End-to-End Mission Pipeline (pipeline.py)")
    print("5. Exit")
    print("----------------------------------------")

def main():
    while True:
        print_menu()
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            print("\n[+] Starting Training...")
            os.system(f"{sys.executable} train.py")
        elif choice == '2':
            print("\n[+] Running Evaluation...")
            os.system(f"{sys.executable} evaluate.py")
        elif choice == '3':
            print("\n[+] Running Inference...")
            os.system(f"{sys.executable} predict.py")
        elif choice == '4':
            print("\n[+] Executing Mission Pipeline Simulation...")
            os.system(f"{sys.executable} pipeline.py")
        elif choice == '5':
            print("\nExiting pipeline. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()