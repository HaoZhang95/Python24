# -*- coding: utf-8 -*-
# python xml.etree.ElementTree

import os
import xml.etree.ElementTree as ET
from xml.dom import minidom


class xmltojson:
    # global var
    # show log
    SHOW_LOG = True
    # XML file
    XML_PATH = None
    a = {}
    m = []

    def get_root(self, path):
        '''parse the XML file,and get the tree of the XML file
        finally,return the root element of the tree.
        if the XML file dose not exist,then print the information'''
        # if os.path.exists(path):
        # if SHOW_LOG:
        # print('start to parse the file : [{}]'.format(path))
        tree = ET.fromstring(path)
        return tree
        # else:
        # print('the path [{}] dose not exist!'.format(path))

    def get_element_tag(self, element):
        '''return the element tag if the element is not None.'''
        if element is not None:

            return element.tag
        else:
            print('the element is None!')

    def get_element_attrib(self, element):
        '''return the element attrib if the element is not None.'''
        if element is not None:

            return element.attrib
        else:
            print('the element is None!')

    def get_element_text(self, element):
        '''return the text of the element.'''
        if element is not None:
            return element.text
        else:
            print('the element is None!')

    def get_element_children(self, element):
        '''return the element children if the element is not None.'''
        if element is not None:

            return [c for c in element]
        else:
            print('the element is None!')

    def get_elements_tag(self, elements):
        '''return the list of tags of element's tag'''
        if elements is not None:
            tags = []
            for e in elements:
                tags.append(e.tag)
            return tags
        else:
            print('the elements is None!')

    def get_elements_attrib(self, elements):
        '''return the list of attribs of element's attrib'''
        if elements is not None:
            attribs = []
            for a in elements:
                attribs.append(a.attrib)
            return attribs
        else:
            print('the elements is None!')

    def get_elements_text(self, elements):
        '''return the dict of element'''
        if elements is not None:
            text = []
            for t in elements:
                text.append(t.text)
            return dict(zip(self.get_elements_tag(elements), text))
        else:
            print('the elements is None!')

    def main(self, xml):
        # root
        root = self.get_root(xml)

        # children
        children = self.get_element_children(root)

        children_tags = self.get_elements_tag(children)

        children_attribs = self.get_elements_attrib(children)

        i = 0

        # 获取二级元素的每一个子节点的名称和值
        for c in children:
            p = 0
            c_children = self.get_element_children(c)
            dict_text = self.get_elements_text(c_children)
            if dict_text:
                # print (children_tags[i])
                if children_tags[i] == 'TemplateSMS':
                    self.a['templateSMS'] = dict_text
                else:
                    if children_tags[i] == 'SubAccount':
                        k = 0

                        for x in children:
                            if children_tags[k] == 'totalCount':
                                self.m.append(dict_text)
                                self.a['SubAccount'] = self.m
                                p = 1
                            k = k + 1
                        if p == 0:
                            self.a[children_tags[i]] = dict_text
                    else:
                        self.a[children_tags[i]] = dict_text


            else:
                self.a[children_tags[i]] = c.text
            i = i + 1
        return self.a

    def main2(self, xml):
        # root
        root = self.get_root(xml)

        # children
        children = self.get_element_children(root)

        children_tags = self.get_elements_tag(children)

        children_attribs = self.get_elements_attrib(children)

        i = 0

        # 获取二级元素的每一个子节点的名称和值
        for c in children:
            p = 0
            c_children = self.get_element_children(c)
            dict_text = self.get_elements_text(c_children)
            if dict_text:
                if children_tags[i] == 'TemplateSMS':
                    k = 0

                    for x in children:
                        if children_tags[k] == 'totalCount':
                            self.m.append(dict_text)
                            self.a['TemplateSMS'] = self.m
                            p = 1
                        k = k + 1
                    if p == 0:
                        self.a[children_tags[i]] = dict_text
                else:
                    self.a[children_tags[i]] = dict_text

            else:
                self.a[children_tags[i]] = c.text
            i = i + 1
        return self.a
