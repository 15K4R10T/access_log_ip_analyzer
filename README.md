# Manuals 
<pre>
./script.sh auth.log
=== ACCESS LOG IP ANALYZER ===
File: access.log

Ekstraksi semua alamat IP...
10 IP teratas berdasarkan frekuensi:
   1861 192.168.18.6

Mencari akses mencurigakan...
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /_admin HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /_vti_bin/_vti_adm/admin.dll HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /~admin HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /~administrator HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /~root HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /~sysadmin HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /acct_login HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /admin HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /admin.cgi HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /admin.php HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"

Mencari status kode error 404/403:
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /randomfile1 HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /frand2 HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /.bash_history HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /.bashrc HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /.cache HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /.config HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /.cvs HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /.cvsignore HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /.forward HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
192.168.18.6 - - [27/Apr/2025:12:55:29 +0000] "GET /.git/HEAD HTTP/1.1" 404 436 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"

Mencari request mencurigakan:

Mencari user agent mencurigakan:

Daftar semua IP unik:
   1861 192.168.18.6

File IP unik tersimpan di ip_counts.txt
</pre>

you can cat ip with 
cat ip_counts.txt

