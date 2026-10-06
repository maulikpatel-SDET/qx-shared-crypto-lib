# qx-shared-crypto-lib  (Repo 2 of 4)

Internal crypto wrapper library. Other repos call `sign_payload()` etc. and never
name the algorithm themselves. Installed by qx-payment-service via git URL
(see qx-payment-service/requirements.txt).

| File | Algorithm hidden inside | Test case |
|---|---|---|
| qx_crypto/signing.py | RSA-2048 PKCS#1 v1.5 | CR-05 |
| qx_crypto/constants.py | RSA key size 1024 (weak) | CR-11 |
