@auth.requires_membership('kepala_sekolah')
def tanda_terima_paket():
    import json as json
    sekolahan_saya = db((db.map_sekolah_kepala.id_kepala_sekolah==auth.user.id) &
        (db.map_sekolah_kepala.id_sekolah==db.m_sekolah.id)).select().as_list()
    paket_saya=[]
    nama_sekolah=""
    if len(sekolahan_saya)==1:
        id_sekolahan_saya=sekolahan_saya[0]['m_sekolah']['id']
        nama_sekolah=sekolahan_saya[0]['m_sekolah']['nama_sekolah']
        paket_saya = db((db.t_pemberian_paket.id_paket == db.m_paket.id) &
            (db.t_pemberian_paket.id_tujuan == id_sekolahan_saya) &
            (db.t_pemberian_paket.deleted == False)).select().as_list()
    form = SQLFORM.factory(
        Field('js', 'string')
        )
    if form.process(dbio=False).accepted:
        vv = json.loads(request.vars.js)
        print (vv)
        for i in vv:
            db.t_tanda_terima_paket.insert(id_t_pemberian_paket = i['id'], jumlah = i['jumlah'], 
                tanggal_terima = i['tanggal_terima'], id_user= auth.user.id)
    elif form.errors:
        response.flash = 'Ada kesalahan pengisian form'
    else:
        response.flash= "Silahkan isi"
    return dict(form = form, paket_saya = paket_saya, nama_sekolah=nama_sekolah)

@auth.requires_membership('kepala_sekolah')
def tanda_terima():
    import json as json
    sekolahan_saya = db((db.map_sekolah_kepala.id_kepala_sekolah==auth.user.id) &
        (db.map_sekolah_kepala.id_sekolah==db.m_sekolah.id)).select().as_list()
    paket_saya=[]
    nama_sekolah=""
    if len(sekolahan_saya)==1:
        id_sekolahan_saya=sekolahan_saya[0]['m_sekolah']['id']
        nama_sekolah=sekolahan_saya[0]['m_sekolah']['nama_sekolah']
        paket_saya = db((db.t_pemberian_paket.id_paket == db.m_paket.id) &
            (db.t_pemberian_paket.id_tujuan == id_sekolahan_saya) &
            (db.t_pemberian_paket.deleted == False)).select().as_list()
    form = SQLFORM.factory(
        Field('js', 'string')
        )
    if form.process(dbio=False).accepted:
        vv = json.loads(request.vars.js)
        print (vv)
        for i in vv:
            db.t_tanda_terima_paket.insert(id_t_pemberian_paket = i['id'], jumlah = i['jumlah'], 
                tanggal_terima = i['tanggal_terima'], id_user= auth.user.id)
    elif form.errors:
        response.flash = 'Ada kesalahan pengisian form'
    else:
        response.flash= "Silahkan isi"
    return response.json(dict(form = form, paket_saya = paket_saya, nama_sekolah=nama_sekolah))

@auth.requires_membership('kepala_sekolah')
def pengajuan_paket_makan():
    #mencari disdik dimana kepsek bertugas
    id_disdik = db((db.map_disdik_sekolah.id_sekolah == db.m_sekolah.id)&(db.map_disdik_sekolah.id_disdik == db.m_disdik.id) &
        (db.map_admin_disdik.id_disdik == db.m_disdik.id)&(db.map_admin_disdik.id_admin == db.auth_user.id) &
        (db.map_sekolah_kepala.id_sekolah == db.m_sekolah.id)&(db.map_sekolah_kepala.id_kepala_sekolah == auth.user.id)
        ).select().as_list()

    form = SQLFORM.factory(
        Field('paket_makan', 'integer', requires = IS_IN_DB(db, db.m_paket.id, '%(nama_paket)s')),
        Field('jumlah_paket', 'integer'),
        )

    if form.process(dbio=False).accepted:
        item = {}
        item['id_paket'] = request.vars.paket_makan
        item['id_pengaju'] = auth.user.id
        item['jumlah'] = request.vars.jumlah_paket
        item['id_approver'] = id_disdik[0]['auth_user']['id']
        db.t_pengajuan_paket.insert(**item)
    elif form.errors:
        response.flash = 'Ada kesalahan pengisian form'
    else:
        response.flash= "Silahkan isi"

    return dict(form = form)

@auth.requires_membership('super_admin')
def map_sekolah_disdik():
    form = SQLFORM.factory(
        Field ('nama_sekolah', 'integer', requires = IS_IN_DB(db, db.m_sekolah.id, '%(nama_sekolah)s')),
        Field ('nama_disdik', 'integer', requires = IS_IN_DB(db, db.m_disdik.id, '%(nama_disdik)s')),
        )
    if form.process(dbio=False).accepted:
        item = {}
        item['id_sekolah'] = request.vars.nama_sekolah
        item['id_disdik'] = request.vars.nama_disdik
        db.map_disdik_sekolah.insert(**item)
    return dict(form = form)

@auth.requires_membership('super_admin')
def map_sekolah_kepala():
    group = db(db.auth_group.role=='kepala_sekolah').select().as_list()
    daftar_total = db((db.auth_user.id == db.auth_membership.user_id) & (db.auth_membership.group_id==group[0]['id'])).select().as_list()
    daftar_kepsek = []
    for dt in daftar_total:
        daftar_kepsek.append( (dt['auth_user']['id'] , dt['auth_user']['first_name']+" "+ dt['auth_user']['last_name']) )

    form = SQLFORM.factory(
        Field ('nama_kepala_sekolah', 'integer', requires = IS_IN_SET(daftar_kepsek)),
        Field ('nama_sekolah', 'integer', requires = IS_IN_DB(db, db.m_sekolah.id, '%(nama_sekolah)s')),
        )

    if form.process(dbio=False).accepted:
        item = {}
        item['id_kepala_sekolah'] = request.vars.nama_kepala_sekolah
        item['id_sekolah'] = request.vars.nama_sekolah
        db.map_sekolah_kepala.insert(**item)
    return dict(form = form)


