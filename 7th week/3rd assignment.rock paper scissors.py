import random
options_list = ['rock','paper','scissors']
scissors = ('      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'     ⠀⠀⢀⣤⠶⠿⣶⣤⡶⠟⠛⠉⠉⠉⢉⡉⠙⠛⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀                                \n'
'    ⠀⠀⣰⡟⠁⢠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀ ⠙⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                      \n'
'    ⠀⣰⡏⠀⣰⡟⠀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣄ ⣸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 \n'
'    ⢠⡟⠀⣰⡟⠀⣄⠈⠉⠛⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠳⠶⠶⠶⠶⣤⣭⣭⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'    ⢸⡇⢀⣿⠁⢠⠛⠿⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'    ⠘⣷⣼⣇⠀⠘⢷⣄⡀⠈⠙⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'    ⠀⠈⠉⢿⡆⠀⠀⠙⠻⠆⠀⠀⠀⠀⠀⠘⠒⠒⠒⠶⢶⣶⣶⣤⣤⣤⣤⣤⣀⣀⣀   ⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'      ⠀⠀⠘⢿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'       ⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'        ⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠉⠛⠲⢶⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'           ⠀⠀⠀⠀⠙⠻⠶⣦⣤⣄⣠⣤⣤⠶⠟⠋⠉⠛⠳⢶⣤⣀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'                                ⠉⠛⠷⣦⣄⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀\n'
'                                 ⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀\n')
paper = (
'                          ⢀⣀⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'                        ⢠⣾⠟⠉⠀⠈⠙⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀\n'
'                       ⣴⠟⠁⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀\n'
'      ⢠⣴⠶⠶⠶⣦         ⣠⣾⠋⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⣀⣀⣀⡀⠀⠀⠀\n'
'      ⢸⡇ ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⢀⣼⠏⢀⣠⡶⠟⠋⠉⠉⠛⢷⣄⠀\n'
'      ⠸⣧⠀ ⠀⠀⠀⠀⢻⡇⠀⠀⣠⡿⠃⠀⠀⠀⠀⢠⣾⣧⠾⠛⠉⠀⠀     ⢈⣿⠀\n'
'       ⢻⣇  ⠀⠀⠀⠘⣇⣴⡾⠋⠀⠀⠀⠀⠀⣰⡿⠛⠁⠀      ⠀⣀⣴⠟⠋⠀\n'
'      ⠀⠀⣿⡇⠀⠀⠀⠀ ⠟⠁⠀⠀⠀⠀⠀⠀⣸⠋⠀⠀⠀⠀⠀⠀  ⣀⣴⠿⠋⠁⠀⠀⠀\n'
'     ⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀   ⢀⣤⠾⠋⣀⣠⣤⣤⣤⣄⡀\n'
'     ⠀⠀⠀⡿⠀                   ⣴⠿⠛⠛⠛    ⠙⣿\n'
'     ⠀⢀⣼⡇⠀⠀⠀⢀⣴⡄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀  ⣰⠟⠁⠀⠀⠀⠀⠀⠀⣀⣤⡾⠏\n'
'     ⠀⡿ ⣷⠀⢀⣴⡿⠋⢀⣴⠿⠁          ⠀⠀⢀⣠⣴⠾⠛⠉⠁⠀⠀\n'
'      ⣷ ⢻⣧⠈⠁⢀⣤⡾⠋⠁⢀⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀\n'
'      ⠹⣇⠀⠹⣷⡀⠉⠁⣤⣴⠶⠛⠀⠀  ⣀⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'       ⠹⣧ ⠈⢿⣦⡀     ⣀⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'        ⠈⠻⣦⣈⣻⡷⠶⣶⣶⡶⠶⠾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')
rock = (
'                ⢀⣀⣀⣤⣄⣀⣀⡀⠀ \n'
'	⠀⠀⠀⠀⠀⠀⢠⣶⠟⠉⠁⠀⣠⠉⠉⠛⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'	⠀⠀⠀⠀⠀⢰⡿⠁⠀⣀⣠⠞⠁⠀⠀⠀⠀⠀⠉⠻⣶⡶⠶⣦⡀⠀⠀⠀⠀\n'
'	⠀⣠⡶⠟⠛⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠈⢿⡄⠀\n'
'	⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣶⠈⣿⡀⠘⣷\n'
'	⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢀⣀⡀⠹⣧⠀⢻⡄\n'
'	⠀⣼⡿⠶⠦⠤⠤⠤⠀⠀⠀⠀⠀⠀⢠⣤⡶⠶⠞⠛⢋⡁⠀⣿⠀⢸⡧⠀\n'
'	⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠟⠃⢀⣿⢀⣾⠁⠀⠀\n'
'	⢸⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⢀⣿⡛⠛⠁⠀⠀\n'
'	⠈⠻⣶⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀\n'
'	⠀⠀⠀⢹⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠟⠋⠀\n'
'	⠀⠀⠀⠀⠙⠿⣶⣤⣤⣀⣀⣠⣤⣴⡶⠾⠛⠉ \n')

