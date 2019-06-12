from qilucleaning.model import BR_Behavior
from qilucleaning.sqlconnnection import connsql
from utils.EncryptUtils import pyEOR



# 个人史的加密
def cleaningbehavior():

    # 初始化连接
    conntheo = connsql()

    print('****开始 behavior ****')

    numFirst=0
    numSecond=conntheo.perNum

    result_num=1

    # 如果数据为0了就不要再循环了
    while result_num>0:
        all_behaviors = conntheo.theo.session.query(BR_Behavior).order_by(BR_Behavior.BR_BehaviorID).slice(numFirst, numSecond).all()

        # 如果没有数据了 就不要再循环了
        if len(all_behaviors)==0:
            break
        else:
            numFirst += conntheo.perNum
            numSecond += conntheo.perNum

        print('正在处理 {0}到{1}行的数据...'.format(str(numFirst-5000), str(numSecond-5000)))

        for single_behavior in all_behaviors:

            single_behavior.BR_EncounterNewID=int(pyEOR(conntheo.key,int(single_behavior.BR_EncounterID)))
            # 一定要flush()，否则会有语句丢失
            conntheo.theo.session.flush()


    # 最后提交一下
    conntheo.theo.session.commit()
    # 最后关闭
    conntheo.theo.session.close()
    print('****结束 behavior ****')



