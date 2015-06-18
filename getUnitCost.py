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
    print("휴폐업조회 조회 단가 확인")

    unitCost = closedownChecker.getUnitCost()

    print("조회 단가 : %f" % unitCost)
except CloseDownException as CE:

    print("Exception Occur : [%d] %s" % (CE.code, CE.message))