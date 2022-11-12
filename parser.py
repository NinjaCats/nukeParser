#coding: utf-8

import re
from typing import List, Any, Pattern


def readScript(f: str) -> str:
    with open(f, 'rt') as nukeScript:
        return nukeScript.read()


def parser(parser: Pattern, code: str) -> list[dict]:
    m = parser.finditer(code)
    return [i.groupdict() for i in m]


class Parser(object):
    parserNode = re.compile(r"(?P<node>^\w+) (?P<value>{(?:[^}]|\n)+})", re.M)
    parserParamter = re.compile(r' (?P<attr>\w+) (?P<value>.+)$', re.M)


class Node(object):
    def __init__(self, nodeClass: str) -> None:
        self.__attrs: List[str] = []
        self.nodeClass = nodeClass

    @property
    def name(self) -> str:
        return self.getAttr('_name')

    def setAttr(self, attr: str, value: str):
        self.__attrs.append(attr)
        setattr(self, f'_{attr}', value)

    def getAttr(self, attr: str) -> Any:
        if hasattr(self, '_name'):
            return getattr(self, attr)
        else:
            return None

    def getAttrs(self) -> List[str]:
        return self.__attrs

    def clearAttrs(self):
        self.__attrs = []


class Nodes(object):
    def __iter__(self):
        self.__max = len(self.__m)
        self.__i = 0
        return self

    def __next__(self) -> Node:
        if self.__i < self.__max:
            _rat = self.__m[self.__i]
            self.__i += 1
            return _rat
        else:
            raise StopIteration

    def __init__(self) -> None:
        self.__m: List[Node] = []

    @classmethod
    def regsiterNode(cls, scriptFile: str):
        _codes = readScript(scriptFile)

        thisNode = cls()
        nodes = parser(Parser.parserNode, _codes)
        for i in nodes:
            thisNode.addNode(i['node'], i['value'])

        return thisNode

    def addNode(self, node: str, value: str):
        _node = Node(node)
        self.__m.append(_node)
        _attrs = parser(Parser.parserParamter, value)
        for i in _attrs:
            _node.setAttr(i['attr'], i['value'])
