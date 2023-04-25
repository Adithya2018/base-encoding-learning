import base64

sample_string = "Python kicks Java's ass!"
sample_string_bytes = sample_string.encode("utf-8")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode('utf-8')

print(sample_string_bytes)
print(base64_bytes)
print(base64_string)
