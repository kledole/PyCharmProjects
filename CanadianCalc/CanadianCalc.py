# File: Canadian Calc
# Description:
#  - Calculates the total order charge from an Online Canadian Store
#
#  - Asks user what country they from, and the total order cost.
#  - If the user is from Canada, prompts the user to enter a province.

# - If outside of Canada, no sales tax is added.

# - Taxes for Canadian provinces are:
#   Alberta = .05% (GST)
#   Ontario, NewBrunswick, Nova Scotia .13%  (Harmonized sales tax)
#   All other (or unknown provinces: .06% provincial tax + .05% (GST)

# Variables:
#    country - name of country
#    cost - cost of order
#    total = total cost of order with appropriate tax
#    province = Canadian province
#    gst - gst tax rate
#    hst - Harmonized sales tax rate
#    provincial = provincial tax rate

# Timestamp: 5:52:18

cost = input("Enter the total purchase cost (decimal only, no dollar sign): ")
canada = input("Was the product purchased in Canada?").upper()

cost = float(cost)


# If no country:
if canada == 'NO':
    total_cost = cost
    print("No sales tax is required, your total cost is {0:.2f}".format(float(total_cost)))
else :
    province = input("Please enter the Canadian province, which sold the product : ").upper()
    if province == 'ONTARIO' or province == 'NEW BRUNSWICK' or province == 'NOVA SCOTIA' :
        hst =  float(.13) * cost
        print("Harmonized sales tax: {0:.2f}".format(hst))
        total_cost = cost + hst
    elif province  == 'ALBERTA' :
        gst = float(.05 * cost)
        print("General Sales Tax: {0:.2f}".format(gst))
        total_cost = cost + gst
    else :
        provincial = float(cost * .06)
        print("Provincial tax: {0:.2f}".format(provincial))
        gst = float(cost * .05)
        print("General Sales Tax: {0:.2f}".format(gst))
        total_cost = cost + provincial + gst

    # Output the total amount:
    print("Your total cost of the product is {0:.2f}".format(float(total_cost)))













