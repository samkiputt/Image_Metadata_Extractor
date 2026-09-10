from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS, IFD

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HEIC_AKTIF = True
except ImportError:
    HEIC_AKTIF = False


def ambil_exif(path):
    img = Image.open(path)
    raw = img.getexif()

    if not raw:
        return None

    data = {}

    for tag_id, value in raw.items():
        tag = TAGS.get(tag_id, tag_id)
        if tag == "GPSInfo":
            continue  # pointer int, GPS dibaca terpisah di bawah
        data[tag] = value

    # GPS IFD - dibaca lewat get_ifd, bukan dari value tag GPSInfo
    try:
        gps_ifd = raw.get_ifd(IFD.GPSInfo)
        if gps_ifd:
            data["GPSInfo"] = dict(gps_ifd)
    except Exception:
        pass

    return data


def ambil_gps(exif):
    if not exif or "GPSInfo" not in exif:
        return None

    gps = {}
    for key, value in exif["GPSInfo"].items():
        nama = GPSTAGS.get(key, key)
        gps[nama] = value

    return gps


def ke_derajat(nilai):
    d, m, s = nilai
    return float(d) + float(m) / 60 + float(s) / 3600


def koordinat_desimal(gps):
    if not gps:
        return None

    if "GPSLatitude" not in gps or "GPSLongitude" not in gps:
        return None

    lat = ke_derajat(gps["GPSLatitude"])
    lon = ke_derajat(gps["GPSLongitude"])

    if gps.get("GPSLatitudeRef") == "S":
        lat = -lat

    if gps.get("GPSLongitudeRef") == "W":
        lon = -lon

    return lat, lon


def cek_satu_foto(path):
    print("=" * 55)
    print(f"FOTO : {path}")
    print("=" * 55)

    try:
        exif = ambil_exif(path)

    except FileNotFoundError:
        print("File tidak ditemukan\n")
        return

    except Exception as e:
        if path.lower().endswith((".heic", ".heif")) and not HEIC_AKTIF:
            print("FOTO HEIC belum didukung.")
            print("Install terlebih dahulu:")
            print("pip install pillow_heif\n")
        else:
            print(f"Gagal membaca foto: {e}\n")
        return

    if not exif:
        print("Foto tidak memiliki metadata EXIF.\n")
        return

    kamera = exif.get("Make", "")
    model = exif.get("Model", "")
    waktu = exif.get("DateTimeOriginal", exif.get("DateTime", ""))

    if kamera or model:
        print(f"Perangkat : {kamera} {model}")

    if waktu:
        print(f"Tanggal : {waktu}")

    gps = ambil_gps(exif)
    koor = koordinat_desimal(gps)

    if koor:
        lat, lon = koor

        print("\nGPS ditemukan")
        print(f"Latitude : {lat:.6f}")
        print(f"Longitude : {lon:.6f}")
        print(f"Google Maps : https://www.google.com/maps?q={lat},{lon}")

    else:
        print("\nMetadata GPS tidak ditemukan.")

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
