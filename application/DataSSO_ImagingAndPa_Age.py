from AllModels_Sqlalchemy.dataInit import agent
from utils.ageJudge import get_age_bydate

theo = agent('192.168.11.201', '1433', 'DataEntryQL', 'sa', '!QAZ2wsx')

target_collection=theo.get_all_encounters()

all_count=len(target_collection)
tCount=0

for single in target_collection:
    tCount+=1
    # 以下是每个就诊的ID
    # print(single.BR_EncounterID)

    # 去查找人口信息学的出生日期
    encounter_birthdate=theo.get_encounter_age(single.BR_EncounterID)

    # 获得所有的影像学数据
    all_Imaging=theo.get_target_MedicalImaging(single.BR_EncounterID)

    # 遍历影像学数据
    for single_Imaging in all_Imaging:
        Imaging_age=get_age_bydate(encounter_birthdate,single_Imaging.BR_MedicalImaging_ImageDate)

        if Imaging_age>-1:
            # print('就诊ID:'+str(single.BR_EncounterID)+',出生日期：'+str(encounter_birthdate)+',影像学日期：'+str(single_Imaging.BR_MedicalImaging_ImageDate)+'影像学年龄：'+str(Imaging_age))
            single_Imaging.BR_MedicalImaging_ImageAge=Imaging_age
            theo.session.flush()

    # 获得所有的病理学数据
    all_Pathlogy =theo.get_target_Pathology(single.BR_EncounterID)

    # 遍历病理学数据
    for single_Pathlogy in all_Pathlogy:
        Pathlogy_age = get_age_bydate(encounter_birthdate, single_Pathlogy.BR_PathologyID_PADate)
        if Pathlogy_age > -1:
            # print('就诊ID:' + str(single.BR_EncounterID) + ',出生日期：' + str(encounter_birthdate) + ',影像学日期：' + str(
            #     single_Pathlogy.BR_PathologyID_PADate) + '病理学年龄：' + str(Pathlogy_age))
            single_Pathlogy.BR_PathologyID_PAAge = Pathlogy_age
            theo.session.flush()

    theo.session.commit()

    result_position=tCount/all_count
    result_position=round(result_position*100, 2)
    print('完成度：'+str(result_position)+'%')
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
