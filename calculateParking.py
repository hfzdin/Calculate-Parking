import math
import datetime

#set the rates according to weekdays,weekends
rateWeekdaysFirst3hour=3
rateWeekdaysAfter3hour=1.5
maxRateWeekdays=20
rateWeekendFirst3hour=5
rateWeekendsAfter3hour=2
maxRateWeekend=40
withinGracePeriod=True
parkingFare=0.0


#get input from user date of the car go into the parking lot
dateGoIn = input('Please enter the date vehicle go in the parking formatted as DD/MM/YYYY: ')
dateGoIn =datetime.datetime.strptime(dateGoIn,"%d/%m/%Y %H:%M")

#get input from user date of the car go out of the parking lot
dateGoOut = input('Please enter the date vehicle go out of the parking formatted as DD/MM/YYYY: ')
dateGoOut=datetime.datetime.strptime(dateGoOut,"%d/%m/%Y %H:%M")

#get input from user the car in grace period or not
withinGracePeriodString = input('Is the vehicle within grace period? Y or N?')

if withinGracePeriodString=="Y":
	withinGracePeriod=True
else:
	withinGracePeriod=False


print("date go in : "+dateGoIn.strftime('%d/%B/%Y %H:%M'))

print("date go out : "+dateGoOut.strftime('%d/%B/%Y %H:%M'))


dateTimeDifference=0;
dateTimeDifferenceInHours=0;
dateTimeDifferenceInMinutes=0;

#condition if car go in weekdays and go out weekdays
if((dateGoIn.weekday()<5) and (dateGoOut.weekday()<5 )):

	# Get the difference between datetimes (as timedelta)
	dateTimeDifference = dateGoOut - dateGoIn
	# Divide difference in seconds by number of seconds in hour (3600) 
	if(dateTimeDifference>datetime.timedelta(hours=1)):
		dateTimeDifferenceInHours = dateTimeDifference.total_seconds() / 3600
		dateTimeDifferenceInHours =int(dateTimeDifferenceInHours)

	if(dateTimeDifferenceInHours>24):
		parkingFare=parkingFare+maxRateWeekdays;
		remainingParkingHours=dateTimeDifferenceInHours-24
		if(dateGoOut.weekday()>5):
			if(remainingParkingHours>3):
				parkingFare=parkingFare+((remainingParkingHours-3)*rateWeekdaysAfter3hour)
			else:
				parkingFare=parkingFare+rateWeekdaysAfter3hour
		else:
			if(remainingParkingHours>3):
				parkingFare=parkingFare+((remainingParkingHours-3)*rateWeekendsAfter3hour)
			else:
				parkingFare=parkingFare+rateWeekendsAfter3hour

	if not withinGracePeriod:
			parkingFare+=rateWeekdaysFirst3hour
			if(dateTimeDifferenceInHours>3):
				parkingFare=parkingFare+((dateTimeDifferenceInHours-3)*rateWeekdaysAfter3hour)
			else:
				parkingFare=parkingFare+rateWeekdaysAfter3hour

#condition if car go in other than condition above
else:
	dateTimeDifference = dateGoOut - dateGoIn
	# Divide difference in seconds by number of seconds in hour (3600) 
	if(dateTimeDifference>datetime.timedelta(hours=1)):
		dateTimeDifferenceInHours = dateTimeDifference.total_seconds() / 3600
		dateTimeDifferenceInHours =int(dateTimeDifferenceInHours)

	if((dateTimeDifferenceInHours>24) and (dateGoIn.weekday()<5)):
		parkingFare=parkingFare+maxRateWeekdays;

	elif((dateTimeDifferenceInHours>24) and (dateGoIn.weekday()>5)):
		parkingFare=parkingFare+maxRateWeekend;

	if(dateTimeDifferenceInHours>24):
		remainingParkingHours=dateGoOut.hour
		if(dateGoOut.weekday()<5):
			parkingFare=parkingFare+(remainingParkingHours*rateWeekdaysAfter3hour)
			
		else:
			parkingFare=parkingFare+(remainingParkingHours*rateWeekendsAfter3hour)

	if not withinGracePeriod:
			parkingFare+=rateWeekendFirst3hour
			if(dateTimeDifferenceInHours>3):
				parkingFare=parkingFare+((dateTimeDifferenceInHours-3)*rateWeekendsAfter3hour)
			else:
				parkingFare=parkingFare+rateWeekendsAfter3hour
	

if(withinGracePeriod):
	print("Car fare = "+ str(parkingFare)+".Car parked for : "+  str(dateTimeDifferenceInHours)+ " hours and within grace periond.")

else:
	print("Car fare = "+ str(parkingFare)+".Car parked for : "+  str(dateTimeDifferenceInHours)+ " hours and over grace periond.")
