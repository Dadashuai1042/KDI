import os
import json
from lib2to3.pytree import Node

from py2neo import Graph, NodeMatcher
from loguru import logger
import sys

logger.add(sys.stdout, format="{time} - {level} - {message}", filter="sub.module")

class KnowledgeGraph:
    def __init__(self):
        self.graph_ = Graph(host="localhost", port=7687, auth=('neo4j', '123456'))  # 您的数据库连接信息
        self.matcher = NodeMatcher(self.graph_)

    def _createNode(self, label, name, properties=None):
        # 创建节点，如果已存在则不创建
        if properties is None:
            properties = {}
        node = self.graph_.nodes.match(label, name=name)
        if not node:
            node = Node(label, name=name, **properties)
            self.graph_.create(node)

    def findNode(self, label, name):
        # 查找节点，返回找到的第一个节点
        return self.graph_.nodes.match(label, name=name).first()

    def importMilitaryStrength(self, data):
        # 导入军事实力数据
        for country_data in data['Sheet1']:
            country_name = country_data['Country']
            power_index = country_data['PwrIndex']
            # 为每个国家创建一个节点，如果节点已存在则更新其属性
            self._createNode('Country', country_name, {'PwrIndex': power_index})

def main():
    graph = KnowledgeGraph()
    # 假设您已经有了一个包含军事实力数据的JSON对象
    military_strength_data = {
        "Sheet1": [
            # ... 这里是您提供的JSON数据中的相关部分 ...
                        {"Rank": 1, "Country": "United States", "PwrIndex": 0.0699},
                        {"Rank": 2, "Country": "Russia", "PwrIndex": 0.0702},
                        {"Rank": 3, "Country": "China", "PwrIndex": 0.0706},
                        {"Rank": 4, "Country": "India", "PwrIndex": 0.1023},
                        {"Rank": 5, "Country": "South Korea", "PwrIndex": 0.1416},
                        {"Rank": 6, "Country": "United Kingdom", "PwrIndex": 0.1443},
                        {"Rank": 7, "Country": "Japan", "PwrIndex": 0.1601},
                        {"Rank": 8, "Country": "Turkiye", "PwrIndex": 0.1697},
                        {"Rank": 9, "Country": "Pakistan", "PwrIndex": 0.1711},
                        {"Rank": 10, "Country": "Italy", "PwrIndex": 0.1863},
                        {"Rank": 11, "Country": "France", "PwrIndex": 0.1878},
                        {"Rank": 12, "Country": "Brazil", "PwrIndex": 0.1944},
                        {"Rank": 13, "Country": "Indonesia", "PwrIndex": 0.2251},
                        {"Rank": 14, "Country": "Iran", "PwrIndex": 0.2269},
                        {"Rank": 15, "Country": "Egypt", "PwrIndex": 0.2283},
                        {"Rank": 16, "Country": "Australia", "PwrIndex": 0.2515},
                        {"Rank": 17, "Country": "Israel", "PwrIndex": 0.2596},
                        {"Rank": 18, "Country": "Ukraine", "PwrIndex": 0.2598},
                        {"Rank": 19, "Country": "Germany", "PwrIndex": 0.2847},
                        {"Rank": 20, "Country": "Spain", "PwrIndex": 0.2882},
                        {"Rank": 21, "Country": "Poland", "PwrIndex": 0.2917},
                        {"Rank": 22, "Country": "Vietnam", "PwrIndex": 0.3158},
                        {"Rank": 23, "Country": "Saudi Arabia", "PwrIndex": 0.3235},
                        {"Rank": 24, "Country": "Thailand", "PwrIndex": 0.3389},
                        {"Rank": 25, "Country": "Algeria", "PwrIndex": 0.3589},
                        {"Rank": 26, "Country": "Canada", "PwrIndex": 0.3813},
                        {"Rank": 27, "Country": "Argentina", "PwrIndex": 0.3823},
                        {"Rank": 28, "Country": "Sweden", "PwrIndex": 0.4009},
                        {"Rank": 29, "Country": "Singapore", "PwrIndex": 0.4087},
                        {"Rank": 30, "Country": "Mexico", "PwrIndex": 0.4274},
                        {"Rank": 31, "Country": "Greece", "PwrIndex": 0.4349},
                        {"Rank": 32, "Country": "South Africa", "PwrIndex": 0.4632},
                        {"Rank": 33, "Country": "Philippines", "PwrIndex": 0.4691},
                        {"Rank": 34, "Country": "Myanmar", "PwrIndex": 0.5251},
                        {"Rank": 35, "Country": "North Korea", "PwrIndex": 0.5313},
                        {"Rank": 36, "Country": "Bangladesh", "PwrIndex": 0.5419},
                        {"Rank": 37, "Country": "Portugal", "PwrIndex": 0.5609},
                        {"Rank": 38, "Country": "Nigeria", "PwrIndex": 0.5619},
                        {"Rank": 39, "Country": "Netherlands", "PwrIndex": 0.5644},
                        {"Rank": 40, "Country": "Norway", "PwrIndex": 0.5664},
                        {"Rank": 41, "Country": "Malaysia", "PwrIndex": 0.5992},
                        {"Rank": 42, "Country": "Switzerland", "PwrIndex": 0.6097},
                        {"Rank": 43, "Country": "Colombia", "PwrIndex": 0.7347},
                        {"Rank": 44, "Country": "Iraq", "PwrIndex": 0.7441},
                        {"Rank": 45, "Country": "Czechia", "PwrIndex": 0.7712},
                        {"Rank": 46, "Country": "Romandia", "PwrIndex": 0.7712},
                        {"Rank": 47, "Country": "Denmark", "PwrIndex": 0.7743},
                        {"Rank": 48, "Country": "Ethiopia", "PwrIndex": 0.7938},
                        {"Rank": 49, "Country": "Finland", "PwrIndex": 0.7967},
                        {"Rank": 50, "Country": "United Arab Emirates", "PwrIndex": 0.8083},
                        {"Rank": 51, "Country": "Chile", "PwrIndex": 0.8128},
                        {"Rank": 52, "Country": "Peru", "PwrIndex": 0.8475},
                        {"Rank": 53, "Country": "Hungary", "PwrIndex": 0.8478},
                        {"Rank": 54, "Country": "Angola", "PwrIndex": 0.8702},
                        {"Rank": 55, "Country": "Serbia", "PwrIndex": 0.9038},
                        {"Rank": 56, "Country": "Venezuela", "PwrIndex": 0.9447},
                        {"Rank": 57, "Country": "Kazakhstan", "PwrIndex": 0.9495},
                        {"Rank": 58, "Country": "Azerbaijian", "PwrIndex": 0.9934},
                        {"Rank": 59, "Country": "Syria", "PwrIndex": 1.0026},
                        {"Rank": 60, "Country": "Morocco", "PwrIndex": 1.0081},
                        {"Rank": 61, "Country": "Bulgaria", "PwrIndex": 1.0132},
                        {"Rank": 62, "Country": "Qatar", "PwrIndex": 1.0789},
                        {"Rank": 63, "Country": "Belarus", "PwrIndex": 1.0901},
                        {"Rank": 64, "Country": "Uzbekistan", "PwrIndex": 1.1069},
                        {"Rank": 65, "Country": "Croatia", "PwrIndex": 1.1333},
                        {"Rank": 66, "Country": "New Zealand", "PwrIndex": 1.1844},
                        {"Rank": 67, "Country": "Cuba", "PwrIndex": 1.1869},
                        {"Rank": 68, "Country": "Slovakia", "PwrIndex": 1.1891},
                        {"Rank": 69, "Country": "Belgium", "PwrIndex": 1.2064},
                        {"Rank": 70, "Country": "Austria", "PwrIndex": 1.2351},
                        {"Rank": 71, "Country": "Ecuador", "PwrIndex": 1.2388},
                        {"Rank": 72, "Country": "Democratic Republic of the Congo", "PwrIndex": 1.2491},
                        {"Rank": 73, "Country": "Tunisia", "PwrIndex": 1.2881},
                        {"Rank": 74, "Country": "Sri Lanka", "PwrIndex": 1.3459},
                        {"Rank": 75, "Country": "Sudan", "PwrIndex": 1.4119},
                        {"Rank": 76, "Country": "Kuwait", "PwrIndex": 1.4261},
                        {"Rank": 77, "Country": "Oman", "PwrIndex": 1.4448},
                        {"Rank": 78, "Country": "Libya", "PwrIndex": 1.4449},
                        {"Rank": 79, "Country": "Jordan", "PwrIndex": 1.4651},
                        {"Rank": 80, "Country": "Yemen", "PwrIndex": 1.4692},
                        {"Rank": 81, "Country": "Bolivia", "PwrIndex": 1.4851},
                        {"Rank": 82, "Country": "Turmenistan", "PwrIndex": 1.4906},
                        {"Rank": 83, "Country": "Georgia", "PwrIndex": 1.6969},
                        {"Rank": 84, "Country": "Paraguay", "PwrIndex": 1.7053},
                        {"Rank": 85, "Country": "Bahrain", "PwrIndex": 1.7163},
                        {"Rank": 86, "Country": "Estonia", "PwrIndex": 1.7237},
                        {"Rank": 87, "Country": "Lithuania", "PwrIndex": 1.7395},
                        {"Rank": 88, "Country": "Kenya", "PwrIndex": 1.7629},
                        {"Rank": 89, "Country": "Albania", "PwrIndex": 1.8188},
                        {"Rank": 90, "Country": "Slovenia", "PwrIndex": 1.8286},
                        {"Rank": 91, "Country": "Mozambique", "PwrIndex": 1.8607},
                        {"Rank": 92, "Country": "Chad", "PwrIndex": 1.8607},
                        {"Rank": 93, "Country": "Ireland", "PwrIndex": 1.8779},
                        {"Rank": 94, "Country": "Honduras", "PwrIndex": 1.9629},
                        {"Rank": 95, "Country": "Uruguay", "PwrIndex": 1.9695},
                        {"Rank": 96, "Country": "Zambia", "PwrIndex": 1.9851},
                        {"Rank": 97, "Country": "Ivory Coast", "PwrIndex": 1.9869},
                        {"Rank": 98, "Country": "Latvia", "PwrIndex": 1.9911},
                        {"Rank": 99, "Country": "Kyrgyzstan", "PwrIndex": 2.0057},
                        {"Rank": 100, "Country": "Zimbabwe", "PwrIndex": 2.0352},
                        {"Rank": 101, "Country": "Armenia", "PwrIndex": 2.0583},
                        {"Rank": 102, "Country": "Tanzania", "PwrIndex": 2.0587},
                        {"Rank": 103, "Country": "Cameroon", "PwrIndex": 2.0599},
                        {"Rank": 104, "Country": "Mongolia", "PwrIndex": 2.1079},
                        {"Rank": 105, "Country": "Mali", "PwrIndex": 2.1115},
                        {"Rank": 106, "Country": "Tajikistan", "PwrIndex": 2.1265},
                        {"Rank": 107, "Country": "Guatemala", "PwrIndex": 2.1301},
                        {"Rank": 108, "Country": "Luxembourg", "PwrIndex": 2.1458},
                        {"Rank": 109, "Country": "North Macedonia", "PwrIndex": 2.1717},
                        {"Rank": 110, "Country": "Cambodia", "PwrIndex": 2.1725},
                        {"Rank": 111, "Country": "Laos", "PwrIndex": 2.2071},
                        {"Rank": 112, "Country": "Ghana", "PwrIndex": 2.2358},
                        {"Rank": 113, "Country": "Uganda", "PwrIndex": 2.2405},
                        {"Rank": 114, "Country": "Afghannistan", "PwrIndex": 2.2715},
                        {"Rank": 115, "Country": "Bosnia and Herzegovina", "PwrIndex": 2.3996},
                        {"Rank": 116, "Country": "Eritrea", "PwrIndex": 2.4152},
                        {"Rank": 117, "Country": "Lebanon", "PwrIndex": 2.4283},
                        {"Rank": 118, "Country": "South Sudan", "PwrIndex": 2.4376},
                        {"Rank": 119, "Country": "Nicaragua", "PwrIndex": 2.4889},
                        {"Rank": 120, "Country": "Niger", "PwrIndex": 2.5988},
                        {"Rank": 121, "Country": "Repubic of the Congo", "PwrIndex": 2.7282},
                        {"Rank": 122, "Country": "Dominican Republic", "PwrIndex": 2.7431},
                        {"Rank": 123, "Country": "Namibia", "PwrIndex": 2.7652},
                        {"Rank": 124, "Country": "El Salvador", "PwrIndex": 2.8204},
                        {"Rank": 125, "Country": "Bostswana", "PwrIndex": 2.8353},
                        {"Rank": 126, "Country": "Burkina Faso", "PwrIndex": 2.8962},
                        {"Rank": 127, "Country": "Montenegro", "PwrIndex": 2.9109},
                        {"Rank": 128, "Country": "Senegal", "PwrIndex": 2.9117},
                        {"Rank": 129, "Country": "Mauritania", "PwrIndex": 2.9277},
                        {"Rank": 130, "Country": "Gabon", "PwrIndex": 2.9517},
                        {"Rank": 131, "Country": "Madagascar", "PwrIndex": 3.0655},
                        {"Rank": 132, "Country": "Panama", "PwrIndex": 3.3388},
                        {"Rank": 133, "Country": "Kosovo", "PwrIndex": 3.4115},
                        {"Rank": 134, "Country": "Iceland", "PwrIndex": 3.5038},
                        {"Rank": 135, "Country": "Central African Republic", "PwrIndex": 3.5316},
                        {"Rank": 136, "Country": "Sierra Leone", "PwrIndex": 3.5433},
                        {"Rank": 137, "Country": "Beliz", "PwrIndex": 3.6437},
                        {"Rank": 138, "Country": "Liberia", "PwrIndex": 3.7262},
                        {"Rank": 139, "Country": "Benin", "PwrIndex": 3.8912},
                        {"Rank": 140, "Country": "Somalia", "PwrIndex": 3.9006},
                        {"Rank": 141, "Country": "Suriname", "PwrIndex": 3.9038},
                        {"Rank": 142, "Country": "Moldova", "PwrIndex": 4.2311},
                        {"Rank": 143, "Country": "Bhutan", "PwrIndex": 6.3704}
        ]
    }
    graph.importMilitaryStrength(military_strength_data)

if __name__ == '__main__':
    main()