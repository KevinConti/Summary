__author__ = 'Kevin'
#Running on python2.7

import ConfigParser

config = ConfigParser.ConfigParser()
cfg_file = open('config.ini', 'r+')
config.readfp(cfg_file)


def set_user(cfg_file, config):
    is_correct = False
    while is_correct == False:
        username = raw_input('Please enter your Reddit username: ')
        print 'Is', username, 'correct? (y/n)'
        y_or_n = raw_input()
        if y_or_n == 'y':
            is_correct = True
        elif y_or_n != 'n':
            print("Input error")
            raise ValueError("Needed to input 'y' or 'n'")
    config.add_section('User')
    config.set('User','Reddit_Username',username)
    config.write(cfg_file)

if len(config.sections()) == 0:
    print("Setting Reddit Username...")
    set_user(cfg_file, config)



cfg_file.close()








