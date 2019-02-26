# dnsbrute

This script include mutliple dns enumeration/bruteforce tools for subdomain discovery

1. Recong-ng
2. Altdns
3. Sublister

Flow:

1) Brute with recon-ng
2) Enum with aquatone (passivetotal, shodan, censys, ridler, virustotal)
3) Enum with subl1st3r
4) Extract unique subdomains from previous results, run altdns on final results.
5) Save and run altdns again.
