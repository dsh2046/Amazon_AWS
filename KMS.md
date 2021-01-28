## AWS CLI
### Encrypt text
`aws kms encrypt --key-id ${YOUR_CMK_ID} --plaintext ${YOUR_TEXT}`
### Decrypt text
`aws kms decrypt --ciphertext-blob fileb://<(echo "{YOUR CIPHERTEXTBLOB HERE}" | base64 -d) --output text --query Plaintext | base64 -d`

### Encrypt file
`aws kms encrypt --key-id ${YOUR_CMK_ID} --plaintext fileb://${YOUR_FILE} --output text --query CiphertextBlob | base64 --decode > ExampleEncryptedFile`

### Decrypt file
`aws kms decrypt --ciphertext-blob fileb://ExampleEncryptedFile --output text --query Plaintext | base64 --decode > ExamplePlaintextFile`
