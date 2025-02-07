# Bus seat booking
max_seat = 8

while max_seat > 0:
    print(f"{max_seat} seats available")
    book=input("Book your seat.(yes/no):")
    if book == "yes":
        max_seat-=1
        print("Seat is booked.")
    else:
        print("No booking done")
print("All seat booked.")