from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Function test failed!')

if capitalize('') != '':
    raise Exception('Function test failed!')

print('All tests passed!')