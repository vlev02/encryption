# -*- coding: utf-8 -*-
"""
实现对文本的加密。
"""

__all__ = ['Encryp','enCode','deCode']

class Encryp():
    '''
    实现字符串加密的加密器。
    args:
        seed 加密方式，不同seed的加密器产生不同的加密结果。
    attributes:
        __words, <str> 需要乱序加密的词库
        __value, <list()> 乱序加密映射规则
        __enDic, <dict> 加密字典
        __deDic, <dict> 解密字典
    '''
    def __init__(self, seed = None):
        
        words = '0123456789abcdef'
        value = []
        if seed == None:
            value = [1, 11, 6, 4, 3, 2, 10, 8, 15, 13, 9, 12, 14, 0, 5, 7]
            value = ''.join([words[v] for v in value])
        else:
            words_ = words
            value = []
            length = len(words_)
            while length:
                seed, ind = seed//length, seed%length
                value.append(words_[ind])
                words_ = words_[ind+1:]+words_[:ind]
                length -= 1
    
        self.__words = words
        self.__value = value
        
        self.__DictsUpdate()
        return
    
    
    def __DictsUpdate(self,):
        '''
        更新加密字典和解密字典
        '''
        self.__enDic = dict([(k,v) for k,v in zip(self.__words,self.__value)])
        self.__deDic = dict([(v,k) for k,v in self.__enDic.items()])
        return
    
    def enCode(self, m):
        '''
        将明文加密成数值
        
        args:
            m, <str> 需要加密的明文 (utf-8)
        '''
        if not m: return 0
        b = m.encode()
        bytes2hex = lambda b : ''.join(['{:x}'.format(byte) for byte in b])
        s = bytes2hex(b)
        S = s[0]
        for word in s[1::]:
            S += self.__enDic.get(word,word)
        I =  int(S,16)
        return I
    
    def deCode(self, I):
        '''
        将数值解密成明文 (utf-8)
        
        args:
            I, <int> 需要解密的数值
        '''
        if not I: return ''
        S = hex(I)[2:]
        s = S[0]
        for Word in S[1::]:
            s += self.__deDic.get(Word,Word)
        b = bytes.fromhex(s)
        m = b.decode()
        return m
    
    

def enCode(m, seed = None):
    return Encryp(seed).enCode(m)

def deCode(I, seed = None):
    return Encryp(seed).deCode(I)