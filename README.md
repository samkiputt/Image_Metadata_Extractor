# Image Metadata Extractor
Image Metadata Extractor adalah program Python yang digunakan untuk membaca dan mengambil informasi metadata atau EXIF yang tersimpan di dalam sebuah file foto.

Metadata EXIF dapat berisi informasi tambahan mengenai sebuah foto, seperti perangkat yang digunakan untuk mengambil foto, tanggal pengambilan foto, dan informasi lokasi GPS apabila data tersebut tersedia.

Project ini dibuat sebagai project pembelajaran Cyber Security untuk pemula, khususnya untuk memahami dasar-dasar metadata analysis, EXIF, GPS metadata, OSINT, Digital Forensics, dan penggunaan Python dalam keamanan siber.

# Features
- EXIF Metadata Extraction — mengambil metadata EXIF yang terdapat pada foto.
- Camera Information — menampilkan merek dan model perangkat atau kamera.
- Date & Time Extraction — menampilkan tanggal dan waktu pengambilan foto jika tersedia.
- GPS Metadata Extraction — membaca informasi GPS yang terdapat pada metadata foto.
- GPS Coordinate Conversion — mengubah koordinat GPS menjadi format desimal.
- Google Maps Link — membuat link Google Maps berdasarkan koordinat GPS.
- HEIC/HEIF Support — mendukung pembacaan file HEIC dan HEIF menggunakan pillow-heif.
- Multiple Image Formats — mendukung format JPG, JPEG, PNG, HEIC, dan HEIF.
- Terminal Interface — program dijalankan melalui terminal dengan input nama file foto.

# Technologies
- Python 3
- Pillow — untuk membuka gambar dan membaca metadata EXIF.
- Pillow-HEIF — untuk mendukung format HEIC dan HEIF.
- EXIF — untuk mengambil informasi metadata dari gambar.
- GPS Metadata — untuk membaca dan mengolah koordinat lokasi.

# Installation
