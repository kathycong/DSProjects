#pip3 install humanize

import humanize
import datetime

posted_date = datetime.datetime(2023, 3, 22, 0, 47)
print(posted_date)

print(humanize.naturaltime(datetime.datetime.now() - posted_date))