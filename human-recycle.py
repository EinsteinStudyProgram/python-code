import time
from apscheduler.schedulers.blocking import BlockingScheduler

def myjob():
    print(time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time())))

sched = BlockingScheduler()
sched.add_job(myjob,'interval',seconds=5)


sched.start()