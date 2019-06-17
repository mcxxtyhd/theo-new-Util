import threading
import timeit

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from AllModels_Sqlalchemy.dataInit import agent
from qilucleaning.model import BR_Diagnosis_copy1
from utils.EncryptUtils import pyEOR
from utils.timekill import clock


class threadCleaning(threading.Thread):
    def __init__(self,sess,threadname,lock):
        threading.Thread.__init__(self)
        self.sess = sess
        self.lock = lock
        self.threadname=threadname

    def run(self):

        result_num = 1

        # 如果数据为0了就不要再循环了
        while result_num < 100:

            start_time = timeit.default_timer()

            for single in range(1 + (result_num - 1) * 1000, 1000 * result_num + 1):
                # pass
                # print(str(redis.getValue(int(single_result.BR_EncounterID))))

                newdata = BR_Diagnosis_copy1(BR_EncounterID=str(single), BR_EncounterNewID=pyEOR(71593504, int(single)))
                self.sess.session.add(newdata)

                # 一定要flush()，否则会有语句丢失
                self.sess.session.flush()

            end_time = timeit.default_timer()
            elapsed = end_time - start_time
            print('当前进程为： -----  '+self.threadname+' ----- ,正在处理 {0}到{1}行的数据...'.format(str(1 + (result_num - 1) * 1000),
                                               str(1000 * result_num + 1)) + ',花费了 %0.2fs...' % elapsed)

            result_num += 1

        # 最后关闭
        self.sess.session.commit()
        self.sess.session.close()

@clock
def testTime():
    print('主线程开始')

    # 开的线程个数
    tThreadNum=5

    allThread=[]
    sessions = []
    for i in range(tThreadNum):

        # 建立连接
        threadAgent = agent('localhost', '3306', 'testconnectspeed', 'root',"root")

        sessions.append(threadAgent.session)

        # 创建锁
        counter_lock = threading.Lock()

        # 第一个参数是每次循环执行多少个
        # 第二个参数是 从多少条数据开始
        # 第三个参数是 在多少条数据结束
        # 给2的原因是怕除数有余
        single=threadCleaning(threadAgent.session,'线程'+str(i),counter_lock)
        allThread.append(single)

    for h in allThread:
        h.start()

    for x in allThread:
        x.join()

    # 最后才提交以及结束
    for y in sessions:
        # 最后提交
        y.commit()
        # 关闭Session:
        y.close()

    print('主线程结束')

testTime()