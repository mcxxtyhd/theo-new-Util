import timeit
from time import clock

from qilucleaning.model import BR_Diagnosis, BR_Diagnosis_copy1
from qilucleaning.sqlconnnection import connsql
from redisPackage.ReServer import RedisServer


# 既往病史的加密
from utils.EncryptUtils import pyEOR

@clock
def cleaningBR_Diagnosis():

    # 初始化连接
    conntheo = connsql()


    print('****开始 BR_Diagnosis ****')

    numFirst=0
    numSecond=conntheo.perNum

    result_num=1

    # 如果数据为0了就不要再循环了
    while result_num<100:

        start_time=timeit.default_timer()

        for single in range(1+(result_num-1)*1000,1000*result_num+1):
            # pass
            # print(str(redis.getValue(int(single_result.BR_EncounterID))))

            newdata=BR_Diagnosis_copy1(BR_EncounterID=str(single),BR_EncounterNewID=pyEOR(71593504,int(single)))
            conntheo.theo.session.add(newdata)

            # 一定要flush()，否则会有语句丢失
            conntheo.theo.session.flush()


        end_time = timeit.default_timer()
        elapsed=end_time-start_time
        print('正在处理 {0}到{1}行的数据...'.format(str(1+(result_num-1)*1000), str(1000*result_num+1))+',花费了 %0.2fs...'%elapsed)

        result_num+=1

    # 最后关闭
    conntheo.theo.session.commit()
    conntheo.theo.session.close()


    print('****结束 BR_Diagnosis ****')


# #1、诊断的清理
cleaningBR_Diagnosis()


