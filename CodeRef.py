import idautils
import ida_xref

def getCodeReference():
    for addr in idautils.CodeRefsFrom(4199689, 0):
        print(hex(addr), idc.GetDisasm(addr))

def cxref_from(ea):
    '''
    Simply show all the addresses which the passed address uses
    The difference b/w this function cxref_to(ea) and xref_to(ea) is that in here
    we are checking that each reference that is mentioned is the code reference not the data reference
    We are making sureit by using the .iscode
    '''
    print("this address is received: ", hex(ea))
    i = 0
    xrefblk = ida_xref.xrefblk_t()
    ok = xrefblk.first_from(ea, ida_xref.XREF_ALL)
    while ok and xrefblk.iscode:
        if i == 1:
            print("I'm going to return this: ",hex(xrefblk.to))
            return xrefblk.to
        ok = xrefblk.next_from()
        i = i + 1

getCodeReference()
addr = cxref_from(4199689)
print(idc.get_segm_name(addr)) # .idata
# 4199689
# 4202329
# 4219168
# 4202240