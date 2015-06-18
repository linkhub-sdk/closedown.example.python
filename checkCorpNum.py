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
    print("휴폐업조회 - 단건")
    
    # 사업자번호 
    corpNum = "4108600477"

    corpState = closedownChecker.checkCorpNum(corpNum)

    tmp = "corpNum (사업자번호) : " + str(corpState.corpNum) +"\n"
    tmp += "type (사업자유형) : " + str(corpState.type) +"\n"
    tmp += "state (사업자상태) : " + str(corpState.state) +"\n"
    tmp += "stateDate (휴폐업일시) : " + str(corpState.stateDate) +"\n"
    tmp += "checkDate (최종 국세청 확인 일자) : " + str(corpState.checkDate) +"\n\n"
    tmp += "* type(사업자유형) : null - 알수없음, 1 - 부가가치세 일반과세자, 2 - 부가가치세 면세과세자, 3 - 부가가치세 간이과세자, 4 - 비영리법인 또는 국가기관, 고유번호가 부여된 단체 " +"\n"
    tmp += "* state(사업자상태) : null - 알수없음, 0 - 등록되지 않은 사업자번호, 1 - 사업중, 2 - 폐업, 3 - 휴업 " +"\n"
    print(tmp)

except CloseDownException as CE:

    print("Exception Occur : [%d] %s" % (CE.code, CE.message))