from .read_file import Read


class CheckPwd:
    def __init__(self):
        pass

    @staticmethod
    def check_pwd_input_with_force(path, group=("emile", "sql", "key", "sql_development"),
                                   msg_input="please input password: ",
                                   msg_error="please try again: ",
                                   msg_end="password error, system exit",
                                   max_try_time=3):
        """
        用于便捷的进行密码的输入
        :param path: config文件路径
        :param group:
            需要提取的组标签，例如需要xml文件中的emile和key元素下的所有键值对，则使用
            ("emile", "key")
        :param msg_input: 输入密码提示信息
        :param msg_error: 密码错误提示信息
        :param msg_end: 达到密码尝试次数上限后的提示信息
        :param max_try_time: 密码尝试次数上限
        :return:
        """
        pwd = input(msg_input)
        for i in range(max_try_time):
            try:
                if pwd != "":
                    file = Read(pwd)
                else:
                    file = Read()
                file = file.read(path)
                try:
                    ret = Read.tile(xml_=file, element_list=group, interpret=True)
                except Exception:
                    raise Exception("file is encrypted, password is needed")
                break
            except Exception as e:
                print("error: ",str(e))
                if i != max_try_time - 1:
                    pwd = input(msg_error)
                else:
                    print(msg_end)
                    exit(0)

        return ret
