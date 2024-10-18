#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #: w0425777     
#Student Name: Katherine Tucker

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # add \n after
    # ask for house number, depth, width
    House = input("Enter House Number: ")

    D = float(input("\nEnter property depth (feet) : "))
    W = float(input("\nEnter property width (feet) : "))

    # decision for base pay
    Area = ( D * W)
    if Area > float("5000"):
        Base = 1500
    else:
        Base = 1000
    
    #decision for grass type
    grass = input("\nEnter type of grass (fescue, bentgrass, campus): ").lower()
    if grass == "fescue":
        price = Area * 0.05
    elif grass == "bentgrass":
        price = Area * 0.02
    elif grass == "campus": 
        price = Area * 0.01
    else:
        price = Area
    
    # how many trees?
    trees = float(input("\nEnter the number of trees: "))

    Total = (trees* 100) + Base + price

    #print total
    print("\nTotal cost for house {0} is: ${1:.2f}\n".format(House, Total))


    # YOUR CODE ENDS HERE

main()