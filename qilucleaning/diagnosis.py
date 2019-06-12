import timeit

from qilucleaning.model import BR_Diagnosis, BR_Diagnosis_copy1
from qilucleaning.sqlconnnection import connsql
from redisPackage.ReServer import RedisServer


# 既往病史的加密
def cleaningBR_Diagnosis():

    # 初始化连接
    conntheo = connsql()
    # 初始化redis连接
    redis = RedisServer()

    print('****开始 BR_Diagnosis ****')

    numFirst=0
    numSecond=conntheo.perNum

    result_num=1

    # 如果数据为0了就不要再循环了
    while result_num>0:
        start_time1 = timeit.default_timer()

        all_results = conntheo.theo.session.query(BR_Diagnosis).slice(numFirst, numSecond).all()

        end_time1 = timeit.default_timer()
        elapsed1 = end_time1 - start_time1
        print('这是取数据的时间，花费了 %0.2fs...' % elapsed1)

        # 如果没有数据了 就不要再循环了
        if len(all_results)==0:
            break
        else:
            numFirst += conntheo.perNum
            numSecond += conntheo.perNum

        start_time=timeit.default_timer()

        for single_result in all_results:
            # pass
            # print(str(redis.getValue(int(single_result.BR_EncounterID))))
            single_result.BR_EncounterNewID=redis.getValue(int(single_result.BR_EncounterID))

            # 一定要flush()，否则会有语句丢失
            conntheo.theo.session.flush()


        end_time = timeit.default_timer()
        elapsed=end_time-start_time
        print('正在处理 {0}到{1}行的数据...'.format(str(numFirst-conntheo.perNum), str(numSecond-conntheo.perNum))+',花费了 %0.2fs...'%elapsed)

    # 最后关闭
    conntheo.theo.session.commit()
    conntheo.theo.session.close()


    print('****结束 BR_Diagnosis ****')


# #1、诊断的清理
cleaningBR_Diagnosis()


