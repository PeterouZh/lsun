import data

def test_export_and_save_images():
    lmdb_path = 'bedroom/bedroom_val_lmdb'
    out_dir = 'bedroom/lsun_bedroom_val'
    flat = True
    data.export_and_save_images(lmdb_path, out_dir, flat)

def test_export_lsun_bedroom_train_images():
    lmdb_path = 'bedroom/bedroom_train_lmdb'
    out_dir = '/home/shhs/.keras/mydata/lsun/lsun_bedroom_train'
    flat = True
    data.export_and_save_images(lmdb_path, out_dir, flat)
