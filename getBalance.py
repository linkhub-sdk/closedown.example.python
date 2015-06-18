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
    print("휴폐업조회 잔여포인트 확인")

    balance = closedownChecker.getBalance()

    print("잔여 포인트 : %f" % balance)
except CloseDownException as CE:

    print("Exception Occur : [%d] %s" % (CE.code, CE.message))