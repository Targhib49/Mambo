@auth.requires_membership('super_admin')
def master_supplier():
    grid = SQLFORM.grid(db.m_supplier, create=True, csv=False)
    return dict(grid = grid)

def master_vendor():
    grid = SQLFORM.grid(db.m_vendor, create=True, csv=False)
    return dict(grid = grid)

@auth.requires_membership('super_admin')
def master_sekolah():
    grid = SQLFORM.grid(db.m_sekolah, create=True, csv=False)
    return dict(grid = grid)

@auth.requires_membership('super_admin')
def master_disdik():
    grid = SQLFORM.grid(db.m_disdik, create=True, csv=False)
    return dict(grid = grid)

@auth.requires_membership('super_admin')
def master_paket():
    grid = SQLFORM.grid(db.m_paket, create=True, csv=False)
    return dict(grid = grid)

@auth.requires_membership('super_admin')
def master_satuan_menu():
    grid = SQLFORM.grid(db.m_satuan_menu, create=True, csv=False)
    return dict(grid = grid)

@auth.requires_membership('super_admin')
def master_satuan_supplier():
    grid = SQLFORM.grid(db.m_satuan_supplier, create=True, csv=False)
    return dict(grid = grid)

def test():
    x= db(db.m_satuan_menu).select().as_list()
    return dict(id=10, nama='halo', tabel = x)