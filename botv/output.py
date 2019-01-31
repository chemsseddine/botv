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
        self.__output[platform] = self.__platform 
        keys = ['targetIntent', 'text', 'title', 'type']
        for key in keys:
            for quick_reply in quick_replies:
                if key not in quick_reply:
                    raise ValueError('Quick Reply should have these keys : targetIntent, text, title, type')
        self.__quickReplies.extend(quick_replies)
        self.__output[platform]["quickReplies"] = self.__quickReplies
        return self.as_dict

    def add_template(self,templates, platform="facebook"):
        self.__output[platform] = self.__platform 
        keys = ['action_url', 'image_url', 'subtitle', 'title']
        for key in keys:
            for template in templates:
                if key not in template:
                    raise ValueError('Facebook template should have these keys : action_url, image_url, subtitle, title')
        self.__templates.extend(templates)
        self.__output[platform]["templates"] = self.__templates
        return self.as_dict


