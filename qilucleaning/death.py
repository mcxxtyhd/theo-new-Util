from qilucleaning.model import BR_Death
from qilucleaning.sqlconnnection import connsql
from utils.EncryptUtils import pyEOR

# 既往病史的加密
def cleaningBR_Death():

    # 初始化连接
    conntheo = connsql()

    print('****开始 BR_Death ****')

    numFirst=0
    numSecond=conntheo.perNum

    result_num=1

    # 如果数据为0了就不要再循环了
    while result_num>0:
        all_results = conntheo.theo.session.query(BR_Death).order_by(BR_Death.BR_DeathID).slice(numFirst, numSecond).all()

        # 如果没有数据了 就不要再循环了
        if len(all_results)==0:
            break
        else:
            numFirst += conntheo.perNum
            numSecond += conntheo.perNum

        print('正在处理 {0}到{1}行的数据...'.format(str(numFirst-5000), str(numSecond-5000)))

        for single_result in all_results:
            single_result.BR_EncounterNewID=int(pyEOR(conntheo.key,int(single_result.BR_EncounterID)))
            # 一定要flush()，否则会有语句丢失
            conntheo.theo.session.flush()


    # 最后提交一下
    conntheo.theo.session.commit()
    # 最后关闭
    conntheo.theo.session.close()
    print('****结束 BR_Death ****')


# #1、死亡的清理
cleaningBR_Death()


