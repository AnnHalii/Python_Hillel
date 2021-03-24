import random

try:
    raise random.choice([ZeroDivisionError, ImportError, KeyError, UnicodeError, StopIteration])
except ZeroDivisionError:
    print('ZeroDivisionError')
except ImportError:
    print('ImportError')
except KeyError:
    print('KeyError')
except UnicodeError:
    print('UnicodeError')
except StopIteration:
    print('StopIteration')
