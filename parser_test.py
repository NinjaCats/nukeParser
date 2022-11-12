import unittest
import parser

class TestNukeSciptParser(unittest.TestCase):
    def test_parse_nuke_sciprt(self):
        f = "test.nk"
        nodes = parser.Nodes.regsiterNode(f)

        for i in nodes:
            _name = i.name
            _className = i.nodeClass
            _file = i.getAttr('_file')
            print(f'nodeName: {_name}\nnodeType: {_className}\nnodeValue: {_file}')



if __name__ == "__main__":
    unittest.main()