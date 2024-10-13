# Import necessary module for input
import sys

def main():
    #Variable Types
    s1 = s2 = s3 = address = country = '' #String
    a = b = c = code = 0 #Integer
    q1 = q2 = q3 = 0 #Integer
    price1 = price2 = price3 = 0.0 #Float
    totalcost = totalcost2 = totalcost3 = subtotal = 0.0 #Float
    gst = gst2 = gst3 = totalgst = everything = 0.0 #Float

    print("Welcome to Iphone Online Service")
    print("----------------------")
    print("Enter 3 Iphone to be sold")

    s1 = input()
    s2 = input()
    s3 = input()
    print("\n---------------------------------------------\n")


    print("Welcome to iPhone online service")
    print("----------------------")
    print("Enter three iPhone to be sold")

    print(f"1.", s1)
    print(f"2.", s2)
    print(f"3.", s3)
    print("\n---------------------------------------------\n")


    print("Some Other Information")
    print("-----------------")
    print("Delivery Address: ")
    address = input()
    print("Postal Code: ")
    code = int(input())
    print("Country")
    country = input()
    print("\n---------------------------------------------\n")


    print(f"Delivery Address: ", address)
    print(f"Postal Code: ", code)
    print(f"Country: ", country)
    print("\n---------------------------------------------\n")


    print("Enter the quantities and price of iPhone 12 Mini: ")
    q1 = int(input())
    price1 = float(input()) 

    print("Enter the quantities and price of iPhone 12 Pro: ")
    q2 = int(input())
    price2 = float(input()) 

    print("Enter the quantities and price of iPhone 12 Max: ")
    q3 = int(input())
    price3 = float(input()) 

      # Display the table information
    print("\nSummary of iPhones")
    print("----------------------")
    print(f"iPhone              Quantity        Price")
    print(f"{s1}               {q1}        {price1:.2f}")
    print(f"{s2}               {q2}        {price2:.2f}")
    print(f"{s3}               {q3}        {price3:.2f}")


    # Swap the names and prices of the 1st and 2nd iPhones
    s1, s2 = s2, s1
    q1, q2 = q2, q1
    price1, price2 = price2, price1


    print("\nSummary of iPhones after swaps")
    print("\n----------------------\n")
    print(f"iPhone              Quantity        Price")
    print(f"{s1}               {q1}        {price1:.2f}")
    print(f"{s2}               {q2}        {price2:.2f}")
    print(f"{s3}               {q3}        {price3:.2f}")


    print("Please Place Your Order")
    print("\n----------------------\n")
    print("No of iPhone 12 Pro: ")
    a = int(input())
    totalcost = a * price1  #Compute the price of the quantities and price for iphone 12 pro order


    print("No of iPhone 12 Mini: ")
    b = int(input())
    totalcost2 = b * price2

    print("No of iPhone 12 Max: ")
    c = int(input())
    totalcost3 = b * price3

    print("----------------------")
    print(f"iPhone           Quantity        Price")
    print(f"{s1}            {a}         {totalcost:.2f}")
    print(f"{s2}            {b}         {totalcost2:.2f}")
    print(f"{s3}            {c}         {totalcost3:.2f}")


    # Calculate subtotal, GST, and total cost
    subtotal = totalcost + totalcost2 + totalcost3
    gst = 0.07 * totalcost
    gst2 = 0.07 * totalcost2
    gst3 = 0.07 * totalcost3
    totalgst = gst + gst2 + gst3
    everything = subtotal + totalgst

    # Display final cost
    print(f"Subtotal:       {subtotal:.2f}")
    print(f"GST (7%):       {totalgst:.2f}")
    print(f"Total Cost:     {everything:.2f}")


    # Calculate stock balance
    t = q1 - a
    t2 = q2 - b
    t3 = q3 - c

     # Display balance report
    print("\nBalance report")
    print("----------------------")
    print(f"iPhone          Quantity    Sold    Balance")
    print(f"{s1}   {q1}        {a}      {t}")
    print(f"{s2}  {q2}        {b}      {t2}")
    print(f"{s3}  {q3}        {c}      {t3}")


# Run the program
if __name__ == "__main__":
    main()