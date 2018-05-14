import re

sample = '"aseanbru@mfa.gov.bn" <aseanbru@mfa.gov.bn>, ASEAN Brunei2 <johariah.wahab@mfa.gov.bn>,ASEAN Brunei <aseanbrunei2014@gmail.com>, Nadiah Ahmad Rafie <nadiah.rafie@mfa.gov.bn>,Shahrul Anaz Hj Ismail <shahrulanaz.ismail@mfa.gov.bn>,Sothida Mak <msothida@gmail.com>, asean-indonesia@yahoo.com,'

result = sample.split(',')
print("result = ",result)

for each_thing in result:
    if '<' not in each_thing:
        print(each_thing)
    
result2 = re.findall("(?:[a-z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*)@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])",sample)    
print(result2)