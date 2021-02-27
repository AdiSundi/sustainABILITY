import qrcode

def createQR(unique_id, sku_id, date_manufacture, plastic_type):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )
    qr.add_data(str(unique_id) + " " + str(sku_id)+" "+str(date_manufacture)+" "+plastic_type)
    qr.make(fit=True)
    img = qr.make_image()
    with open('prod_'+str(unique_id)+'.png', 'wb') as f:
        img.save(f)

if __name__ == "__main__" :
    createQR("abk123", "abk", "27/02/21", "HDPE")
