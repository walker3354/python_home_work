from test_folder.test_module import greeting
# we use from + import that means we only want to use some part of this module not all

usr_name = 'frank'
greeting(usr_name)

# bye(usr_name) <- error  if we want to fix it we have to use "from test_folder.test_modulle import greeting,bye"
