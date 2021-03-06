# zschema sub-schema for zgrab2's pop3 module
# Registers zgrab2-pop3 globally, and pop3 with the main zgrab2 schema.
from zschema.leaves import *
from zschema.compounds import *
import zschema.registry

import schemas.zcrypto as zcrypto
import schemas.zgrab2 as zgrab2

pop3_scan_response = SubRecord({
    "result": SubRecord({
        "banner": String(),
        "noop": String(),
        "help": String(),
        "starttls": String(),
        "quit": String(),
        "tls": zgrab2.tls_log,
    })
}, extends=zgrab2.base_scan_response)

zschema.registry.register_schema("zgrab2-pop3", pop3_scan_response)

zgrab2.register_scan_response_type("pop3", pop3_scan_response)
