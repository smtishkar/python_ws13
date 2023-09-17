class MyDict(dict):

    def my_get(self, key_, value_=None):
        try:
            return self[key_]
        except KeyError :
            return value_

if __name__ == '__main__':
    mg = MyDict({'one': 1, 'two': 2})
    print(mg)
    print(mg.my_get('one', 'Good'))
    try:
        print(mg['sdf'])
    except KeyError:
        print('Ошибка')