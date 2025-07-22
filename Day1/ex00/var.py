def my_var():
    ft_int = 42
    ft_str = "42"
    ft_string = "quarante-deux"
    ft_float = 42.0
    ft_bool = True
    ft_list = [42]
    ft_dict = {42: 42}
    ft_tuple = (42,)
    ft_set = set()

    print(ft_int, "est de type", type(ft_int))
    print(ft_str, "est de type", type(ft_str))
    print(ft_string, "est de type", type(ft_string))
    print(ft_float, "est de type", type(ft_float))
    print(ft_bool, "est de type", type(ft_bool))
    print(ft_list, "est de type", type(ft_list))
    print(ft_dict, "est de type", type(ft_dict))
    print(ft_tuple, "est de type", type(ft_tuple))
    print(ft_set, "est de type", type(ft_set))

if __name__ == '__main__':
    my_var()
