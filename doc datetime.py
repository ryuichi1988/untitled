https://dateutil.readthedocs.io/en/stable/examples.html

relativedelta examples
Let’s begin our trip:

>>> from datetime import *; from dateutil.relativedelta import *
>>> import calendar
Store some values:

>>> NOW = datetime.now()
>>> TODAY = date.today()
>>> NOW
datetime.datetime(2003, 9, 17, 20, 54, 47, 282310)
>>> TODAY
datetime.date(2003, 9, 17)
Next month

>>> NOW+relativedelta(months=+1)
datetime.datetime(2003, 10, 17, 20, 54, 47, 282310)
Next month, plus one week.

>>> NOW+relativedelta(months=+1, weeks=+1)
datetime.datetime(2003, 10, 24, 20, 54, 47, 282310)
Next month, plus one week, at 10am.

>>> TODAY+relativedelta(months=+1, weeks=+1, hour=10)
datetime.datetime(2003, 10, 24, 10, 0)
Here is another example using an absolute relativedelta. Notice the use of year and month (both singular) which causes the values to be replaced in the original datetime rather than performing an arithmetic operation on them.

>>> NOW+relativedelta(year=1, month=1)
datetime.datetime(1, 1, 17, 20, 54, 47, 282310)
Let’s try the other way around. Notice that the hour setting we get in the relativedelta is relative, since it’s a difference, and the weeks parameter has gone.

>>> relativedelta(datetime(2003, 10, 24, 10, 0), TODAY)
relativedelta(months=+1, days=+7, hours=+10)