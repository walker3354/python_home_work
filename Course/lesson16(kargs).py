# kargs = fimilar like args but it store as dictonary, format *kargs
# we can usr parameter[indx] to access the value
def hello(**test_args):
    print('greeting')
    print(f'{test_args['first_name']} {test_args['last_name']}')


hello(first_name='walker', last_name='frank')
