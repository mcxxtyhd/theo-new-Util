import datetime
from datetime import date



# 小的时间在前面 大的时间在后面
def get_age_bydate(theotime,theotime1):


    delta = theotime1 - theotime

    delta=int(delta.days/365.25)

    return delta

    # print (delta)

# theotime ='1961-06-24'
# theotime1 ='2016-06-06'
# theotime = datetime.datetime.strptime(theotime, '%Y-%m-%d')
# theotime1 = datetime.datetime.strptime(theotime1, '%Y-%m-%d')
#
# print(get_age_bydate(theotime,theotime1))


# from time import *
# # a function to find your age
# def age(iday,imonth,iyear):
#     print
#     "Enter Your Date of Birth"
#     d = iday
#     m = imonth
#     y = iyear
#     # get the current time in tuple format
#     a = gmtime()
#     # difference in day
#     dd = a[2] - d
#     # difference in month
#     dm = a[1] - m
#     # difference in year
#     dy = a[0] - y
#     # checks if difference in day is negative
#     if dd < 0:
#         dd = dd + 30
#         dm = dm - 1
#         # checks if difference in month is negative when difference in day is also negative
#         if dm < 0:
#             dm = dm + 12
#             dy = dy - 1
#             # checks if difference in month is negative when difference in day is positive
#     if dm < 0:
#         dm = dm + 12
#         dy = dy - 1
#     print("Your current age is %s Years %s Months & %s Days" % (dy, dm, dd))

