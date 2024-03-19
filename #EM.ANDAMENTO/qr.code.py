pip install qrcode
import qrcode

# Texto a ser decodificado
texto_qr = "SeuTextoAqui"

# Criação o objeti QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qr.code.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adiciona os dados ao QR Code
qr.add_data(texto_qr)
qr.make(fit=True)

# Criação de uma imagem do Qr Code

img = qr.make.image(fill.color="black",back_color="white")

# Salve a imagem do QR Code
img.save("seu_qrcode.png")