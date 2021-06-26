import re
class Sheet:

    def __init__(self):
        self.capacity = {}

    def get(self, column: str):
        """
        该函数的目的是获取在column列的值，内容为等式的话需要计算并返回其结果。举例，若在"A1"列存储的值为"=7+3"，sheet.get("A1")应返回"10"。
        :param column: 列数
        :return: 该列存储的值，默认为空字符串
        """
        value = self.capacity.get(column, '')
        keys = self.capacity.keys()

        if value.strip().isdigit():
            value = value.strip()

        if value and value[0] == '=':
            # 避免循环
            if column == value.strip('='):
                return "#Circular"

            # 正确获取其它列的值
            if value.strip('=') in keys:
                value = self.capacity.get(value.strip('='))

            if (value.find('*') or value.find('+')) or value.count('(') > 1:
                try:
                    value = eval(value.strip('='))
                except:
                    value = ValueError("#Error")

                value = f'{value}'

        return value

    def getLiteral(self, column:str):
        """
        该函数的目的是获取在column列的字符串值，内容为等式的话不需要计算，直接返回字符串。举例，若在"A1"列存储的值为"=7+3"，sheet.getLiteral("A1")应返回"=7+3"。
        :param column: 列数
        :return: 该列存储的字符串值，默认为空字符串
        """
        value = self.capacity[column]

        if value:
            return value
        else:
            raise NotImplementedError("Not implemented!")

    def put(self, column: str, value: str):
        """
        该函数的目的是在column列存储value的值。如果该列已经被占用，则替换为当前值。
        :param column: 列数
        :param value: 在该列需要存储的值
        """
        # 避免循环引用
        if column:
            self.capacity[column] = value
        else:
            raise NotImplementedError("Not implemented!")