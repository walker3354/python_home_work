# Or we can use

import test_folder.test_module as ts
# use "as" we can name a new abbreviation to this module
# test_folder.test_module.method() => ts.method()

usr_name = 'frank'
ts.greeting(usr_name)
ts.bye(usr_name)
