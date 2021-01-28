### Encrypt text
`aws kms encrypt --key-id ${YOUR_CMK_ID} --plaintext ${YOUR_TEXT}`
### Decrypt text
`aws kms decrypt --ciphertext-blob fileb://<(echo "{YOUR CIPHERTEXTBLOB HERE}" | base64 -d) --output text --query Plaintext | base64 -d`
