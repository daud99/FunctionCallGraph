import json

from idaapi import *
from idautils import *
import ida_xref


queue = []
nodes = []
edges = []

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





def getMainEntryPoint():
    entry_points =  get_entry_qty()
    entry_point_id = entry_points - 1  # range id from 0 to get_entry_qty() -1
    entry_point_ordinal = get_entry_ordinal(entry_point_id)
    entry_point_name = get_entry_name(entry_point_ordinal)
    entry_point_ea = get_entry(entry_point_ordinal)  # ea => effective address
    return entry_point_name, entry_point_ea

def getFunctionStartEndAddress(ea):
    func = idaapi.get_func(ea)
    return func.start_ea, func.end_ea

def printEntireFunctionIntructoins(ea, parent):
    start = idc.get_func_attr(ea, FUNCATTR_START)
    end = idc.get_func_attr(ea, FUNCATTR_END)
    cur_addr = start
    while cur_addr <= end:
        if idc.print_insn_mnem(cur_addr) == "call":
            print(hex(cur_addr), idc.GetDisasm(cur_addr))
            address = cxref_from(cur_addr)
            print(idc.get_segm_name(address))
            print(str(idc.get_segm_name(address)))
            print(str(idc.get_segm_name(address)) == ".idata")

            if not str(idc.get_segm_name(address)) == ".idata":
                func_name = idc.get_func_name(address)
                nodes.append(func_name)
                edges.append((parent, func_name))
                queue.append([address, func_name])
            else:
                func_name = str(idc.GetDisasm(cur_addr))[4:].strip()
                nodes.append(func_name)
                edges.append((parent, func_name))
        cur_addr = idc.next_head(cur_addr, end)
        # print("below")
        # print(queue)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name, ea = getMainEntryPoint()
    # ea = 4199680
    nodes.append("Entry Point")
    queue.append([ea, "Entry Point"])
    while True:
        e = queue.pop(0)
        printEntireFunctionIntructoins(e[0], e[1])
        print(len(queue))
        if len(queue) == 0:
            break
    print("Node are")
    print(nodes)
    print("Edges are")
    print(edges)
    graph = {"edges": edges, "nodes": nodes}
    with open('graph.json', 'w') as out:
        out.write((json.dumps(graph, indent=4)))
