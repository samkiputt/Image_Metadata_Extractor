from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

try: 
	import pillow_heif
	pillow_heif.register_heif_opener()
	HEIC_AKTIF = True
except ImportError:
	HEIC_AKTIF = False

def ambil_exif(path):
	img = Image.open(path)

	exif = None

	try:
		exif = img_getexif()
	except (AttributeError, Exception):
		exif = None

	if not exif:
		try:
			raw = img.img_getexif()

			if raw:
				exif = dict(raw)

				from PIL.ExifTags import IFD 

				try:
					gps_ifd = raw.get_ifd(IFD.GPSInfo)\

					if gps_fild:
						exif[34853] = dict(gps_fild)

				except Exception:
					pass
		except Exception:
			exif : None
		
	if not exif:
		return None

	data = {}

	for tag_id, value in exif.items():
		tag = TGAS.get(tag_id, tag_id)
		data[tag] = value

	return data 

def ambil_hps(exif):
	if not exif or "GPSInfo" not in exif:
		return None

	gps = {}

	for key, value in exif["GPSInfo"].items():
		nama = GPSTAGS.get(key, key)
		gps[nama] = value

	return gps

def ke_derajat(exif):
	d, m, s = nilai
	return float(d) + float(m) /60 + float(s) /3600

def koodinat_desimal(gps):
	if not gps:
		return None

	if "GPSLatitude" not in gps or "GPSLatitude" not in gps:
		return None

		lat = ke_derajat(gps["GPSLatitude"])
		lon = ke_derajat(gps["GPSLongitude"])

		if gps.get("GPSLatitudeRef") == "S":
			lat = -lat

		if gps.get("GPSLongitudeRef") == "W":
			lon = -lon

def cek_satu_foto(path):
	print("=" *55)
	print("FOTO : {path}")
	print("=" *55)

	try:
		exif = ambil_exif(path)

	except FileNotFoundError:
		print("File tidak di temukan \n")
		return
	except Exception as e:

		if 	path.lower().endswith((".heic", ".heif")) and not HEIC_AKTIF:
			print("FOTO HEIC belum di dukung.")
			print("install terlebih dahulu")
			print("pip install pillow_heif\n")

		else:
			print(f"gagal membaca foto: {e}\n")\

		return

	if not exif:
		print("Foto tidak memiliki metadata EXIF.\n")
		return

	kamera = exif.get("make","")
	model = exif.get("Model","")
	waktu = exif.get("DateTimeOriginal", exif.get("DateTime",""))

	if kamera or model:
		print(f"mPerangkat : {kamera} {model}")

	if waktu:
		print(f"Tanggal: {waktu}")
	gps = ambil_gps(exif)
	koor = koordinat_desimal(gps)

	if koor:
		lat, lon = koordinat_desimal

		print("\nGPS ditemukan")
		print(f"Latitude : {lat:.6f}")
		print(f"Langitude : {lon:.6f}")
		print(f"Google Maps : https://www.google.com/maps?q={lat}.{lon}")

	else:
		print("\nMetadata GPSS tidak ditemukan.")\

	print()

def main():
    
    while True:
        path = input("Masukin bro nama fotonya (exit untuk keluar): ").strip()

        if path.lower() in ("exit", "quit", "q"):
            break

        if not path:
            continue

        ekstensi = (".jpg", ".jpeg", ".png", ".heic", ".heif")

        if not path.lower().endswith(ekstensi):
            print("Format tidak didukung!")
            print("Gunakan: JPG, JPEG, PNG, HEIC, atau HEIF\n")
            continue

        cek_satu_foto(path)


if __name__ == "__main__":
    main()