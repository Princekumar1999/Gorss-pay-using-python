''' Write a program to prompt the user for hours and rate
 per hour using input to compute gross pay.
 Pay the hourly rate for the hours up to 40 and 1.5 times
 the hourly rate for all hours worked above 40 hours.
 Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75)'''
hrs = float(input('Enter Hours:'))
rat = float(input('Enter Rate:'))
if hrs>40:
    sdk = hrs * rat
    hgg = (hrs - 40.0) * (rat * 0.5)
    hgs = sdk + hgg
else:
    hgs = hrs * rat
print(hgs)
