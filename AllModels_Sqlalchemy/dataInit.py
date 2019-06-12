from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from qilucleaning.model import BR_MedicalImaging, BR_MedicalImaging_Diag, BR_Encounter, \
    BR_Demographics, BR_Pathology

import pymysql


class agent:
    def __init__(self,server_address,server_port,server_database,server_user,server_password):
        self.server_address=server_address
        self.server_port = server_port
        self.server_database = server_database
        self.server_user = server_user
        self.server_password = server_password

        # 这是sqlserver的连接方式
        # engine = create_engine('mssql+pymssql://'+str(self.server_user)+':'+str(self.server_password)+'@'+str(self.server_address)+':'+str(self.server_port)+'/'+str(self.server_database)+'?charset=utf8')

        # 这是mysql的连接方式
        engine = create_engine('mysql+pymysql://'+str(self.server_user)+':'+str(self.server_password)+'@'+str(self.server_address)+':'+str(self.server_port)+'/'+str(self.server_database)+'?charset=utf8', max_overflow=5)

        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        # 创建Session:
        self.session = DBSession()

    # 获得所有的就诊信息
    def get_all_encounters(self):
        all_encounters = self.session.query(BR_Encounter).all()
        return all_encounters

    # 根据就诊ID获得人口信息学的出生日期
    def get_encounter_age(self,iBR_EncounterID):
        target_demographics = self.session.query(BR_Demographics).filter(BR_Demographics.BR_EncounterID==iBR_EncounterID).first()
        return target_demographics.BR_Demographics_BirthDate

    # 根据就诊ID  获得所有的影像学信息
    def get_target_MedicalImaging(self, iBR_EncounterID):
        target_all_Imaging = self.session.query(BR_MedicalImaging).filter(
            BR_MedicalImaging.BR_EncounterID == iBR_EncounterID).all()
        return target_all_Imaging

    # 根据就诊ID  获得所有的病理学信息
    def get_target_Pathology(self, iBR_EncounterID):
        target_all_Pathology = self.session.query(BR_Pathology).filter(
            BR_Pathology.BR_EncounterID == iBR_EncounterID).all()
        return target_all_Pathology

    # 获得影像学
    def update_target_diag(self):
        all_BR_MedicalImaging = self.session.query(BR_MedicalImaging).all()
        return all_BR_MedicalImaging

    # 获得影像学诊断意见
    def get_diag(self,iBR_MedicalImagingID):
        all_BR_MedicalImaging_diag = self.session.query(BR_MedicalImaging_Diag).filter(BR_MedicalImaging_Diag.BR_MedicalImagingID==iBR_MedicalImagingID).all()
        return all_BR_MedicalImaging_diag


# 处理影像学中就诊意见的序号
# theo = agent('localhost', '1433', 'testDEQL', 'sa', '123')
# # print(len(theo.update_target_diag()))
# all_count=len(theo.update_target_diag())
# tCount=0
# for single in theo.update_target_diag():
#     tCount+=1
#     # 以下是每个影像学的ID
#     # print(single.BR_MedicalImagingID)
#
#     # 接下来需要到每个影像学诊断意见中查找  将其集合  做处理
#     target_diag=theo.get_diag(single.BR_MedicalImagingID)
#
#     diag_no=1
#     for single_diag in target_diag:
#         single_diag.BR_MedicalImaging_Diag_No=diag_no
#         diag_no+=1
#
#         theo.session.flush()
#
#     theo.session.commit()
#
#     result_position=tCount/all_count
#     result_position=round(result_position*100, 2)
#     print('完成度：'+str(result_position)+'%')
