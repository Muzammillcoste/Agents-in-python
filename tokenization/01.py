import tiktoken

init_obj = tiktoken.encoding_for_model('gpt-4')

message="Hello, how are you today?"

encoded_message=init_obj.encode(message)
print('encoded',encoded_message)

decode = init_obj.decode(encoded_message)
print('decoded',decode)
 