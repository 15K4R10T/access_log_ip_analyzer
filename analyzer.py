#!/bin/bash

echo "=== ACCESS LOG IP ANALYZER ==="
echo "File: access.log"
echo ""

# Ekstrak semua alamat IP dari file
echo "Ekstraksi semua alamat IP..."
grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}' access.log | sort | uniq -c | sort -nr > ip_counts.txt

# Tampilkan 10 IP teratas berdasarkan jumlah kemunculan
echo "10 IP teratas berdasarkan frekuensi:"
head -10 ip_counts.txt

# Cari pola akses mencurigakan
echo ""
echo "Mencari akses mencurigakan..."
grep -E '(login|admin|password|flag|ctf|hack|root|shell)' access.log | head -10

# Cari HTTP status code 404 atau 403 (akses gagal)
echo ""
echo "Mencari status kode error 404/403:"
grep -E ' 404 | 403 ' access.log | head -10

# Cari request yang mencurigakan
echo ""
echo "Mencari request mencurigakan:"
grep -E '(\.php\?|\.asp\?|\.jsp\?|\/etc\/passwd|\/etc\/shadow|\.\.\/|union\+select|exec\(|system\(|eval\>

# Cari user agent yang mencurigakan
echo ""
echo "Mencari user agent mencurigakan:"
grep -E '(sqlmap|nikto|nmap|wpscan|dirbuster|hydra|burpsuite)' access.log | head -10

# Tampilkan semua IP unik
echo ""
echo "Daftar semua IP unik:"
cat ip_counts.txt

echo ""
echo "File IP unik tersimpan di ip_counts.txt"
