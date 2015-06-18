# -*- coding: utf-8 -*-
# code for console Encoding difference. Don't mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Except as E: pass

import testValue

from closedown import CloseDown, CloseDownException

closedownChecker = CloseDown(testValue.LinkID,testValue.SecretKey)

try:
    print("휴폐업조회 - 대량")
    
    # 사업자번호 목록, 최대 1000건
    corpNumList = ["4108600477","1234567890","8888888888", "4352343543"]

    corpStateList = closedownChecker.checkCorpNums(corpNumList)

    tmp = "* state(사업자상태) : null - 알수없음, 0 - 등록되지 않은 사업자번호, 1 - 사업중, 2 - 폐업, 3 - 휴업 " +"\n"
    tmp += "* type(사업자유형) : null - 알수없음, 1 - 부가가치세 일반과세자, 2 - 부가가치세 면세과세자, 3 - 부가가치세 간이과세자, 4 - 비영리법인 또는 국가기관, 고유번호가 부여된 단체 " +"\n"
    print(tmp)

    i = 0

    for CorpState in corpStateList:
        i = i + 1
        print ("corpNum : %s " % CorpState.corpNum)
        print ("type : %s " % CorpState.type)
        print ("state : %s " % CorpState.state)
        print ("stateDate : %s " % CorpState.stateDate)
        print ("checkDate : %s " % CorpState.checkDate)
        print ("\n")

    #for state in corpStateList:    
    #    for key, value in state.__dict__.items():
    #        if not key.startswith("__"):
    #            print("%s : %s" % (key,value))
    #    print("\n")

except CloseDownException as CE:

    print("Exception Occur : [%d] %s" % (CE.code, CE.message))