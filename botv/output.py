class Output:


    def __init__(self, response=None):
        self.platform = "facebook"
        self.__quickReplies = []
        self.__templates= []
        self.__output=dict()
        self.__entities = dict()

        self.__platform = dict(quickReplies=self.__quickReplies, templates=self.__templates) 
        self.__output[self.platform] = self.__platform
        self.__body = dict(
                output = self.__output,
                entities = self.__entities
                )
        if response:
            self.__output['response'] = response

    @property
    def as_dict(self):
        if not self.__entities:
            self.__body.pop('entities', None)

        for key in list(self.__platform.keys()):
            if not self.__platform[key] :
                del self.__platform[key]

        for key in list(self.__output.keys()):
            if not self.__output[key] :
                del self.__output[key]


        return self.__body


    @property
    def entities(self):
        return self.__entities

    @property
    def quickReplies(self):
        return self.__quickReplies

    @property
    def templates(self):
        return self.__templates


    def add_entity(self, **kwgs):
        for key,value in kwgs.items():
            self.__entities[key] = value
        self.__body['entities'] = self.__entities
        return self.as_dict

    def add_response(self, response):
        self.__output['response'] = response
        return self.as_dict

    def add_qr(self, quick_replies, platform="facebook"):
        keys = ['targetIntent', 'text', 'title', 'replyType']
        assert  quick_replies and all(key in keys for key in [[*i] for i in quick_replies][0]) ,"check your quick reply object"
        self.__output[platform] = self.__platform 
        self.__quickReplies.extend(quick_replies)
        self.__output[platform]["quickReplies"] = self.__quickReplies
        return self.as_dict

    def add_template(self,templates, platform="facebook"):
        self.__output[platform] = self.__platform 
        keys = ['actionUrl', 'imageUrl', 'subtitle', 'title']
        assert templates and all(key in keys for key in [[*i] for i in templates][0]),"check your quick template object"
        self.__templates.extend(templates)
        self.__output[platform]["templates"] = self.__templates
        return self.as_dict


