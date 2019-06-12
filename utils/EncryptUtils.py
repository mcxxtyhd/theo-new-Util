import hashlib

# hashlib md5加密
def pyhashlibMd5(needsEncryptData):
    newcontent=str(needsEncryptData).strip()
    return str(hashlib.md5(newcontent.encode(encoding='UTF-8')).hexdigest()).strip()

# 异或加密
def pyEOR(key,needsEncryptData):
    # print('raw data:'+str(needsEncryptData))
    newresult=key^needsEncryptData
    # print('new data:'+str(newresult))

    return newresult




