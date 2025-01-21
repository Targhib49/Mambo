
@auth.requires_membership('super_admin')
def map_admin_disdik_user_id():
    group = db(db.auth_group.role=='disdik_admin').select().as_list()
    daftar_total = db((db.auth_user.id == db.auth_membership.user_id) & (db.auth_membership.group_id==group[0]['id'])).select().as_list()
    daftar_admin = []
    for dt in daftar_total:
        daftar_admin.append( (dt['auth_user']['id'] , dt['auth_user']['first_name']+" "+ dt['auth_user']['last_name']) )

    form = SQLFORM.factory(
        Field ('nama_admin', 'integer', requires = IS_IN_SET(daftar_admin)),
        Field ('nama_disdik', 'integer', requires = IS_IN_DB(db, db.m_disdik.id, '%(nama_disdik)s')),
        )

    if form.process(dbio=False).accepted:
        item = {}
        item['id_admin'] = request.vars.nama_admin
        item['id_disdik'] = request.vars.nama_disdik
        db.map_admin_disdik.insert(**item)
    return dict(form = form)

@auth.requires_membership('super_admin')
def list_map_admin_disdik_user_id():
    fields = (db.m_disdik.nama_disdik, db.m_disdik.alamat, db.auth_user.first_name, db.auth_user.last_name)
    grid = SQLFORM.grid((db.map_admin_disdik.id_disdik==db.m_disdik.id) & (db.map_admin_disdik.id_admin==db.auth_user.id),
        fields = fields,
        create=False, deletable=False, csv=False, editable=False, details=False)
    return dict(grid = grid)



@auth.requires_membership('disdik_admin')
def persetujuan_paket():
    db.t_pengajuan_paket.time_stamp_setuju.readable=False
    db.t_pengajuan_paket.time_stamp.writeable=False
    query = ((db.t_pengajuan_paket.id_paket == db.m_paket.id)
        & (db.t_pengajuan_paket.approve == False)
        & (db.t_pengajuan_paket.id_pengaju == db.auth_user.id)
        & (db.t_pengajuan_paket.id_approver == auth.user.id)
        & (db.map_sekolah_kepala.id_kepala_sekolah == db.t_pengajuan_paket.id_pengaju)
        & (db.map_sekolah_kepala.id_sekolah == db.m_sekolah.id)
        )
    links = [
        dict(header='Setuju',body=lambda row: A("Setuju", _href = URL('disdik', 'approve', vars=dict(id=row.t_pengajuan_paket.id) ) ))
        ]
    fields = (db.t_pengajuan_paket.time_stamp, db.m_sekolah.nama_sekolah, db.m_paket.nama_paket, db.t_pengajuan_paket.jumlah)
    grid = SQLFORM.grid(query, links=links,
        fields = fields,
        create=False, deletable=False, csv=False, editable=False)
    return dict(grid=grid)

@auth.requires_membership('disdik_admin')
def approve():
    from datetime import datetime
    id = request.vars.id
    vendor_id = request.vars.nama_vendor
    query = ((db.t_pengajuan_paket.id_paket == db.m_paket.id)
        & (db.t_pengajuan_paket.approve == False)
        & (db.t_pengajuan_paket.id_pengaju == db.auth_user.id)
        & (db.t_pengajuan_paket.id_approver == auth.user.id)
        & (db.map_sekolah_kepala.id_kepala_sekolah == db.t_pengajuan_paket.id_pengaju)
        & (db.map_sekolah_kepala.id_sekolah == db.m_sekolah.id)
        & (db.t_pengajuan_paket.id == id)
        )

    pesanan = db(query).select().as_list()[0]

    form = SQLFORM.factory(
        Field('nama_vendor', 'integer', requires = IS_IN_DB(db, db.m_vendor.id, '%(nama_vendor)s')),
        )

    if form.process(dbio=False).accepted:
        db(db.t_pengajuan_paket.id==id).update(approve = True, time_stamp_setuju = datetime.now, id_vendor = vendor_id)
        redirect(URL('persetujuan_paket'))
    else:
        response.flash= "Ada kesalahan dalam mengisi form"
    return dict(form=form, pesanan = pesanan)

@auth.requires_membership('disdik_admin')
def pemberian_paket():
    form = SQLFORM.factory(
        Field('paket', 'integer', requires = IS_IN_DB(db, db.m_paket.id,'%(nama_paket)s' )),
        Field('jumlah', 'integer'),
        Field('tujuan', 'integer', requires = IS_IN_DB(db, db.m_sekolah.id,'%(nama_sekolah)s' )),
        )
    if form.process(dbio=False).accepted:
        dt={}
        dt['id_paket']=request.vars.paket
        dt['jumlah']=request.vars.jumlah
        dt['id_tujuan']=request.vars.tujuan
        dt['id_user']=auth.user.id
        db.t_pemberian_paket.insert(**dt)
    else:
        response.flash= "Ada kesalahan dalam mengisi form"

    return dict(form = form)

