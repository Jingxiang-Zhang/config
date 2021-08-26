from Crypto.Cipher import AES
import base64


class Aescrypt():
    """
    用于文件的加密和解密模块，采用AEC进行加密
    """

    def __init__(self, key, model, iv=b"", encode_="gbk"):
        """
        :param key: 用于加密、解密的秘钥
        :param model: 加密模式，可选ECB或CBC
        :param iv: CBC模式使用
        :param encode_: 编码类型
        """
        self.encode_ = encode_
        self.model = {'ECB': AES.MODE_ECB, 'CBC': AES.MODE_CBC}[model]
        self.key = self.__add_16(key)
        if model == 'ECB':
            self.aes = AES.new(self.key, self.model)  # 创建一个aes对象
        elif model == 'CBC':
            self.aes = AES.new(self.key, self.model, iv)  # 创建一个aes对象

        # 这里的密钥长度必须是16、24或32，目前16位的就够用了

    def __add_16(self, par):
        par = par.encode(self.encode_)
        while len(par) % 16 != 0:
            par += b'\x00'
        return par

    def aesencrypt(self, text):
        """
        将指定的文本进行加密
        :param text: 待加密的文本
        :return: 加密后的文本
        """
        text = self.__add_16(text)
        self.encrypt_text = self.aes.encrypt(text)
        return base64.encodebytes(self.encrypt_text).decode().strip()

    def aesdecrypt(self, text):
        """
        用于对指定文本进行解密
        :param text: 待解密的文本
        :return: 解密后的文本
        """
        text = base64.decodebytes(text.encode(self.encode_))
        self.decrypt_text = self.aes.decrypt(text)
        return self.decrypt_text.decode(self.encode_).strip('\0')
