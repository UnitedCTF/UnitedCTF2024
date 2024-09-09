from function import api


async def run_navigation(session, ws):
    print('Welcome to the Attractions App!')

    print('\t1. View attractions')
    if session.logged_in:
        print('\t2. Logout')
    else:
        print('\t2. Login')
    print('\t3. Flags')
    print('\t4. Register')
    print('\t5. Exit')

    choice = get_choice(1, 5)
    if choice == '1':
        await attractions(ws)
    elif choice == '2':
        if session.logged_in:
            await logout(session, ws)
        else:
            await login(session, ws)
    elif choice == '3':
        if session.logged_in:
            await flags(session, ws)
        else:
            print('\tYou need to be logged in to view flags')
    elif choice == '4':
        await register(ws)
    else:
        session.connected = False
        print('Goodbye!')
    print()


def get_choice(minimum, maximum):
    choice = input('Enter your choice: ')
    while not choice.isdigit() or int(choice) < minimum or int(choice) > maximum:
        choice = input('Enter a valid choice: ')
    return choice


async def attractions(ws):
    response = await api.get_attractions(ws)
    for i in range(len(response)):
        print(f'\t{i + 1}. {response[i]}')

    choice = get_choice(1, len(response))
    response = await api.get_attraction(ws, response[int(choice) - 1])
    for key, value in response.items():
        if type(value) == str:
            val = value.replace("\n", "\n\t\t")
        else:
            val = value
        print(f'\t{key}: {val}')


async def login(session, ws):
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    response = await api.login(ws, session, username, password)
    if response:
        print('Login successful')
        session.logged_in = True
    else:
        print('Login failed')
        session.logged_in = False
    print()


async def logout(session, ws):
    response = await api.logout(ws, session)
    if response:
        print('Logout successful')
        session.logged_in = False
    else:
        print('Logout failed')
    print()

async def flags(session, ws):
    print('Flags:')
    user_flags = await api.get_flags(ws, session)
    if user_flags is not None:
        if len(user_flags) == 0:
            print('\tNo flags found')
        else:
            for flag in user_flags:
                print(f'\t{flag}')
    else:
        print('\tFailed to retrieve flags')


async def register(ws):
    print('Register:')
    username = input('\tEnter your username: ')
    password = input('\tEnter your password: ')
    confirm = input('\tConfirm your password: ')
    if password != confirm:
        print('\t\tPasswords do not match')
        return
    email = input('\tEnter your email: ')

    response = await api.register(ws, username, password, email)
    if response:
        print('\tRegistration successful')
    else:
        print('\tRegistration failed')
    print()