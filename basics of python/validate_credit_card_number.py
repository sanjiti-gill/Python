card = input("Enter credit card number: ")

# Step 1: Remove hyphens if any
card_number = card.replace("-", "")

# Step 2: Check if all characters are digits and length is 16
if not card_number.isdigit() or len(card_number) != 16:
    print("Invalid")
else:
    # Step 3: Must start with 4, 5, or 6
    if card_number[0] not in ['4', '5', '6']:
        print("Invalid")
    else:
        # Step 4: Check for 4 or more consecutive repeating digits
        valid = True
        for i in range(len(card_number) - 3):
            if card_number[i] == card_number[i+1] == card_number[i+2] == card_number[i+3]:
                valid = False
                break
        
        if valid:
            print("Valid")
        else:
            print("Invalid")
