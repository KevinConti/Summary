__author__ = 'Kevin'
#Running on python2.7

import ConfigParser

config = ConfigParser.ConfigParser()
cfg_file = open('config.ini', 'r+')
config.readfp(cfg_file)

#
def check_input():
    y_or_n = raw_input()
    if y_or_n == 'y':
        return True
    elif y_or_n != 'n':
        print("Input error")
        raise ValueError("Needed to input 'y' or 'n'")
    else:
        return False

#Sets the reddit_username of the user and also creates the [Subs]
#section in the .ini file
def set_user(cfg_file, config):
    is_correct = False
    while is_correct == False:
        username = raw_input('Please enter your Reddit username: ')
        print 'Is', username, 'correct? (y/n)'
        is_correct = check_input()
    config.add_section('User')
    config.set('User','Reddit_Username',username)
    config.add_section('Subs')
    config.write(cfg_file)

if len(config.sections()) == 0:
    print("Setting Reddit Username...")
    set_user(cfg_file, config)


def show_current_config(cfg_file, config):
    print('Your current subreddit configuration:')
    print ''
    print '{0:30}'.format('Subreddit'),'Upvotes_Required'
    options_list = config.options('Subs')
    for option in options_list:
        print '{0:30}'.format(option), config.get('Subs',option)
    print ''

show_current_config(cfg_file, config)

#Iterates through all currents subs and asks user if they want them
#removed
def remove_subs(config):
    for option in config.options('Subs'):
        print 'Would you like to remove', option, '? (y/n)'
        should_remove = check_input()
        if should_remove:
            config.remove_option('Subs',option)
    #TODO not displaying correctly. config.write is causing data to duplicate
    empty_file = open('config.ini', 'r+')
    empty_file.truncate()
    config.write(empty_file)

#Iterates through current results, and then asks
#if more should be added on

def modify_subs(cfg_file, config):
    #TODO iterate through current results, and then allow for more
    #to be added on
    print 'Would you like to remove current subs? (y/n) '
    to_remove = check_input()
    if to_remove:
        cfg_file.close()
        remove_subs(config)
        cfg_file = open('config.ini', 'r+')

print 'Would you like to modify your subs? (y/n) '
need_to_change = check_input()
if (need_to_change):
    modify_subs(cfg_file, config)

cfg_file.close()








