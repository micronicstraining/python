print("Hello from package_with_side_effect!")

if __name__ == '__main__':
    print('My init is being executed')
else:
    print(__name__, 'I am being imported somewhere')
