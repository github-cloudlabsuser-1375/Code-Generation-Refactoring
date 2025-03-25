#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100

# ...existing code...
def calculate_sum(arr):
    # Changed to use built-in sum
    return sum(arr)
# ...existing code...
def main():
    try:
        n = int(input("Enter the number of elements (1-100): "))
        if not 1 <= n <= MAX:
            print("Invalid input. Please provide a digit ranging from 1 to 100.")
            return  # Changed from exit(1)

        arr = []

        print(f"Enter {n} integers:")
        for _ in range(n):
            try:
                arr.append(int(input()))
            except ValueError:
                print("Invalid input. Please enter valid integers.")
                return  # Changed from exit(1)

        total = calculate_sum(arr)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        # Removed exit(1) to allow graceful exit
# ...existing code...
if __name__ == "__main__":
    main()