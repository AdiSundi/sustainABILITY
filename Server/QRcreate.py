import qrcode

def createQR(unique_id, sku_id_product_name, date_manufacture, plastic_type):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )
    qr.add_data(str(unique_id) + " " + str(sku_id_product_name)+" "+str(date_manufacture)+" "+plastic_type)
    qr.make(fit=True)
    img = qr.make_image()
    with open('prod_'+str(unique_id)+'.png', 'wb') as f:
        img.save(f)

if __name__ == "__main__" :
    createQR("xyzSoap123q525_270221_HDPE_123qjo_56", "xyzSoap_100mL", "27/02/21", "HDPE")
