import timeit

from qilucleaning.model import BR_Encounter
from qilucleaning.sqlconnnection import connsql
from utils.EncryptUtils import pyhashlibMd5
import pymssql
import decimal

# 既往病史的加密
def cleaningEncounter():

    # 初始化连接
    conntheo = connsql()

    print('****开始 Encounter ****')

    numFirst=0
    numSecond=conntheo.perNum

    result_num=1

    # 如果数据为0了就不要再循环了
    while result_num>0:
        all_results = conntheo.theo.session.query(BR_Encounter).order_by(BR_Encounter.BR_EncounterID).slice(numFirst, numSecond).all()

        # 如果没有数据了 就不要再循环了
        if len(all_results)==0:
            break
        else:
            numFirst += conntheo.perNum
            numSecond += conntheo.perNum

        print('正在处理 {0}到{1}行的数据...'.format(str(numFirst-conntheo.perNum), str(numSecond-conntheo.perNum)))
        start_time=timeit.default_timer()

        for single_result in all_results:
            single_result.EncounterIDEncrypt=pyhashlibMd5(single_result.BR_EncounterID)

            # 一定要flush()，否则会有语句丢失
            conntheo.theo.session.flush()


        end_time = timeit.default_timer()
        elapsed=end_time-start_time
        print('花费了 %0.2fs...'%elapsed)

    # 最后关闭
    conntheo.theo.session.commit()
    conntheo.theo.session.close()


    print('****结束 Encounter ****')


# #1、诊断的清理
cleaningEncounter()


