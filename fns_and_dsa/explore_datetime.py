from datetime import datetime, timedelta


def calculate_future_date():
    current_date = datetime.now()
    print("Current date and time:", current_date)
    future_date = int(input("Enter the number of days to add to the current date: "))
    new_date = current_date + timedelta(days=future_date)
    print("Future date:", new_date)
    



if __name__ == "__main__":
    calculate_future_date()
