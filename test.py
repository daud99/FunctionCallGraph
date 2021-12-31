def getMainEntryPoint():
    entry_points =  get_entry_qty()
    entry_point_id = entry_points - 1  # range id from 0 to get_entry_qty() -1
    entry_point_ordinal = get_entry_ordinal(entry_point_id)
    entry_point_name = get_entry_name(entry_point_ordinal)
    entry_point_ea = get_entry(entry_point_ordinal)  # ea => effective address
    return entry_point_name, entry_point_ea


name, ea = getMainEntryPoint()
print(name)
print(ea)
print(hex(ea))