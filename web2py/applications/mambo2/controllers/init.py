def init_all():
	init_user()
	init_role_and_membership()
	return dict(a='b')

def init_user():
	db.auth_user.update_or_insert(db.auth_user.id==1, first_name='Super', last_name='Admin', email='super_admin@local.test')
	db(db.auth_user.id==1).validate_and_update(password='1234')

	db.auth_user.update_or_insert(db.auth_user.id==2, first_name='Kepala', last_name='Sekolah', email='kepala_sekolah@local.test')
	db(db.auth_user.id==2).validate_and_update(password='1234')

	db.auth_user.update_or_insert(db.auth_user.id==3, first_name='Disdik', last_name='Regional', email='disdik@local.test')
	db(db.auth_user.id==3).validate_and_update(password='1234')

	db.auth_user.update_or_insert(db.auth_user.id==4, first_name='Supplier', last_name='1', email='supplier1@local.test')
	db(db.auth_user.id==4).validate_and_update(password='1234')

	db.auth_user.update_or_insert(db.auth_user.id==5, first_name='Vendor', last_name='1', email='vendor1@local.test')
	db(db.auth_user.id==5).validate_and_update(password='1234')

	db.auth_user.update_or_insert(db.auth_user.id==6, first_name='Vendor', last_name='2', email='vendor2@local.test')
	db(db.auth_user.id==6).validate_and_update(password='1234')

	db.auth_user.update_or_insert(db.auth_user.id==7, first_name='Supplier', last_name='2', email='supplier2@local.test')
	db(db.auth_user.id==7).validate_and_update(password='1234')

	return dict(a='b')

def init_role_and_membership():
	db.auth_group.update_or_insert(db.auth_group.id==1, role = 'super_admin', description = 'Super Admin untuk Mambo')
	db.auth_group.update_or_insert(db.auth_group.id==2, role = 'kepala_sekolah', description = 'Kepala Sekolah')
	db.auth_group.update_or_insert(db.auth_group.id==3, role = 'disdik_admin', description = 'Admin dari Disdik Regional')
	db.auth_group.update_or_insert(db.auth_group.id==4, role = 'supplier', description = 'Supplier')
	db.auth_group.update_or_insert(db.auth_group.id==5, role = 'vendor', description = 'Vendor/Katering')
	auth.add_membership(1, 1)
	auth.add_membership(2, 2)	
	auth.add_membership(3, 3)	
	auth.add_membership(4, 4)
	auth.add_membership(5, 5)
	auth.add_membership(5, 6)
	auth.add_membership(4, 7)
	return dict(a='b')

def init_propinsi():
	return dict(a='b')
	