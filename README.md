# sat6_package_profile
Project to compare the packages installed between two hosts registered on the Satellite 6.

Currently we are doing the API call on Satellite to check the Content Host installed packages, compare then and then create a report.

Below a simple example:
```
$ ./package_profile.py 
Type the First CH fqdn: node005.local.domain
Type the Second CH fqdn: refnode01.local.domain
Package,Fist System,Second System,Difference
dbus,1.6.12-17,1.10.24-13,lower on node005.local.domain
dbus-libs,1.6.12-17,1.10.24-13,lower on node005.local.domain
katello-ca-consumer-sat64.local.domain,1.0-2,1.0-3,lower on node005.local.domain
openssl,1.0.2k-16,1.0.2k-8,greater on node005.local.domain
openssl-libs,1.0.2k-16,1.0.2k-8,greater on node005.local.domain
python,2.7.5-77,2.7.5-58,greater on node005.local.domain
python-dmidecode,3.12.2-3,3.12.2-1,greater on node005.local.domain
python-libs,2.7.5-77,2.7.5-58,greater on node005.local.domain
subscription-manager,1.21.10-3,1.19.21-1,greater on node005.local.domain
yum,3.4.3-161,3.4.3-154,greater on node005.local.domain
axel,2.4-9,-,only on node005.local.domain
iptraf-ng,1.1.4-7,-,only on node005.local.domain
open-vm-tools,10.2.5-3,-,only on node005.local.domain
python-backports,1.0-8,-,only on node005.local.domain
python-backports-ssl_match_hostname,3.5.0.1-1,-,only on node005.local.domain
python-inotify,0.9.4-4,-,only on node005.local.domain
python-ipaddress,1.0.16-2,-,only on node005.local.domain
python-setuptools,0.9.8-7,-,only on node005.local.domain
subscription-manager-rhsm,1.21.10-3,-,only on node005.local.domain
subscription-manager-rhsm-certificates,1.21.10-3,-,only on node005.local.domain
bzip2,1.0.6-13,-,only on refnode01.local.domain
libyaml,0.1.4-11,-,only on refnode01.local.domain
openscap,1.2.17-2,-,only on refnode01.local.domain
openscap-scanner,1.2.17-2,-,only on refnode01.local.domain
python-rhsm,1.19.9-1,-,only on refnode01.local.domain
python-rhsm-certificates,1.19.9-1,-,only on refnode01.local.domain
ruby,2.0.0.648-34,-,only on refnode01.local.domain
rubygem-bigdecimal,1.2.0-34,-,only on refnode01.local.domain
rubygem-foreman_scap_client,0.3.0-3,-,only on refnode01.local.domain
rubygem-io-console,0.4.2-34,-,only on refnode01.local.domain
rubygem-json,1.7.7-34,-,only on refnode01.local.domain
rubygem-psych,2.0.0-34,-,only on refnode01.local.domain
rubygem-rdoc,4.0.0-34,-,only on refnode01.local.domain
rubygems,2.0.14.1-34,-,only on refnode01.local.domain
ruby-irb,2.0.0.648-34,-,only on refnode01.local.domain
ruby-libs,2.0.0.648-34,-,only on refnode01.local.domain
```
If we add the same machine, then will be expected to see no difference
```
$ ./package_profile.py 
Type the First CH fqdn: refnode01.local.domain
Type the Second CH fqdn: refnode01.local.domain
Package,Fist System,Second System,Difference
$ 
```

A lot of things to improve, however, it's a great start point! Hope you enjoy it.