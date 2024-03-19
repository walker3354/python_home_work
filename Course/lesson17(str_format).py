
def main():
    animal = 'cow'
    item = 'moon'

    print(f'The {animal} cross the {item}')
    print('The {} cross the {}'.format(animal, item))
    # we can assign the specific variable to access
    print('The {0} cross the {1}'.format(animal, item))
    # or we can give hime name to access like function
    print('The {persion} cross the {road}'.format(
        persion='walker', road='high way'))

    # we can also use the format methood as a string
    greeting_txt = "hi {usr_name} welcome to the system"
    print(greeting_txt.format(usr_name='walker'))

    # remember the index operator []? the format also can set the limit like that
    name = 'walker'
    print('welcom home {} .I miss you'.format(name))
    print('welcom home {:10}.I miss you'.format(name))
    print('welcom home {:<10}.I miss you'.format(name))
    print('welcom home {:>10}.I miss you'.format(name))
    print('welcom home {:^10}.I miss you'.format(name))
    '''
    welcom home walker
    welcom home walker    
    welcom home walker    
    welcom home     walker
    welcom home   walker  
    '''


main()
