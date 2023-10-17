import math
import datetime

rateWeekdaysFirst3hour=3
rateWeekdaysAfter3hour=1.5
rateWeekendFirst3hour=5
rateWeekendsAfter3hour=2

dateGoIn = input('Please enter the date vehicle go in the parking formatted as DD/MM/YYYY: ')
dateGoIn=datetime.datetime.strptime(dateGoIn,"%d/%m/%Y").date()

dateGoOut = input('Please enter the date vehicle go out of the parking formatted as DD/MM/YYYY: ')
dateGoOut=datetime.datetime.strptime(dateGoOut,"%d/%m/%Y").date()

withinGracePeriod = input('Is the vehicle within grace period? ')

print("date go in : "+dateGoIn.strftime('%d/%B/%Y'))

print("date go out : "+dateGoOut.strftime('%d/%B/%Y'))

