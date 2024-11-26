class NodeParse:
    def __init__(self, selector):
        self.selector = selector

    def to_text(self):
        list = []
        for s in self.selector:
            if s.xpath("//style").get() is not None:
                list.append('')
            if s.xpath('/node()').get() is not None:
                list.append(''
                            .join(s.xpath('string(.)').get())
                            .replace('\n', '')
                            .replace('\t', '')
                            .replace('\r', '')
                            .replace('\u3000', '')
                            .replace('\xa0', '')
                            .replace(' ', '')
                            .strip())
        return ''.join(list)


def node_text(s):
    list = []
    if s.xpath("//style").get() is not None:
        list.append('')
    if s.xpath('/node()').get() is not None:
        list.append(''
                    .join(s.xpath('string(.)').get())
                    .replace('\n', '')
                    .replace('\t', '')
                    .replace('\u3000', '')
                    .replace('\xa0', '')
                    .replace(' ', '')
                    .strip())
    return ''.join(list)
