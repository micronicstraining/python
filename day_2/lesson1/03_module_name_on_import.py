#! /usr/bin/env python3
import module_with_side_effect as se1

print(se1.__name__)

if __name__ == '__main__':
    print('I am being executed')
    import module_with_side_effect_2 as se2
    print('Hello from 03', se2.__name__)
else:
    print('I am being imported')
    import module_with_side_effect_2 as se2
    print(se2.__name__)