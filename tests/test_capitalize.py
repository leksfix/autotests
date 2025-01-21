from capitalize import capitalize

assert capitalize('hello') == 'Hello'
assert capitalize('') == ''
assert capitalize(None) is None

print('All tests passed!')