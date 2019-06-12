from sqlalchemy import Column, String, INT, ForeignKey, Time, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 患者
class BR_Information(Base):
    # 表的名字:
    __tablename__ = 'BR_Information'

    # 表的结构:
    BR_Information_ID = Column(INT(), primary_key=True)

    BR_Information_PatientNo = Column(String(4000))

# 就诊
class BR_Encounter(Base):
    # 表的名字:
    __tablename__ = 'BR_Encounter'

    # 表的结构:
    BR_EncounterID = Column(INT(), primary_key=True)

    EncounterIDEncrypt= Column(String(500))


# 个人史
class BR_Behavior(Base):
    # 表的名字:
    __tablename__ = 'BR_Behavior'

    # 表的结构:
    BR_BehaviorID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_EncounterNewID=Column(INT())

# 既往病史
class BR_Comorbidity(Base):
    # 表的名字:
    __tablename__ = 'BR_Comorbidity'

    # 表的结构:
    BR_ComorbidityID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_EncounterNewID = Column(INT())

# 死亡情况
class BR_Death(Base):
    # 表的名字:
    __tablename__ = 'BR_Death'

    # 表的结构:
    BR_DeathID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_EncounterNewID = Column(INT())

# 人口信息学
class BR_Demographics(Base):
    # 表的名字:
    __tablename__ = 'BR_Demographics'

    # 表的结构:
    BR_Demographics_ID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_Demographics_BirthDate=Column(Date)

    BR_EncounterNewID = Column(INT())

# 诊断
class BR_Diagnosis(Base):
    # 表的名字:
    __tablename__ = 'BR_Diagnosis'

    # 表的结构:
    BR_DiagnosisID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_EncounterNewID = Column(INT())

# 诊断
class BR_Diagnosis_copy1(Base):
    # 表的名字:
    __tablename__ = 'BR_Diagnosis_copy1'

    # 表的结构:
    BR_DiagnosisID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_EncounterNewID = Column(INT())

# 实验室检查
class BR_Lab(Base):
    # 表的名字:
    __tablename__ = 'BR_Lab'

    # 表的结构:
    BR_LabID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_EncounterNewID = Column(INT())

# 影像学
class BR_MedicalImaging(Base):
    # 表的名字:
    __tablename__ = 'BR_MedicalImaging'

    # 表的结构:
    BR_MedicalImagingID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_MedicalImaging_ImageAge = Column(INT())

    BR_MedicalImaging_ImageDate=Column(Date)

    BR_EncounterNewID = Column(INT())

# 影像学诊断意见
class BR_MedicalImaging_Diag(Base):
    # 表的名字:
    __tablename__ = 'BR_MedicalImaging_Diag'

    # 表的结构:
    BR_MedicalImaging_DiagID = Column(INT(), primary_key=True)

    BR_MedicalImagingID = Column(INT(), ForeignKey('BR_MedicalImaging.BR_MedicalImagingID'))

    BR_MedicalImaging_Diag_No = Column(INT())

# 药物治疗
class BR_Medication(Base):
    # 表的名字:
    __tablename__ = 'BR_Medication'

    # 表的结构:
    BR_MedicationID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_EncounterNewID = Column(INT())

# 病理学
class BR_Pathology(Base):
    # 表的名字:
    __tablename__ = 'BR_Pathology'

    # 表的结构:
    BR_PathologyID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_PathologyID_PAAge = Column(INT())

    BR_PathologyID_PADate = Column(Date)

    BR_EncounterNewID = Column(INT())

# 诊疗处理
class BR_Procedure(Base):
    # 表的名字:
    __tablename__ = 'BR_Procedure'

    # 表的结构:
    BR_ProcedureID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_EncounterNewID = Column(INT())

# 化疗方案
class BR_Scheme(Base):
    # 表的名字:
    __tablename__ = 'BR_Scheme'

    # 表的结构:
    BR_SchemeID = Column(INT(), primary_key=True)

    BR_EncounterID = Column(INT(), ForeignKey('BR_Encounter.BR_EncounterID'))

    BR_EncounterNewID = Column(INT())

# 生命体征
class formativetableprimarykey_fourthtry(Base):
    # 表的名字:
    __tablename__ = 'formativetableprimarykey_fourthtry'

    formativeID= Column(INT(), primary_key=True)
    # 表的结构:
    Medical_record_no = Column(INT())

    Lis_visit_id = Column(INT())



