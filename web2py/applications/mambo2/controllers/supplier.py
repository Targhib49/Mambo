
def map_supplier_user_id():
    group = db(db.auth_group.role=='supplier').select().as_list()
    daftar_total = db((db.auth_user.id == db.auth_membership.user_id) & (db.auth_membership.group_id==group[0]['id'])).select().as_list()
    daftar_supplier = []

    for dt in daftar_total:
        daftar_supplier.append( (dt['auth_user']['id'] , dt['auth_user']['first_name']+" "+ dt['auth_user']['last_name']) )

    form = SQLFORM.factory(
        Field ('nama_user', 'integer', requires = IS_IN_SET(daftar_supplier)),
        Field ('nama_supplier', 'integer', requires = IS_IN_DB(db, db.m_supplier.id, '%(nama_supplier)s')),
        )

    if form.process(dbio=False).accepted:
        item = {}
        item['id_user'] = request.vars.nama_user
        item['id_supplier'] = request.vars.nama_supplier
        db.map_supplier_user.insert(**item)
    return dict(form = form)    


@auth.requires_membership('supplier')
def item_supplier():
    form = SQLFORM.factory(
        Field('nama_barang', 'string', requires = IS_NOT_EMPTY('Harus diisi')),
        Field('harga', 'integer', requires = IS_NOT_EMPTY('Harus diisi')),
        Field('volume', 'integer', requires = IS_NOT_EMPTY('Harus diisi')),
        Field('satuan', 'integer', requires = IS_IN_DB(db, db.m_satuan_supplier.id, '%(nama_satuan)s')),
        )
    id_supplier = db(db.m_supplier.id_user==auth.user.id).select().as_list()[0]

    if form.process(dbio=False).accepted:
        item = {}
        item['nama_item'] = request.vars.nama_barang
        item['id_supplier'] = id_supplier['id']
        item['volume'] = request.vars.volume
        item['harga'] = request.vars.harga
        item['id_satuan_supplier'] = request.vars.satuan
        db.t_harga_supplier.insert(**item)
    else:
        response.flash= "Ada kesalahan dalam mengisi form"

    return dict(form = form)

def item_supplier_list():
    q = ( (db.t_harga_supplier.id_supplier == db.m_supplier.id)&
        (db.t_harga_supplier.id_satuan_supplier == db.m_satuan_supplier.id)        
        )
    grid = SQLFORM.grid(q)

    return dict(grid = q)