@auth.requires_membership('disdik_admin')
def pemberian_paket_apps():
    daftar_paket = db(db.m_paket).select(db.m_paket.id, db.m_paket.nama_paket, db.m_paket.pagu_harga).as_list()
    daftar_sekolah = db(db.m_sekolah).select(db.m_sekolah.id, db.m_sekolah.nama_sekolah).as_list()
    return dict(res = 'ok', daftar_paket=daftar_paket, daftar_sekolah= daftar_sekolah)

@auth.requires_membership('disdik_admin')
def pemberian_paket_submit_apps():
    dt={}
    dt['id_paket']=request.vars.paket
    dt['jumlah']=request.vars.jumlah
    dt['id_tujuan']=request.vars.tujuan
    dt['id_user']=auth.user.id
    db.t_pemberian_paket.insert(**dt)
    return dict(res = 'ok')

@auth.requires_membership('disdik_admin')
def daftar_pemberian_paket():
    # print('env', request.env)
    # print('client', request.client)
    q=((db.t_pemberian_paket.id_paket== db.m_paket.id) & 
        (db.t_pemberian_paket.id_tujuan==db.m_sekolah.id)&
        (db.t_pemberian_paket.id_user==auth.user.id))
    fields = (db.m_sekolah.nama_sekolah, db.m_paket.nama_paket, db.t_pemberian_paket.jumlah)
    grid = SQLFORM.grid((q), fields = fields,
        create=False, csv=False, editable=False, deletable=False, details=False)
    return dict(grid = grid)

@auth.requires_membership('disdik_admin')
def daftar_pemberian_paket_apps():
    q=((db.t_pemberian_paket.id_paket== db.m_paket.id) & 
        (db.t_pemberian_paket.id_tujuan==db.m_sekolah.id)&
        (db.t_pemberian_paket.id_user==auth.user.id))
    fields = (db.m_sekolah.nama_sekolah, db.m_paket.nama_paket, db.t_pemberian_paket.jumlah)
    daftar=db(q).select(db.m_sekolah.nama_sekolah, db.m_paket.nama_paket, db.t_pemberian_paket.jumlah).as_list()
    return dict(daftar = daftar, res='ok')

@auth.requires_membership('disdik_admin')
def daftar_penerimaan_paket():
    q=((db.t_pemberian_paket.id_paket== db.m_paket.id) & 
        (db.t_pemberian_paket.id_tujuan==db.m_sekolah.id)&
        (db.t_pemberian_paket.id_user==auth.user.id)&
        (db.t_tanda_terima_paket.id_t_pemberian_paket==db.t_pemberian_paket.id)&
        (db.t_tanda_terima_paket.id_user==db.auth_user.id)
        )

    fields = (db.m_sekolah.nama_sekolah, db.m_paket.nama_paket, db.t_pemberian_paket.jumlah,
        db.t_tanda_terima_paket.jumlah, db.t_tanda_terima_paket.tanggal_terima, 
        db.auth_user.first_name, db.auth_user.last_name)
    links = [
        dict(header='Penerima',body=lambda row: SPAN(row.auth_user.first_name+" "+row.auth_user.last_name))
        ]

    grid = SQLFORM.grid(q, fields = fields, links=links,
        create=False, csv=False, editable=False, deletable=False, details=False)

    return dict(grid = grid)

@auth.requires_membership('disdik_admin')
def daftar_penerimaan_paket_apps():
    q=((db.t_pemberian_paket.id_paket== db.m_paket.id) & 
        (db.t_pemberian_paket.id_tujuan==db.m_sekolah.id)&
        (db.t_pemberian_paket.id_user==auth.user.id)&
        (db.t_tanda_terima_paket.id_t_pemberian_paket==db.t_pemberian_paket.id)&
        (db.t_tanda_terima_paket.id_user==db.auth_user.id)
        )
    daftar = db(q).select(db.m_sekolah.nama_sekolah, db.m_paket.nama_paket, db.t_pemberian_paket.jumlah,
        db.t_tanda_terima_paket.jumlah, db.t_tanda_terima_paket.tanggal_terima, 
        db.auth_user.first_name, db.auth_user.last_name).as_list()
    return dict(daftar = daftar, res='ok')