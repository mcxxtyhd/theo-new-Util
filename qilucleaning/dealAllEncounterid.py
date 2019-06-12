from qilucleaning.model import BR_Encounter
from qilucleaning.sqlconnnection import connsql
from redisPackage.ReServer import RedisServer
from utils.EncryptUtils import pyEOR


# 初始化sqlserver连接
conntheo = connsql()
# 初始化redis连接
redis=RedisServer()


print('****开始 转换encounterid ****')

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

    for single_result in all_results:

        current_encounterid=int(single_result.BR_EncounterID)
        result=int(pyEOR(conntheo.key,current_encounterid))

        # print("old value {0},and this is new value:{1}".format(current_encounterid,result))
        redis.setValue(int(result),int(current_encounterid))


# 最后关闭
conntheo.theo.session.close()
print('****结束 转换encounterid ****')