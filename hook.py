#!/usr/bin/env python

import sys
import time

from digitalocean import ClientV2

do_key = "0661fbe5daf4d755fb3063512068dba5cd5082da3c928958337d9858fa15d856"

command = sys.argv[1]
domain = sys.argv[2]

if command == "deploy_challenge":

    challenge = sys.argv[3]

    client = ClientV2(token=do_key)
    domain_record = client.domains.get(domain)
    if domain_record:
        name = "_acme-challenge"
        new_record = client.domains.create_domain_record(domain, 'TXT', name, challenge, )

    time.sleep(15)


if command == "clean_challenge":

    challenge = sys.argv[3]

    client = ClientV2(token=do_key)
    domain_records = client.domains.list_domain_records(domain)
    for record in domain_records['domain_records']:
        if record['type'] == 'TXT' and record['data'] == challenge:
            pass
            #client.domains.delete_domain_record(domain, record['id'])

if command == "deploy_cert":
    pass

time.sleep(5)

sys.exit(0)
