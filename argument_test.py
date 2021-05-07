def arguments(name, *args, **arguments):
    '''
    help 메세지(설명 메세지)
    '''
    print(name)
    for arg in args:
        print(arg)
    for kwarg, kwargs in arguments.items():
        print(kwarg, "======", kwargs)

주인장이름 = 'suzy'
가 = '1st'
나 = '2st'
다 = '3st'

help(arguments)
arguments(주인장이름, 가, 나, 다, test1=10, test2=20, test3=30)


