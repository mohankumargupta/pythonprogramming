#find when the next microcontroller meeting is 
#second Wednesday of every month
import calendar
from time import strptime

def nextMeeting(month, year):
	#firstday: Mon:0 ...  Sun:6
	month_num = strptime(month,'%b').tm_mon
	print(month_num)
	firstday, end = calendar.monthrange(year,month_num)
	print(firstday,end)
	if firstday > 2:
		return 17 - firstday
	elif firstday < 2:
		return 10 - firstday
	else:
		return 8

meeting_date = nextMeeting('Mar', 2015)
print(meeting_date)
#print({v: k for k,v in enumerate(calendar.month_abbr)})