print('⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⢠⣶⠟⠉⠁⠀⣠⠉⠉⠛⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠉⠀⠈⠙⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⢰⡿⠁⠀⣀⣠⠞⠁⠀⠀⠀⠀⠀⠉⠻⣶⡶⠶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⣠⡶⠟⠛⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠈⢿⡄⠀⢠⣴⠶⠶⠶⣦⣄⠀⠀⠀⠀⠀⠀⠀⣠⣾⠋⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⣀⣀⣀⡀⠀⠀⠀\n'
'⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣶⠈⣿⡀⠘⣷⠀⢸⡇⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⢀⣼⠏⢀⣠⡶⠟⠋⠉⠉⠛⢷⣄⠀\n'
'⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢀⣀⡀⠹⣧⠀⢻⡄⠸⣧⠀⠀⠀⠀⠀⢻⡇⠀⠀⣠⡿⠃⠀⠀⠀⠀⠀⢠⣾⣧⠾⠛⠉⠀⠀⠀⠀⠀⠀⢈⣿⠀\n'
'⠀⣼⡿⠶⠦⠤⠤⠤⠀⠀⠀⠀⠀⠀⢠⣤⡶⠶⠞⠛⢋⡁⠀⣿⠀⢸⡧⠀⢻⣇⠀⠀⠀⠀⠘⣇⣴⡾⠋⠀⠀⠀⠀⠀⠀⣰⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⠀\n'
'⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠟⠃⢀⣿⢀⣾⠁⠀⠀⣿⡇⠀⠀⠀⠀⠟⠁⠀⠀⠀⠀⠀⠀⠀⣸⠋⠀⠀⠀⠀⠀⠀⠀⣀⣴⠿⠋⠁⠀⠀⠀\n'
'⢸⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⢀⣿⡛⠛⠁⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⢀⣤⠾⠋⣀⣠⣤⣤⣤⣄⡀\n'
'⠈⠻⣶⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⠀⠀⠀⠂⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠛⠛⠛⠉⠉⠁⠀⠀⠙⣿\n'
'⠀⠀⠀⢹⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠟⠋⠀⠀⠀⠀⠀⠀⢀⣼⡇⠀⠀⠀⢀⣴⡄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠏\n'
'⠀⠀⠀⠀⠙⠿⣶⣤⣤⣀⣀⣠⣤⣴⡶⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠉⣷⠀⢀⣴⡿⠋⠀⢀⣴⠿⠁⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⢀⣠⣴⠾⠛⠉⠁⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣀⣀⣀⡀⠀⠀⠀⠀⠀⠁⣷⠀⢻⣧⠈⠁⢀⣤⡾⠋⠁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⢀⣤⠶⠿⣶⣤⡶⠟⠛⠉⠉⠉⢉⡉⠙⠛⢷⣦⡀⠀⠀⠀⠹⣇⠀⠹⣷⡀⠉⠁⣤⣴⠶⠛⠋⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⣰⡟⠁⢠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠙⢿⡄⠀⠀⠀⠹⣧⡀⠈⢿⣦⡀⠁⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⣰⡏⠀⣰⡟⠀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣄⣸⣇⠀⠀⠀⠀⠈⠻⣦⣄⣈⣻⡷⠶⣶⣶⡶⠶⠾⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⢠⡟⠀⣰⡟⠀⣄⠈⠉⠛⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠳⠶⠶⠶⠶⣤⣭⣭⣋⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⢸⡇⢀⣿⠁⢠⠛⠿⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠘⣷⣼⣇⠀⠘⢷⣄⡀⠈⠙⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠈⠉⢿⡆⠀⠀⠙⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠒⠒⠶⢶⣶⣶⣤⣤⣤⣤⣤⣀⣀⣀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠘⢿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠉⠛⠲⢶⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠶⣦⣤⣄⣠⣤⣤⠶⠟⠋⠉⠛⠳⢶⣤⣀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⣦⣄⡀⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\n\n')
print(' whale cum to my rock paper scissors game!')
while True :
    x = input(" press 's' to start the game and 'q' to quit :")
    if x == 's' :
        while True :
            print('\n a. versus match')
            print(' b. computer math \n')
            x = input('please choose an option: ')
            if x == 'a' :
                while True :
                    print('\n a. 1 round match')
                    print(' b. 3 round match')
                    print(' c. 5 round match\n')
                    x = input('please choose an option: ')
                    if x == 'a' :
                        print('\n a. rock')
                        print(' b. paper')
                        print(' c. scissors\n')
                        p1 = input('player1,please choose an option: ')
                        print('\n a. rock')
                        print(' b. paper')
                        print(' c. scissors\n')
                        p2 = input('player2,please choose an option: ')
                        if ((p1 == 'a' and p2 == 'c') or (p1 == 'b' and p2 == 'a') or (p1 == 'c' and p2 == 'b')) :
                            print("\n player1 won this round! \n")
                            print("game over\n")
                            break
                        elif ((p2 == 'a' and p1 == 'c') or (p2 == 'b' and p1 == 'a') or (p2 == 'c' and p1 == 'b')) :
                            print("\n player2 won this round! \n")
                            print("game over\n")
                            break
                        elif ((p1 == 'a' and p2 == 'a') or (p1 == 'b' and p2 == 'b') or (p1 == 'c' and p2 == 'c')) :
                            print("\n player1 and player2 tied this round! \n")
                            print("game over\n")
                            break
                        else :
                            print('\n invalid! \n')      
                        break
                    elif x == 'b' :
                        counter1 = 0
                        counter2 = 0
                        counter3 = 0
                        for i in range(3) :
                            while True :
                                print('\n a. rock')
                                print(' b. paper')
                                print(' c. scissors\n')
                                p1 = input('player1,please choose an option: ')
                                if not(p1 == 'a' or p1 == 'b' or p1 == 'c') :
                                    continue
                                elif (p1 == 'a' or p1 == 'b' or p1 == 'c') :
                                    break
                            while True :
                                print('\n a. rock')
                                print(' b. paper')
                                print(' c. scissors\n')
                                p2 = input('player2,please choose an option: ')
                                if not(p2 == 'a' or p2 == 'b' or p2 == 'c') :
                                    continue
                                elif (p2 == 'a' or p2 == 'b' or p2 == 'c') :
                                    break
                            if ((p1 == 'a' and p2 == 'c') or (p1 == 'b' and p2 == 'a') or (p1 == 'c' and p2 == 'b')) :
                                print("\n player1 won this round! \n")
                                counter1 += 1
                                continue
                            elif ((p2 == 'a' and p1 == 'c') or (p2 == 'b' and p1 == 'a') or (p2 == 'c' and p1 == 'b')) :
                                print("\n player2 won this round! \n")
                                counter2 += 1
                                continue
                            elif ((p1 == 'a' and p2 == 'a') or (p1 == 'b' and p2 == 'b') or (p1 == 'c' and p2 == 'c')) :
                                print("\n player1 and player2 tied this round! \n")
                                counter3 += 1
                                continue
                            else :
                                print('\n invalid! \n')
                        if counter1 > counter2 :
                            print("\n player1 won in total")
                            print(' your total score is',(counter1 - counter2),'\n') 
                        elif counter2 > counter1 :
                            print("\n player2 won in total")
                            print(' your total score is',(counter2 - counter1),'\n')
                        elif counter3 == 3 :
                            print("\n player1 and player2 are tied in total")
                            print(" player1 total score is",counter1,'\n')
                            print(" player2 total score is",counter2,'\n')
                        print("game over\n")
                        break
                    elif x == 'c' :
                        counter1 = 0
                        counter2 = 0
                        counter3 = 0
                        for i in range(5) :
                            while True :
                                print('\n a. rock')
                                print(' b. paper')
                                print(' c. scissors\n')
                                p1 = input('player1,please choose an option: ')
                                if not(p1 == 'a' or p1 == 'b' or p1 == 'c') :
                                    continue
                                elif (p1 == 'a' or p1 == 'b' or p1 == 'c') :
                                    break 
                            while True :
                                print('\n a. rock')
                                print(' b. paper')
                                print(' c. scissors\n')
                                p2 = input('player2,please choose an option: ')
                                if not(p2 == 'a' or p2 == 'b' or p2 == 'c') :
                                    continue
                                elif (p2 == 'a' or p2 == 'b' or p2 == 'c') :
                                    break
                            if ((p1 == 'a' and p2 == 'c') or (p1 == 'b' and p2 == 'a') or (p1 == 'c' and p2 == 'b')) :
                                print("\n player1 won this round! \n")
                                counter1 += 1
                                continue
                            elif ((p2 == 'a' and p1 == 'c') or (p2 == 'b' and p1 == 'a') or (p2 == 'c' and p1 == 'b')) :
                                print("\n player2 won this round! \n")
                                counter2 += 1
                                continue
                            elif ((p1 == 'a' and p2 == 'a') or (p1 == 'b' and p2 == 'b') or (p1 == 'c' and p2 == 'c')) :
                                print("\n player1 and player2 tied this round! \n")
                                counter3 += 1
                                continue
                            else :
                                print('\n invalid! \n')
                        if counter1 > counter2 :
                            print("\n player1 won in total")
                            print(' your total score is',(counter1 - counter2),'\n') 
                        elif counter2 > counter1 :
                            print("\n player2 won in total")
                            print(' your total score is',(counter2 - counter1),'\n')
                        elif counter3 == 3 :
                            print("\n player1 and player2 are tied in total")
                            print(" player1 total score is",counter1,'\n')
                            print(" player2 total score is",counter2,'\n')
                        break
                    else :
                        print('\n invalid! \n')
                break
            elif x == 'b' :
                while True :
                    print('\n a. 1 round match')
                    print(' b. 3 round match')
                    print(' c. 5 round match\n')
                    x = input('please choose an option: ')
                    if x == 'a' :
                        while True :
                            print('\n a. rock')
                            print(' b. paper')
                            print(' c. scissors\n')
                            z = input('choose rock,paper or scissors: ')
                            num = random.randint(0,2)
                            y = options_list[num]
                            print('\n',y)
                            if ((y == 'scissors' and z == 'a') or (y == 'rock' and z == 'b') or (y == 'paper' and z == 'c')) :
                                if y == 'scissors' :
                                    print(scissors)
                                elif y == 'rock' :
                                    print(rock)
                                elif y == 'paper' :
                                    print(paper)
                                print("\n you've won! \n")
                                print("game over\n")
                                break                    
                            elif ((y == 'scissors' and z == 'b') or (y == 'rock' and z == 'c') or (y == 'paper' and z == 'a')) :
                                if y == 'scissors' :
                                    print(scissors)
                                elif y == 'rock' :
                                    print(rock)
                                elif y == 'paper' :
                                    print(paper)
                                print("\n you've lost! \n")
                                print('game over\n')
                                break
                            elif  ((y == 'scissors' and z == 'c') or (y == 'rock' and z == 'a') or (y == 'paper' and z == 'b')) :
                                if y == 'scissors' :
                                    print(scissors)
                                elif y == 'rock' :
                                    print(rock)
                                elif y == 'paper' :
                                    print(paper)
                                print("\n you are tied!\n")
                                print('game over \n')
                                break
                            else :
                                print('\n invalid! \n')
                                break
                    elif x == 'b' :
                        counter1 = 0
                        counter2 = 0
                        counter3 = 0
                        while True :    
                            print('\n a. rock')
                            print(' b. paper')
                            print(' c. scissors\n')
                            if (counter1 + counter2 + counter3) == 3 :
                                break
                            z = input('choose rock,paper or scissors: ')
                            num = random.randint(0,2)
                            y = options_list[num]
                            if ((y == 'scissors' and z == 'a') or (y == 'rock' and z == 'b') or (y == 'paper' and z == 'c')) :
                                if y == 'scissors' :
                                    print(scissors)
                                elif y == 'rock' :
                                    print(rock)
                                elif y == 'paper' :
                                    print(paper)
                                print('\n',y)
                                print("\n you've won! \n")
                                counter1 += 1
                                continue
                            elif ((y == 'scissors' and z == 'b') or (y == 'rock' and z == 'c') or (y == 'paper' and z == 'a')) :
                                if y == 'scissors' :
                                    print(scissors)
                                elif y == 'rock' :
                                    print(rock)
                                elif y == 'paper' :
                                    print(paper)
                                print('\n',y)
                                print("\n you've lost! \n")
                                counter2 += 1
                                continue
                            elif  ((y == 'scissors' and z == 'c') or (y == 'rock' and z == 'a') or (y == 'paper' and z == 'b')) :
                                if y == 'scissors' :
                                    print(scissors)
                                elif y == 'rock' :
                                    print(rock)
                                elif y == 'paper' :
                                    print(paper)
                                print('\n',y)
                                print("\n you are tied!\n")
                                counter3 += 1
                                continue
                            else :
                                print('\n invalid! \n')
                        if counter1 > counter2 :
                            print("\n you've won")
                            print(' your total score is',(counter1 - counter2),'\n') 
                        elif counter2 > counter1 :
                            print("\n you've lost")
                            print(' your total score is',(counter2 - counter1),'\n')
                        elif counter3 == 3 :
                            print("\n you are tied in total")
                            print(" your total score is",counter1,'\n')
                        
                        print('game over \n')
                        break
                    elif x == 'c' :
                        counter1 = 0
                        counter2 = 0
                        counter3 = 0
                        while True :    
                            print('\n a. rock')
                            print(' b. paper')
                            print(' c. scissors\n')
                            if (counter1 + counter2 + counter3) == 5 :
                                break
                            z = input('choose rock,paper or scissors: ')
                            num = random.randint(0,2)
                            y = options_list[num]
                            if ((y == 'scissors' and z == 'a') or (y == 'rock' and z == 'b') or (y == 'paper' and z == 'c')) :
                                if y == 'scissors' :
                                    print(scissors)
                                elif y == 'rock' :
                                    print(rock)
                                elif y == 'paper' :
                                    print(paper)
                                print('\n',y)
                                print("\n you've won this round! \n")
                                counter1 += 1
                                continue
                            elif ((y == 'scissors' and z == 'b') or (y == 'rock' and z == 'c') or (y == 'paper' and z == 'a')) :
                                if y == 'scissors' :
                                    print(scissors)
                                elif y == 'rock' :
                                    print(rock)
                                elif y == 'paper' :
                                    print(paper)
                                print('\n',y)
                                print("\n you've lost this round! \n")
                                counter2 += 1
                                continue
                            elif  ((y == 'scissors' and z == 'c') or (y == 'rock' and z == 'a') or (y == 'paper' and z == 'b')) :
                                if y == 'scissors' :
                                    print(scissors)
                                elif y == 'rock' :
                                    print(rock)
                                elif y == 'paper' :
                                    print(paper)
                                print('\n',y)
                                print("\n you are tied this round!\n")
                                counter3 += 1
                                continue
                            else :
                                print('\n invalid \n')
                        if counter1 > counter2 :
                            print("\n you've won")
                            print(' your total score is',(counter1 - counter2),'\n') 
                        elif counter2 > counter1 :
                            print("\n you've lost")
                            print(' your total score is',(counter2 - counter1),'\n')
                        elif counter1 == counter2 :
                            print("\n you are tied in total")
                            print(" your total score is",counter1,'\n')
                        
                        print('game over \n')
                        break
                    else :
                        print('\n invalid! \n')
                break
            else :
                print('\n invalid! \n')
    elif x == 'q' :
        print('\n game over! \n')
        print(' thanks for playing \n')
        break
    else :
        print('\n invalid \n') 